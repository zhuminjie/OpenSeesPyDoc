.. include:: sub.txt

======================================
 sparseSYM -- Sparse Symmetric solver
======================================

.. class:: sparseSYM(lSparse=1)

   Create a SparseSYM system for sparse symmetric 
   matrix which uses a row-oriented solution method in the solution phase.
   A subclass of :class:`system`.

   =====================   ======================
   ``lSparse`` |int|       Ordering scheme:

                           #. -- MMD
			   #. -- ND
			   #. -- RCM
   =====================   ======================
