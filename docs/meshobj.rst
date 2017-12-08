.. include:: sub.txt

Mesh Object
==============

.. class:: mesh()

   The :class:`mesh` object is for creating and updating moving and background mesh
   in OpenSees. Use :ref:`mesh-class-methods` below to create meshes.
     
Object attributes
------------------------

#. :attr:`mesh.tag`
#. :attr:`mesh.meshsize`
#. :attr:`mesh.numEleNodes`
#. :attr:`mesh.inclDisp`
#. :attr:`mesh.ndf`
#. :attr:`mesh.eleType`
#. :attr:`mesh.nds`
#. :attr:`mesh.eles`

.. attribute:: mesh.tag
      
   An object attribute (get) |int|.
   The tag of the mesh.

   ::
   
      print(msh.tag)

.. attribute:: mesh.meshsize

   An object attribute (get/set) |float|.
   The mesh size for the mesh object.
	       
   ::
   
      msh.meshsize = 0.001

.. attribute:: mesh.numEleNodes

   An object attribute (get/set) |int|.
   The number of nodes for elements to be meshed.
   If not set, 2 is used for line mesh, 3 for face mesh, and 4 for volume mesh.
	       
   ::
   
      msh.numEleNodes = 2

.. attribute:: mesh.inclDisp

   An object attribute (get/set) |int|.
   When it is ``1`` (default), it will add displacement
   to nodal coordinates when meshing.
	       
   ::
   
      msh.inclDisp = 0

.. attribute:: mesh.ndf

   An object attribute (get/set) |int|.
   The :attr:`node.ndf` for |node| objects to be meshed.
   If not set, :attr:`model.ndf` is used.
	       
   ::
   
      msh.ndf = 3

.. attribute:: mesh.eleType

   An object attribute (get/set) |callable|.
   A python callable object which will create the element with given :meth:`mesh.eleArgs`,
   for example, the :ref:`element-class-methods` of the |element| class.
   If not set, no elements will be meshed, but nodes will.
	       
   ::
   
      msh.eleType = element.Truss


.. attribute:: mesh.nds

   An object attribute (get) |list|.
   The list of |node| objects in the mesh.
	       
   ::
   
      nds = msh.nds

.. attribute:: mesh.eles

   An object attribute (get) |list|.
   The list of |element| objects in the mesh.
	       
   ::
   
      eles = msh.eles

Object methods
---------------------

#. :meth:`mesh.__str__`
#. :meth:`mesh.remove`
#. :meth:`mesh.clear`
#. :meth:`mesh.eleArgs`
#. :meth:`mesh.mesh`

.. method:: mesh.__str__()

   The string reprsentation of the :class:`mesh`. Usually
   used in the |print| function.

   ::

      print(m)

.. method:: mesh.remove()

   Remove the mesh in the OpenSees.

   ::

      msh.remove()

.. method:: mesh.clear()

   Clear the mesh by removing OpenSees nodes and elements.

   ::

      msh.clear()


.. method:: mesh.eleArgs(*args, **kwargs)

   Set the element arguments for given :attr:`mesh.eleType`.

   .. note::

      The ``args`` and ``kwargs`` can be found in :ref:`element-class-methods`
      of the |element| class
      but without the ``nds``, which will be automatically
      added.

   ::

      msh.eleArgs(A=0.1, mat=mat)


.. classmethod:: mesh.mesh()

   Do the mesh. A face mesh will mesh its lines first. A volume mesh
   will mesh its faces first.

   ::

      line.mesh()



.. _mesh-class-methods:


Class methods
---------------

#. :meth:`mesh.line`
#. :meth:`mesh.face`
#. :meth:`mesh.volume`


.. classmethod:: mesh.line(nds)

   Create a line mesh object.

   ========================   ======================================================================
   ``nds`` |list|             A list of :class:`node`, which define the line.
   ========================   ======================================================================


   ::

      line = mesh.line(nds=nds)
      line.eleType = element.Truss
      line.eleArgs(A=0.1, mat=mat)
      print(line)





.. classmethod:: mesh.face(lines)

   Create a face mesh object.

   ========================   ============================================================================
   ``lines`` |list|           A list of :meth:`mesh.line`, which define the face.
   ========================   ============================================================================


   ::

      face = mesh.face(lines=lines)
      face.eleType = element.Tri31
      face.eleArgs(thick=1.0,type='PlaneStress',mat=mat)



.. classmethod:: mesh.volume(faces)

   Create a volume mesh object.

   ========================   ================================================================================
   ``faces`` |list|           A list of :meth:`mesh.face`, which define the volme.
   ========================   ================================================================================


   ::

      vol = mesh.volume(faces=faces)




