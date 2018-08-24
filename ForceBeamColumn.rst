.. include:: sub.txt

.. _forceBeamColumn-Element:
   
=================
 forceBeamColumn
=================

.. function:: element('forceBeamColumn',eleTag,iNode,jNode,transfTag,integrationTag,'-iter',maxIter=10,tol=1e-12,'-mass',mass=0.0)
   :noindex:

   Create a ForceBeamColumn element.

   ========================   =============================================================
   ``eleTag`` |int|           tag of the element
   ``iNode`` |int|            tag of node i
   ``jNode`` |int|            tag of node j
   ``transfTag`` |int|        tag of transformation
   ``integrationTag`` |int|   tag of :func:`beamIntegration`
   ``maxIter`` |float|        maximum number of iterations to undertake to satisfy element compatibility (optional)
   ``tol`` |float|            tolerance for satisfaction of element compatibility (optional)
   ``mass`` |float|           element mass density (per unit length), from which a lumped-mass matrix is formed (optional)
   ========================   =============================================================

