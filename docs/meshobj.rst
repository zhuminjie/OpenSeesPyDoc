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
     #. :attr:`mesh.numEleNodes`
     #. :attr:`mesh.inclDisp`
     #. :attr:`mesh.ndf`
     #. :attr:`mesh.eleType`
     #. :attr:`mesh.nds`
     #. :attr:`mesh.eles`
     #. :attr:`mesh.id`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`
     #. :meth:`mesh.clearEles`
     #. :meth:`mesh.clearNodes`
     #. :meth:`mesh.eleArgs`
     #. :meth:`mesh.mesh`


Following are available mesh subclasses in the OpenSees:

.. toctree::
   :maxdepth: 2

.. attribute:: mesh.meshsize

   An object attribute (get/set) |float|.
   The mesh size for the mesh object.
	       
   ::
   
      msh.meshsize = 0.001

.. attribute:: mesh.numEleNodes

   An object attribute (get) |int|.
   The number of nodes for elements to be meshed.
   By default, 2 is used for :meth:`mesh.line`,
   3 for :meth:`mesh.tri`, 6 for :meth:`mesh.PFEM`.
	       
   ::
   
      print(msh.numEleNodes)

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
   for example, the subclasses of the |element| class.
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

.. attribute:: mesh.id

   An object attribute (get/set) |int|.
   The id of the mesh. When :attr:`mesh.id` > 0,
   the mesh is considered as a structural mesh.
   When :attr:`mesh.id` < 0, it is considered as fluid mesh.
   When :attr:`mesh.id` = 0, it will not considered in FSI.
   The meshes with same :attr:`mesh.id` are
   considered as part of a same single structure.
   By default, it is ``1`` for :meth:`mesh.line` and :meth:`mesh.tri`
   and ``-1`` for :meth:`mesh.PFEM`.
	       
   ::
   
      mesh.id = -1;


.. method:: mesh.clearEles()

   Clear OpenSees elements in the mesh.

   ::

      msh.clearEles()

.. method:: mesh.clearNodes()

   Clear OpenSees nodes in the mesh.

   ::

      msh.clearNodes()


.. method:: mesh.eleArgs(*args, **kwargs)

   Set the element arguments for given :attr:`mesh.eleType`.

   .. note::

      The ``args`` and ``kwargs`` can be found in subclasses
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
#. :meth:`mesh.tri`
#. :meth:`mesh.PFEM`

.. classmethod:: mesh.line(nds)

   Create a line mesh object. The line mesh take 2 :class:`node` objects for each element.

   ========================   ======================================================================
   ``nds`` |list|             A list of :class:`node`, which define the line.
   ========================   ======================================================================


   ::

      line = mesh.line(nds=nds)
      line.eleType = element.Truss
      line.eleArgs(A=0.1, mat=mat)
      print(line)





.. classmethod:: mesh.tri(lines)

   Create a triangular mesh object. The line mesh take 3 :class:`node` objects for each element.

   ========================   ============================================================================
   ``lines`` |list|           A list of :meth:`mesh.line`, which define the area to be meshed.
   ========================   ============================================================================


   ::

      face = mesh.face(lines=lines)
      face.eleType = element.Tri31
      face.eleArgs(thick=1.0,type='PlaneStress',mat=mat)



.. classmethod:: mesh.PFEM(lines)
   
   Create a PFEM mesh object. A PFEM mesh take 6 :class:`node` objects for each
   :ref:`PFEM Elements <PFEM-Elements>`.

   ========================   ============================================================================
   ``lines`` |list|           A list of :meth:`mesh.line`, which define the area to be meshed.
   ========================   ============================================================================


   ::

      fluid = mesh.PFEM([line1,line2,line3,line4])
      fluid.meshsize = 0.01
      fluid.eleType = element.PFEMElement2DBubble
      fluid.eleArgs(rho=1000.0, mu=1e-3, b1=0.0, b2=-9.81)
      fluid.mesh()



