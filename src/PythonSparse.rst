.. include:: sub.txt

.. _systemPythonSparse:

=======================
 PythonSparse system
=======================

The **PythonSparse** system delegates linear system solves (:math:`\mathbf{A}\mathbf{x} = \mathbf{b}`) to user-defined Python objects. Sparse matrix buffers (CSR, CSC, or COO format) are exposed to Python via zero-copy memoryviews, enabling efficient integration with SciPy, CuPy, nvmath, or custom solvers without writing C++ wrappers or recompiling OpenSees. See the CuPy and SciPy examples below.

.. function:: system('PythonSparse', config)
   :noindex:

   Create a linear system that forwards sparse matrix data to a Python solver object. ``config`` is a ``dict`` of solver options; see the table below.

============================   ==================================================================================
``'solver'``                   Python object with a ``solve(**kwargs)`` method (**required**)
``'scheme'``                   Sparse storage format: ``'CSR'``, ``'CSC'``, or ``'COO'``. Default: ``'CSR'``.
``'writable'``                 Buffers the solver may modify: ``'values'``, ``'rhs'``, ``'values,rhs'`` or ``'all'``, or ``'none'``.
                               Also accepts a list: ``['values', 'rhs']``. Default: ``'none'`` — only the solution buffer ``x`` is writable.
============================   ==================================================================================

.. note::

   Enabling ``writable`` for ``values`` or ``rhs`` allows in-place updates of the stiffness matrix and right-hand side vector; use only if you know what you are doing.

The solver object must implement a ``solve(**kwargs)`` method. OpenSees passes matrix data as keyword arguments: memoryviews for arrays and scalars for metadata. Use `numpy.frombuffer <https://numpy.org/doc/stable/reference/generated/numpy.frombuffer.html>`_ to interpret memoryviews as NumPy arrays without copying. The keyword structure depends on ``scheme``:

**CSR/CSC format** — compressed storage uses ``index_ptr`` and ``indices``:

============================   =================   ============================================================
``index_ptr``                  memoryview          Row pointers (CSR) or column pointers (CSC), int32
``indices``                    memoryview          Column indices (CSR) or row indices (CSC), int32
``values``                     memoryview          Matrix coefficients (float64)
``rhs``                        memoryview          Right-hand side vector (float64)
``x``                          memoryview          Solution buffer (float64, writable). Write the solution *in place*.
``num_eqn``                    int                 Number of equations
``nnz``                        int                 Number of nonzeros
``matrix_status``              str                 ``'UNCHANGED'``, ``'COEFFICIENTS_CHANGED'``, or ``'STRUCTURE_CHANGED'``
``storage_scheme``             str                 ``'CSR'``, ``'CSC'``, or ``'COO'``
============================   =================   ============================================================

**COO format** — coordinate storage uses ``row`` and ``col`` instead of ``index_ptr`` / ``indices``:

============================   =================   ============================================================
``row``                        memoryview          Row indices for each nonzero, int32 (COO only)
``col``                        memoryview          Column indices for each nonzero, int32 (COO only)
``values``                     memoryview          Matrix coefficients (float64)
``rhs``                        memoryview          Right-hand side vector (float64)
``x``                          memoryview          Solution buffer (float64, writable). Write the solution *in place*.
``num_eqn``                    int                 Number of equations
``nnz``                        int                 Number of nonzeros
``matrix_status``              str                 ``'UNCHANGED'``, ``'COEFFICIENTS_CHANGED'``, or ``'STRUCTURE_CHANGED'``
``storage_scheme``             str                 ``'COO'``
============================   =================   ============================================================

The ``solve`` method should return ``0`` on success, or a negative value to indicate failure.

.. warning:: **In-place output required**

   You **must** write the solution directly into the ``x`` buffer. OpenSees uses this buffer; it does **not** use return values or new arrays.

   **Do:** Use in-place assignment, e.g. ``np.frombuffer(x, dtype=np.float64, count=num_eqn)[:] = result``

   **Do not:** Return the solution, assign to a new variable, or write to a copy. The result will be ignored and the analysis will use uninitialized or stale data.

.. _pythonSparseExampleCupy:

Example — CuPy conjugate gradient (GPU)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This example uses `CuPy <https://cupy.dev/>`_ and `cupyx.scipy.sparse.linalg.cg <https://docs.cupy.dev/en/stable/reference/generated/cupyx.scipy.sparse.linalg.cg.html>`_ to solve the linear system on an NVIDIA GPU:

