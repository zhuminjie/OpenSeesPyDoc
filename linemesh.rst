.. include:: sub.txt

.. _LineMesh:
   
===========
 line mesh
===========

.. function:: mesh('line',tag,nd1,nd2,id,ndf,meshsize,eleType='',*eleArgs=[])
   :noindex:

   Create a line mesh object. 

   ========================   ===========================================================================
   ``tag`` |int|              mesh tag.
   ``nd1`` |int|              line end node 1
   ``nd2`` |int|              line end node 2
   ``id`` |int|               mesh id. Meshes with same id are considered as same structure
                              of fluid identity.

                              * ``id`` = 0 : not considered in FSI
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

