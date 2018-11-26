.. include:: sub.txt

.. _nonlinearBeamColumn-Element:
   
=====================
 nonlinearBeamColumn
=====================

.. function:: element('nonlinearBeamColumn',eleTag,iNode,jNode,numIntgrPts,secTag,transfTag,'-iter',maxIter=10,tol=1e-12,'-mass',mass=0.0,'-integration',intType)
   :noindex:

   Create a nonlinearBeamColumn element. This element is for backward compatability.

   ========================   =============================================================
   ``eleTag`` |int|           tag of the element
   ``iNode`` |int|            tag of node i
   ``jNode`` |int|            tag of node j
   ``numIntgrPts`` |int|      number of integration points.
   ``secTag`` |int|           tag of section
   ``transfTag`` |int|        tag of transformation
   ``maxIter`` |float|        maximum number of iterations to undertake to satisfy element compatibility (optional)
   ``tol`` |float|            tolerance for satisfaction of element compatibility (optional)
   ``mass`` |float|           element mass density (per unit length), from which a lumped-mass matrix is formed (optional)
   ``intType`` |str|          integration type (optional, default is ``'Lobatto'``)

                              * ``'Lobatto'``
			      * ``'Legendre'``
			      * ``'Radau'``
			      * ``'NewtonCotes'``
			      * ``'Trapezoidal'``
   ========================   =============================================================

