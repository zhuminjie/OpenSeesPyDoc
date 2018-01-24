.. include:: sub.txt

.. _TriMesh:
   
=================
 triangular mesh
=================

.. function:: mesh('tri',tag,ndf,meshsize,numlines,*ltags,'-remesh',eleType,*eleArgs)
   :noindex:

   Create a triangular mesh object.


   ========================   ===========================================================================
   ``tag`` |int|              mesh tag.
   ``ndf`` |int|              ndf for nodes to be created.
   ``meshsize`` |float|       mesh size.
   ``numlines`` |int|         number of lines (:ref:`LineMesh`) for defining a polygon.
   ``ltags`` |listi|          the :ref:`LineMesh` tags
   ``'-remesh'``              this mesh can be remeshed. (optional)
   ``eleType`` |str|          the element type, (optional)

                              * ``'PFEMElement2DBubble'``
			      * ``'PFEMElement2DQuasi'``
			      * ``'tri31'``

			      if no type is given, only nodes are created
			      
   ``eleArgs`` |list|         a list of element arguments. (optional)
   ========================   ===========================================================================

