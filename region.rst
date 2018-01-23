.. include:: sub.txt

=============
 region func
=============

.. function:: region(regTag,'-ele',*eles,'-eleOnly',*eles,'-eleRange',startEle,endEle,'-eleOnlyRange',startEle,endEle,'-node',*nds,'-nodeOnly',*nds,'-nodeRange',startNode,endNode,'-nodeOnlyRange',startNode,endNode,'-rayleigh',alphaM,betaK,betaKinit,betaKcomm,'getNodeTags','getEleTags')

   Create a mesh region

   ========================   ===========================================================================
   ``regTag`` |int|           region tag.
   ``eles`` |listi|           a list of element tags
   ``startEle`` |int|         start element tag
   ``endEle`` |int|           end element tag
   ``nds`` |listi|            a list of node tags
   ``startNode`` |int|        start node tag
   ``endNode`` |int|          end node tag
   ``alphaM`` |float|         :func:`rayleigh` damping parameter
   ``betaK`` |float|          :func:`rayleigh` damping parameter
   ``betaKinit`` |float|      :func:`rayleigh` damping parameter
   ``betaKcomm`` |float|      :func:`rayleigh` damping parameter
   ``'getNodeTags'``          return node tags in the region
   ``'getEleTags'``           return element tags in the region
   ========================   ===========================================================================

