.. include:: sub.txt

.. _TriMesh:
   
=================
 triangular mesh
=================

.. function:: mesh('tri',tag,numlines,*ltags,id,ndf,meshsize,eleType='',*eleArgs=[])
   :noindex:

   Create a triangular mesh object.


   ========================   ===========================================================================
   ``tag`` |int|              mesh tag.
   ``numlines`` |int|         number of lines (:ref:`LineMesh`) for defining a polygon.
   ``ltags`` |listi|          the :ref:`LineMesh` tags
   ``id`` |int|               mesh id. Meshes with same id are considered as same structure
                              of fluid identity.

                              * ``id`` = 0 : reserved
			      * ``id`` > 0 : structure
			      * ``id`` < 0 : fluid
   ``ndf`` |int|              ndf for nodes to be created.
   ``meshsize`` |float|       mesh size.
   ``eleType`` |str|          the element type, (optional)

                              * ``'PFEMElement2DBubble'``
			      * ``'PFEMElement2DQuasi'``
			      * ``'tri31'``

			      if no type is given, only nodes are created
			      
   ``eleArgs`` |list|         a list of element arguments. (optional)
   ========================   ===========================================================================

