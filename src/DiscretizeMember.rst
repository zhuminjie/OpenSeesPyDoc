.. include:: sub.txt

==========================
 DiscretizeMember command
==========================

.. function:: preprocessing.DiscretizeMember.DiscretizeMember(ndI, ndJ, numEle, eleType, integrTag, transfTag, nodeTag, eleTag)

   Create a OpenSees node.

   ========================   ===========================================================================
   ``ndI`` |int|              node tag at I end
   ``ndJ`` |int|              node tag at J end
   ``numEle`` |int|           number of element to discretize
   ``eleType`` |str|          the element type
   ``integrTag`` |int|        beam integration tag (:doc:`beamIntegration`)
   ``transfTag`` |int|        geometric transformation tag (:doc:`geomTransf`)
   ``nodeTag`` |int|          starting node tag
   ``eleTag`` |int|           starting element tag
   ========================   ===========================================================================



