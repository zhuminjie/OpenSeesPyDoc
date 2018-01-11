.. include:: sub.txt

==========================================
 pfemTest  class
==========================================

.. class:: pfemTest(tolv,tolp,tolrv,tolrp,iter,maxincr,tolrelv=1e-15,tolrelp=1e-15,pFlag=0,nType=2)

   Create a PFEM test, which check both increments and residual for
   velocities and pressures. A subclass of :class:`test`.

   ======================   =========================================================================
   ``tolv`` |float|         Tolerance for velocity increments
   ``tolp`` |float|         Tolerance for pressure increments
   ``tolrv`` |float|        Tolerance for velocity residual
   ``tolrp`` |float|        Tolerance for pressure residual
   ``maxincr`` |int|        Max times for error increasing
   ``iter`` |int|           Max number of iterations to check
   ``tolrv`` |float|        Tolerance for relative velocity increments (optional)
   ``tolrp`` |float|        Tolerance for relative pressure increments (optional)
   ``pFlag`` |int|          See :class:`normUnbalance` (optional)		    
   ``nType`` |int|          See :class:`normUnbalance` (optional)
   ======================   =========================================================================

   ::

      pfemTest(tolv=1e-6, tolp=1e-6, tolrv=1e-6, tolrp=1e-6, iter=20, maxincr=3, pFlag=1)




