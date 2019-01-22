.. include:: sub.txt

=========================
 PFEMElementCompressible
=========================

.. function:: element('PFEMElementCompressible',eleTag,nd1,nd2,nd3,nd4,rho,mu,b1,b2,[thickness,kappa])
   :noindex:

   Create a PFEM compressible element, which is a fluid element for FSI analysis.

   ========================   =============================================================
   ``eleTag`` |int|           tag of the element
   ``nd1`` |int|              tag of node 1
   ``nd2`` |int|              tag of node 2
   ``nd3`` |int|              tag of node 3
   ``nd4`` |int|              tag of node 4 (middle node)
   ``rho`` |float|            fluid density
   ``mu`` |float|             fluid viscosity
   ``b1`` |float|             body body acceleration in x direction
   ``b2`` |float|             body body acceleration in y direction
   ``thickness`` |float|      element thickness (optional)
   ``kappa`` |float|          fluid bulk modulus (optional)
   ========================   =============================================================

