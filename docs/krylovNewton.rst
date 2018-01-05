.. include:: sub.txt

krylovNewton 
======================================================

.. class:: krylovNewton(iterate='current',increment='current',maxDim=3)

   Create a KrylovNewton algorithm which uses a Krylov subspace accelerator to accelerate the convergence of the :class:`modifiedNewton`. A subclass of :class:`algorithm`.

   ================================   =============================================================
   ``iterate`` |str|                  Tangent to iterate on,
		                      ``'current'``, ``'initial'``, ``'noTangent'`` (optional)
   ``increment`` |str|                Tangent to increment on,
		                      ``'current'``, ``'initial'``, ``'noTangent'`` (optional)
   ``maxDim`` |int|                   Max number of iterations until
		                      the tangent is reformed and
                                      the acceleration restarts. (optional)
   ================================   =============================================================



