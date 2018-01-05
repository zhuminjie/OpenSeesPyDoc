.. include:: sub.txt

=================================
 egen 
=================================

.. class:: egen(sSolver, pSolver=sSolver)

   Create a Egen system for both structural analysis and
   Fluid-Structure Interaction using `Eigen`_. A subclass of :class:`system`.

   =====================   ================================================================
   ``sSolver`` |str|       Structural solver:
		           ``'LLT'``, ``'LDLT'``, ``'LU'``, ``'QR'``, ``'CG'``, ``'PCG'``,
		           ``'LSCG'``, ``'BiCG'``, ``'PBiCG'``
   ``pSolver`` |str|       Pressure solver (optional)
   =====================   ================================================================




