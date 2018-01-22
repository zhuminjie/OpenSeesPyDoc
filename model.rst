.. include:: sub.txt

============
 model func
============

.. function:: model('basic', '-ndm',ndm,'-ndf',ndf)

   Create a basic OpenSees model.

   ========================   ===========================================================================
   ``ndm`` |int|              spatial dimension of problem (1,2, or 3)
   ``ndf`` |int|              number of degrees of freedom at node (optional)
	      
                              default value depends on value of ndm:
   
			      * ndm=1 -> ndf=1
                              * ndm=2 -> ndf=3
                              * ndm=3 -> ndf=6

   ========================   ===========================================================================

