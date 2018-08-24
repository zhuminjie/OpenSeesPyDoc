.. include:: sub.txt

.. _dispBeamColumn-Element:
   
=================
 dispBeamColumn
=================

.. function:: element('dispBeamColumn',eleTag,iNode,jNode,transfTag,integrationTag,'-cMass','-mass',mass=0.0)
   :noindex:

   Create a ForceBeamColumn element.

   ========================   =============================================================
   ``eleTag`` |int|           tag of the element
   ``iNode`` |int|            tag of node i
   ``jNode`` |int|            tag of node j
   ``transfTag`` |int|        tag of transformation
   ``integrationTag`` |int|   tag of :func:`beamIntegration`
   ``'-cMass'``               to form consistent mass matrix (optional, default = lumped mass matrix)
   ``mass`` |float|           element mass density (per unit length), from which a lumped-mass matrix is formed (optional)
   ========================   =============================================================

