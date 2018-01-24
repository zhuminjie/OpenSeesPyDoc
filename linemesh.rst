.. include:: sub.txt

.. _LineMesh:
   
===========
 line mesh
===========

.. function:: mesh('line',tag,id, ndf,meshsize,'-ele',eleTag,'-nodes',nd1,nd2)
   :noindex:

   Create a line mesh object.

   ========================   ===========================================================================
   ``tag`` |int|              mesh tag.
   ``id`` |int|               mesh id. Meshes with same id are considered as same structure
                              of fluid identity.

                              * ``id`` = 0 : not considered in FSI
			      * ``id`` > 0 : structure
			      * ``id`` < 0 : fluid
			      
   ``ndf`` |int|              ndf for nodes to be created.
   ``meshsize`` |float|       mesh size.
   ``eleTag`` |int|           the tag of the element defining the line. The element
                              will be replaced by the meshed line elements
			      with same element type and properties. 
   ``nd1`` |int|              End node 1, needed when no element is given.
   ``nd2`` |int|              End node 2, needed when no element is given.
   ========================   ===========================================================================

