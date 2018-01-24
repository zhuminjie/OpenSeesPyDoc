.. include:: sub.txt

.. _LineMesh:
   
===========
 line mesh
===========

.. function:: mesh('line',tag,ndf,meshsize,numnodes,*ndtags,'-remesh',eleType,*eleArgs)
   :noindex:

   Create a line mesh object.


   ========================   ===========================================================================
   ``tag`` |int|              mesh tag.
   ``ndf`` |int|              ndf for nodes to be created.
   ``meshsize`` |float|       mesh size.
   ``numnodes`` |int|         number of end nodes for lines.
   ``ndtags`` |listi|         the node tags
   ``'-remesh'``              this mesh can be remeshed. (optional)
   ``eleType`` |str|          the element type, (optional)

                              * ``'elasticBeamColumn'``
			      * ``'forceBeamColumn'``
			      * ``'dispBeamColumn'``

			      if no type is given, only nodes are created
			      
   ``eleArgs`` |list|         a list of element arguments. (optional)
   ========================   ===========================================================================

