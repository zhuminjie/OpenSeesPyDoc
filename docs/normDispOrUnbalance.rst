.. include:: sub.txt

===========================================================
 normDispOrUnbalance 
===========================================================

.. class:: normDispOrUnbalance(tolIncr,tolR,iter,pFlag=0,nType=2,maxincr=-1)

   Create a NormDispOrUnbalance test, which check if both
   :class:`normUnbalance` and :class:`normDispIncr` are converged. A subclass of :class:`test`.

   ======================   =============================================================
   ``tolIncr`` |float|      Tolerance for left hand solution increments
   ``tolIncr`` |float|      Tolerance for right hand residual
   ``iter`` |int|           Max number of iterations to check
   ``pFlag`` |int|          See :class:`normUnbalance` (optional)		    
   ``nType`` |int|          See :class:`normUnbalance` (optional)
   ``maxincr`` |int|        See :class:`normUnbalance` (optional)
   ======================   =============================================================

::

   normDispOrUnbalance(tolIncr=1.0e-8, tolR=1.0e-6, iter=10)



