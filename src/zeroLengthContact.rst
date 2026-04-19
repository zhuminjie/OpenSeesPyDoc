.. include:: sub.txt

===========================
 zeroLengthContact elements
===========================

Node-to-node frictional contact (**2D** or **3D**): constrained node vs retained node. Mohr–Coulomb: :math:`T = \mu N + c` (:math:`T` tangential, :math:`N` normal, :math:`\mu` friction, :math:`c` cohesion).

**2D**

.. function:: element('zeroLengthContact2D', eleTag, cNode, rNode, Kn, Kt, mu, '-normal', Nx, Ny)

**3D**

.. function:: element('zeroLengthContact3D', eleTag, cNode, rNode, Kn, Kt, mu, c, dir)

   ================================   ===========================================================================
   ``eleTag`` |int|                  element tag
   ``cNode``, ``rNode`` |int|       constrained and retained node tags
   ``Kn``, ``Kt`` |float|            penalty stiffness (normal, tangential)
   ``mu`` |float|                   friction coefficient
   ``Nx``, ``Ny`` |float|           (2D) unit normal components
   ``c`` |float|                    (3D) cohesion (not used in 2D)
   ``dir`` |int|                    (3D) out-normal of retained plane: 1 = +X, 2 = +Y, 3 = +Z
   ================================   ===========================================================================

.. note::

   #. Element tangent is non-symmetric; use a non-symmetric linear system solver.
   #. 2D contact: nodes with 2 DOF; 3D contact: nodes with 3 DOF.
   #. Out-normal of the master (retained) plane is taken fixed during analysis.

.. seealso::

   `Notes (OpenSees wiki) <http://opensees.berkeley.edu/wiki/index.php/ZeroLengthContact_Element>`_

.. admonition:: Example

   **2D:** contact between nodes **2** and **4**, normal ``(0, -1)``.

   .. code-block:: python

      import openseespy.opensees as ops

      ops.element('zeroLengthContact2D', 1, 2, 4, 1e8, 1e8, 0.3, '-normal', 0, -1)

   **3D:** cohesion ``0``, out-normal **+Z** (``dir`` = 3).

   .. code-block:: python

      ops.element('zeroLengthContact3D', 1, 2, 4, 1e8, 1e8, 0.3, 0.0, 3)

Code developed by: **Gang Wang**, Geomatrix
