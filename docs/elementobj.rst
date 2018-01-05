.. include:: sub.txt

===========================
 element -- Finite Element
===========================

.. class:: element()

   A subclass of :class:`tagged` and
   a base class for the OpenSees Element objects.

   One cannot create an :class:`element` object
   directly, but only through its subclasses.


   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`element.nds`
     #. :attr:`element.ndf`
     #. :attr:`element.stiff`
     #. :attr:`element.damp`
     #. :attr:`element.mass`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`

   

Following are element subclasses available in the OpenSees:

Zero-Length Elements

.. toctree::
   :maxdepth: 2

   zeroLengthSection

Truss Elements

.. toctree::
   :maxdepth: 2

   truss

.. _Beam-Column-Elements:
  
Beam-Column Elements

.. toctree::
   :maxdepth: 2

   elasticBeamColumn
   forceBeamColumn
   dispBeamColumn

Triangular Elements

.. toctree::
   :maxdepth: 2

   tri31


.. _PFEM-Elements:
  
PFEM Elements

.. toctree::
   :maxdepth: 2

   bubble2d





	      

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
