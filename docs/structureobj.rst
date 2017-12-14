.. include:: sub.txt

Structure Object
=======================

.. class:: structure(meshes=[])

   The :class:`structure` object is a wrapper of ``Structure`` object in OpenSees
   for Fluid-Structure Interaction Simulation.
   A :class:`structure` is a single structure separated from other structures
   and may contain multiple :class:`mesh` objects. 
     
Object attributes
------------------------

#. :attr:`structure.tag`
#. :attr:`structure.meshes`

.. attribute:: structure.tag
      
   An object attribute (get) |int|.
   The tag of the structure.

   ::
   
      print(s.tag)

.. attribute:: structure.meshes

   An object attribute (get/set) |list|.
   Set or get the :class:`mesh` objects of the structure.
	       
   ::
   
      s.meshes = [msh1,msh2,msh3]


Object methods
---------------------

#. :meth:`structure.__str__`
#. :meth:`structure.remove`
#. :meth:`structure.add`

.. method:: structure.__str__()

   The string reprsentation of the :class:`structure`. Usually
   used in the |print| function.

   ::

      print(s)

.. method:: structure.remove(mesh=None)

   If no ``mesh`` is given,
   Remove the :class:`structure` object in the OpenSees.
   Otherwise, remove the :class:`mesh` object from the
   :class:`structure`.

   ::

      s.remove()

.. method:: structure.add(mesh)

   Add a :class:`mesh` object to the
   :class:`structure`.

   ::

      s.add(msh)
