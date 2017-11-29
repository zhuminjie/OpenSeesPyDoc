.. include:: sub.txt

Element Object
=======================

.. class:: element()

   A python :class:`element` object
   is a wrapper to the OpenSees ``Element`` object.

   .. note::
   
      One cannot create an :class:`element` object
      directly, but only through :ref:`element-class-methods`.


Object attributes
-------------------

.. attribute:: element.tag
      
   An object attribute (get) |int|.
   The :class:`element` tag.

   ::

      print(ele.tag)

.. attribute:: element.nds

   An object attribute (get) |list|.
   The element :class:`node` objects.

   ::

      print(ele.nds)

.. attribute:: element.ndf

   An object attribute (get) |int|.
   The element number of dofs.

   ::

      print(ele.ndf)

.. attribute:: element.stiff

   An object attribute (get) |listl|.
   The element stiffness matrix.

   ::

      print(ele.stiff)

.. attribute:: element.damp

   An object attribute (get) |listl|.
   The element damping matrix.

   ::

      print(ele.damp)

.. attribute:: element.mass

   An object attribute (get) |listl|.
   The element mass matrix.

   ::

      print(ele.mass)

Object methods
---------------

#. :meth:`element.__str__`
#. :meth:`element.remove`

.. method:: element.__str__()

   The string reprsentation of the :class:`element`. Usually
   used in the |print| function.

   ::

      print(ele)

.. method:: element.remove()

   Remove the corresponding OpenSees ``Element`` object.
	       
   .. seealso::

      :meth:`node.remove`

   ::

      ele.remove()

.. _element-class-methods:

Class methods
---------------

#. :meth:`element.Truss`

.. classmethod:: element.Truss(nds, A, mat, rho=0.0, cMass=0,doRayleigh=0)

   Create a Truss :class:`element` object.

   ========================   =============================================================
   ``nds`` |list|             Truss end :class:`node` objects.
   ``A`` |float|              Cross-sectional area of element.
   ``mat`` |unimat|           A |unimat| object.
   ``rho`` |float|            Mass per unit length. (optional)
   ``cMass`` |int|            Consistent mass flag (0 lumped mass, 1 consistent mass).
		              (optional)
   ``doRayleigh`` |int|       Rayleigh damping flag (0 no rayleigh damping,
		              1 include rayleigh damping). (optional)
   ========================   =============================================================


   ::

      # create a truss element
      ele = element.Truss(nds=[nds[1],nds[4]], A=A, mat=mat)
   
      # create 100 truss elements
      eles = [element.Truss(nds=[nds[i],nds[i+1]], A=A, mat=mat) for i in range(100)] 
