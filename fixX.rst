.. include:: sub.txt

===========
 fixX func
===========

.. function:: fixX(x, *fixValues, '-tol', tol=1e-10)

   Create SP constraints.

   ========================   ===========================================================================
   ``x`` |float|              x-coordinates of nodes to be constrained
   ``fixValues`` |listi|      fix values
	      
	                      * 0 free
	                      * 1 fixed
   ``tol`` |float|            tolerance
   ========================   ===========================================================================

