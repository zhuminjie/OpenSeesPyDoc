.. include:: sub.txt

.. _LineMesh:
   
===========
 line mesh
===========

.. function:: mesh('line',tag,numnodes,*ndtags,id,ndf,meshsize,eleType='',*eleArgs=[])
   :noindex:

   Create a line mesh object. 

   ========================   ===========================================================================
   ``tag`` |int|              mesh tag.
   ``numnodes`` |int|         number of nodes for defining consective lines.
   ``ndtags`` |listi|         the node tags
   ``id`` |int|               mesh id. Meshes with same id are considered as same structure
                              of fluid identity.

                              * ``id`` = 0 : background
			      * ``id`` > 0 : structure
			      * ``id`` < 0 : fluid
   ``ndf`` |int|              ndf for nodes to be created.
   ``meshsize`` |float|       mesh size.
   ``eleType`` |str|          the type of the element, (optional)

                              * ``'elasticBeamColumn'``
                              * ``'forceBeamColumn'``
                              * ``'dispBeamColumn'``

			      if no type is given, only nodes are created
   ``eleArgs`` |list|         a list of element arguments. (optional)
   ========================   ===========================================================================

