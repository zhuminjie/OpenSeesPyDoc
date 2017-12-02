.. include:: sub.txt

Mesh Object
==============

.. class:: mesh(bgsize=0.0, bgtol=0.0)

   Create a python :class:`mesh` object which is
   for creating moving mesh and background mesh in the OpenSees.
   All regular FE mesh are considered as moving mesh.
   The backgroundm mesh is useful for Fluid-Structure Interaction.

   ========================   ===============================================================
   ``bgsize`` |float|         Mesh size for background mesh. (optional)
   ``bgtol`` |float|          Boundary tolerance for background mesh. (optional)
   ========================   ===============================================================

   .. note::

      If ``bgsize`` is given  then a background mesh is created.
      Otherwise, a moving mesh is created.

   ::

      # a moving mesh
      msh = mesh()

      # a background mesh
      msh = mesh(bgsize = 0.01)
     
Object attributes
------------------------

#. :attr:`mesh.tag`
#. :attr:`mesh.moving`
#. :attr:`mesh.eleType`

.. attribute:: mesh.tag
      
   An object attribute (get) |int|.
   The tag of the mesh.

   ::
   
      print(msh.tag)

.. attribute:: mesh.moving

   An object attribute (get) |bool|.
   Indicate if the mesh is a moving mesh or a background mesh.
	       
   ::
   
      if msh.moving:
          print('This is a moving mesh')


.. attribute:: mesh.eleType

   An object attribute (get/set) |callable|.
   A python callable object which will create the element with given :meth:`mesh.eleArgs`.
   For example, the :ref:`element-class-methods` of the |element| class.
   The ``eleType`` must be set before doing any meshing.
	       
   ::
   
      msh.eleType = element.Truss

Object methods
---------------------

#. :meth:`mesh.__str__`
#. :meth:`mesh.remove`
#. :meth:`mesh.eleArgs`
#. :meth:`mesh.line`

.. method:: mesh.__str__()

   The string reprsentation of the :class:`mesh`. Usually
   used in the |print| function.

   ::

      print(m)

.. method:: mesh.remove()

   Remove the mesh in the OpenSees.

   ::

      msh.remove()


.. method:: mesh.eleArgs(*args, **kwargs)

   Set the element arguments for given :attr:`mesh.eleType`.

   .. note::

      The ``args`` and ``kwargs`` can be found in :ref:`element-class-methods`
      of the |element| class
      but without the ``nds``, which will be automatically
      added.

   ::

      msh.eleArgs(A=0.1, mat=mat)

.. method:: mesh.line(meshsize, nds)

   Mesh lines elements between ``nds`` with the ``meshsize``.

   ========================   ======================================================================
   ``meshsize`` |float|       The mesh size, i.e. the length of each meshed line element.
   ``nds`` |list|             A list of two nodes, which are the ends of the line.
   ========================   ======================================================================


   ::

      msh = mesh()
      msh.eleType = element.Truss
      msh.eleArgs(A=0.1, mat=mat)
      nds = [node([0.0,0.0]), node([1.0,0.0])
      eles = msh.line(meshsize=0.01, nds=nds)
