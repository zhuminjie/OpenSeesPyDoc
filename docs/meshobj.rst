.. include:: sub.txt

==================================
 mesh 
==================================

.. class:: mesh()

   A subclass of :class:`tagged`.
   The :class:`mesh` object is for creating and updating mesh
   in OpenSees. Use subclasses to create meshes.

   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`mesh.meshsize`
     #. :attr:`mesh.inclDisp`
     #. :attr:`mesh.ndf`
     #. :attr:`mesh.ele`
     #. :attr:`mesh.nds`
     #. :attr:`mesh.eles`
     #. :attr:`mesh.id`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`
     #. :meth:`mesh.clearEles`
     #. :meth:`mesh.clearNodes`
     #. :meth:`mesh.make`


Following are available mesh subclasses in the OpenSees:

.. toctree::
   :maxdepth: 2

   line
	      
.. attribute:: mesh.meshsize

   An object attribute (get/set) |float|.
   The mesh size for the mesh object.

.. attribute:: mesh.inclDisp

   An object attribute (get/set) |bool|.
   When it is ``True``, it will add displacement
   to nodal coordinates when meshing.
	       
.. attribute:: mesh.ndf

   An object attribute (get/set) |int|.
   The :attr:`node.ndf` for |node| objects to be meshed.
   If not set, :attr:`model.ndf` is used.
	       
.. attribute:: mesh.ele

   An object attribute (get/set) |element|.
   The mesh will generate same type of elements.
   Once the element is given to mesh, it will be removed from model.
   If not set, only nodes will be generated.
	       
.. attribute:: mesh.nds

   An object attribute (get) |list|.
   The list of |node| objects generated in the mesh.
	       
.. attribute:: mesh.eles

   An object attribute (get) |list|.
   The list of |element| objects generated in the mesh.
	       
.. attribute:: mesh.id

   An object attribute (get/set) |int|.
   The id of the mesh. When :attr:`mesh.id` > 0,
   the mesh is considered as a structural mesh.
   When :attr:`mesh.id` < 0, it is considered as fluid mesh.
   When :attr:`mesh.id` = 0, it will not considered in FSI.
   The meshes with same :attr:`mesh.id` are
   considered as part of a same single structure.
   By default, it is ``0``.


.. method:: mesh.clearEles()

   Clear elements in the mesh.


.. method:: mesh.clearNodes()

   Clear nodes in the mesh.


.. classmethod:: mesh.make()

   Make all meshes. This is a class method.