.. code-block:: python

   import numpy as np
   import cupy as cp
   import cupyx.scipy.sparse as cupyx_sparse
   import cupyx.scipy.sparse.linalg as cupyx_splinalg
   import openseespy.opensees as ops

   class CuPyCGSolver:
       def __init__(self, rtol=1e-5, atol=1e-12, maxiter=None):
           self.rtol = rtol
           self.atol = atol
           self.maxiter = maxiter
           self.A = None

       def solve(self, **kwargs):
           index_ptr = kwargs['index_ptr']
           indices = kwargs['indices']
           values = kwargs['values']
           rhs = kwargs['rhs']
           x = kwargs['x']
           num_eqn = kwargs['num_eqn']
           nnz = kwargs['nnz']
           matrix_status = kwargs['matrix_status']

           indptr = np.frombuffer(index_ptr, dtype=np.int32, count=num_eqn + 1)
           idx = np.frombuffer(indices, dtype=np.int32, count=nnz)
           vals = np.frombuffer(values, dtype=np.float64, count=nnz)

           if matrix_status == 'STRUCTURE_CHANGED' or self.A is None:
               self.A = cupyx_sparse.csr_matrix(
                   (cp.asarray(vals), cp.asarray(idx), cp.asarray(indptr)),
                   shape=(num_eqn, num_eqn)
               )
           elif matrix_status == 'COEFFICIENTS_CHANGED':
               self.A.data[:] = cp.asarray(vals)

           rhs_gpu = cp.asarray(np.frombuffer(rhs, dtype=np.float64, count=num_eqn))
           x_gpu, info = cupyx_splinalg.cg(
               self.A, rhs_gpu, tol=self.rtol, atol=self.atol, maxiter=self.maxiter
           )

           np.frombuffer(x, dtype=np.float64, count=num_eqn)[:] = cp.asnumpy(x_gpu)
           return -int(info)

   solver = CuPyCGSolver(rtol=1e-8, atol=1e-12, maxiter=1000)
   ops.system('PythonSparse', {'solver': solver, 'scheme': 'CSR'})

.. _pythonSparseExampleScipy:

Example — SciPy direct solve (CPU)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This example uses `SciPy <https://scipy.org/>`_ `factorized <https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.factorized.html>`_ (sparse LU) on CPU:

.. code-block:: python

   import numpy as np
   import scipy.sparse as sp
   import scipy.sparse.linalg as sp_linalg
   import openseespy.opensees as ops

   class SciPyFactorizedSolver:
       def __init__(self):
           self.A = None
           self._solve_func = None

       def solve(self, **kwargs):
           index_ptr = kwargs['index_ptr']
           indices = kwargs['indices']
           values = kwargs['values']
           rhs = kwargs['rhs']
           x = kwargs['x']
           num_eqn = kwargs['num_eqn']
           nnz = kwargs['nnz']
           matrix_status = kwargs['matrix_status']

           indptr = np.frombuffer(index_ptr, dtype=np.int32, count=num_eqn + 1)
           idx = np.frombuffer(indices, dtype=np.int32, count=nnz)
           vals = np.frombuffer(values, dtype=np.float64, count=nnz)

           if matrix_status != 'UNCHANGED' or self._solve_func is None:
               self.A = sp.csr_matrix((vals.copy(), idx.copy(), indptr.copy()),
                                     shape=(num_eqn, num_eqn))
               self._solve_func = sp_linalg.factorized(self.A)

           rhs_arr = np.frombuffer(rhs, dtype=np.float64, count=num_eqn)
           x_arr = np.frombuffer(x, dtype=np.float64, count=num_eqn)
           x_arr[:] = self._solve_func(rhs_arr)
           return 0

   solver = SciPyFactorizedSolver()
   ops.system('PythonSparse', {'solver': solver, 'scheme': 'CSR'})

Code developed by: `gaaraujo <https://github.com/gaaraujo>`_

.. seealso::

   * :ref:`eigenPythonSparse` — PythonSparse interface for generalized eigenvalue problems (``eigen('PythonSparse', ...)``)
   * `EXAMPLES/SolverBenchmark/benchmark_python_sparse.py <https://github.com/OpenSees/OpenSees/blob/master/EXAMPLES/SolverBenchmark/benchmark_python_sparse.py>`_ — benchmark PythonSparse against native solvers
