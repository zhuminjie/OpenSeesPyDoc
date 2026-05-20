.. include:: sub.txt

==================
 eigen command
==================

.. function:: eigen(solver='-genBandArpack', numEigenvalues)

   Eigen value analysis. Return a list of eigen values.

   ================================   ===========================================================================
   numEigenvalues |int|               number of eigenvalues required
   solver |str|                       optional string detailing type of solver: ``'-genBandArpack'``, ``'-fullGenLapack'``, ``'-symmBandLapack'``, or ``'PythonSparse'`` (optional)
   ``config``                         for ``'PythonSparse'`` only: dictionary of solver options; see :ref:`eigenPythonSparse`
   ================================   ===========================================================================

   .. code-block:: python

      eigenvalues = ops.eigen(10)
      eigenvalues = ops.eigen('-fullGenLapack', 10)
      eigenvalues = ops.eigen('standard', '-symmBandLapack', 10)

.. note::

   #. The eigenvectors are stored at the nodes and can be printed out using a Node Recorder, the nodeEigenvector command, or the Print command.
   #. The default eigensolver is able to solve only for N-1 eigenvalues, where N is the number of inertial DOFs. When running into this limitation the -fullGenLapack solver can be used instead of the default Arpack solver.
   #. The -fullGenLapack option is VERY SLOW for moderate to large models

.. _eigenPythonSparse:

PythonSparse eigen solver
-------------------------

.. index::
   single: PythonEigen (see PythonSparse eigen)

The **PythonSparse** eigen interface solves the generalized eigenvalue problem :math:`\mathbf{K}\phi = \lambda \mathbf{M}\phi` using a user-defined Python object. Sparse **K** and **M** buffers are exposed via zero-copy memoryviews so you can call SciPy, CuPy, or a custom eigensolver without recompiling OpenSees.

Call ``ops.eigen('PythonSparse', numEigenvalues, config)``. The ``config`` dictionary accepts:

============================   ==================================================================================
``'solver'``                   Python object with a ``solve(**kwargs)`` method (**required**)
``'scheme'``                   ``'CSR'``, ``'CSC'``, or ``'COO'``. Default: ``'CSR'``.
============================   ==================================================================================

.. note::

   The PythonSparse eigen interface is available only when using the Python interpreter (OpenSeesPy).

The solver object must implement ``solve(**kwargs)``. Keywords depend on ``scheme``:

**CSR/CSC**

============================   =================   ============================================================
``index_ptr``                  memoryview          Row pointers (CSR) or column pointers (CSC), int32
``indices``                    memoryview          Column indices (CSR) or row indices (CSC), int32
``k_values``                   memoryview          Stiffness matrix **K** coefficients (float64)
``m_values``                   memoryview          Mass matrix **M** coefficients (float64)
``eigenvalues``                memoryview          Output buffer for eigenvalues (float64, writable)
``eigenvectors``               memoryview          Output buffer for eigenvectors (float64, writable), row-major by mode
``num_eqn``                    int                 Number of equations
``nnz``                        int                 Number of nonzeros (K and M share sparsity pattern)
``matrix_status``              str                 ``'UNCHANGED'``, ``'COEFFICIENTS_CHANGED'``, or ``'STRUCTURE_CHANGED'``
``storage_scheme``             str                 ``'CSR'``, ``'CSC'``, or ``'COO'``
``num_modes``                  int                 Number of modes requested
``generalized``                bool                ``True``: generalized (K, M); ``False``: standard (K only)
``find_smallest``              bool                ``True``: smallest eigenvalues; ``False``: largest
============================   =================   ============================================================

**COO** — uses ``row_indices`` and ``col_indices`` instead of ``index_ptr`` / ``indices`` (same ``k_values``, ``m_values``, outputs, and metadata as above).

The ``solve`` method should return ``None`` on success, or raise an exception on failure.

.. warning:: **In-place output required**

   Write eigenvalues and eigenvectors into the ``eigenvalues`` and ``eigenvectors`` buffers. OpenSees does **not** use return values for the modes.

   **Do:** e.g. ``np.frombuffer(eigenvalues, ...)[:] = eigvals`` and ``np.frombuffer(eigenvectors, ...)[:] = eigvecs.T.flatten()``

   **Do not:** Return arrays only; results must be copied back into the buffers.


.. _eigenPythonSparseExample:

Example — SciPy ``eigsh``
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   import numpy as np
   import scipy.sparse as sp
   import scipy.sparse.linalg as sp_linalg
   import openseespy.opensees as ops

   class SciPyGeneralizedEigenSolver:
       def __init__(self, maxiter=None, tol=0.0):
           self.maxiter = maxiter
           self.tol = tol
           self._k_matrix = None
           self._m_matrix = None

       def solve(self, **kwargs):
           index_ptr = kwargs['index_ptr']
           indices = kwargs['indices']
           k_values = kwargs['k_values']
           m_values = kwargs['m_values']
           eigenvalues = kwargs['eigenvalues']
           eigenvectors = kwargs['eigenvectors']
           num_eqn = kwargs['num_eqn']
           nnz = kwargs['nnz']
           matrix_status = kwargs['matrix_status']
           num_modes = kwargs['num_modes']
           find_smallest = kwargs['find_smallest']

           indptr = np.frombuffer(index_ptr, dtype=np.int32, count=num_eqn + 1)
           idx = np.frombuffer(indices, dtype=np.int32, count=nnz)
           k_data = np.frombuffer(k_values, dtype=np.float64, count=nnz)
           m_data = np.frombuffer(m_values, dtype=np.float64, count=nnz)

           if matrix_status == 'STRUCTURE_CHANGED' or self._k_matrix is None:
               self._k_matrix = sp.csr_matrix((k_data, idx, indptr),
                                             shape=(num_eqn, num_eqn))
               self._m_matrix = sp.csr_matrix((m_data, idx, indptr),
                                             shape=(num_eqn, num_eqn))
           elif matrix_status == 'COEFFICIENTS_CHANGED':
               self._k_matrix.data[:] = k_data
               self._m_matrix.data[:] = m_data

           eigsh_kwargs = {
               'k': num_modes,
               'M': self._m_matrix,
               'which': 'LM',
           }
           if find_smallest:
               eigsh_kwargs['sigma'] = 0.0
           if self.maxiter is not None:
               eigsh_kwargs['maxiter'] = self.maxiter
           if self.tol > 0.0:
               eigsh_kwargs['tol'] = self.tol

           eigvals, eigvecs = sp_linalg.eigsh(self._k_matrix, **eigsh_kwargs)

           np.frombuffer(eigenvalues, dtype=np.float64,
                         count=num_modes)[:] = eigvals[:num_modes]
           np.frombuffer(eigenvectors, dtype=np.float64,
                         count=num_modes * num_eqn)[:] = eigvecs.T.flatten()

           return None

   solver = SciPyGeneralizedEigenSolver()
   eigenvalues = ops.eigen('PythonSparse', 10, {'solver': solver, 'scheme': 'CSR'})

.. seealso::

   * :ref:`systemPythonSparse` — PythonSparse linear system (``system('PythonSparse', ...)``)
   * `EXAMPLES/SolverBenchmark/benchmark_python_sparse_eigen.py <https://github.com/OpenSees/OpenSees/blob/master/EXAMPLES/SolverBenchmark/benchmark_python_sparse_eigen.py>`_