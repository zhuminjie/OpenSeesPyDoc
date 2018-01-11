.. include:: sub.txt

=================================
 element  class
=================================

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
     #. :attr:`element.force`
     #. :attr:`element.dampingForce`
     #. :attr:`element.dynamicForce`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`
     #. :meth:`element.section`
     #. :meth:`element.uniMat`
     #. :meth:`element.nDMat`

   

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


.. attribute:: element.ndf

   An object attribute (get) |int|.
   The element number of dofs.


.. attribute:: element.stiff

   An object attribute (get) |listl|.
   The element stiffness matrix.


.. attribute:: element.damp

   An object attribute (get) |listl|.
   The element damping matrix.


.. attribute:: element.mass

   An object attribute (get) |listl|.
   The element mass matrix.


.. attribute:: element.force

   An object attribute (get) |listl|.
   The resisting force.



.. attribute:: element.dampingForce

   An object attribute (get) |listl|.
   The damping force.


.. attribute:: element.dynamicForce

   An object attribute (get) |listl|.
   The dynamic resisting force.


.. method:: element.section(num)

   Return the ``num`` th |section| in the element.
   If no such section, return |none|.

   ========================   ====================================================================
   ``num`` |int|              The section number in element, start from ``1``.
   ========================   ====================================================================

.. method:: element.uniMat(num)

   Return the ``num`` th |unimat| in the element.
   If no such section, return |none|.

   ========================   ====================================================================
   ``num`` |int|              The material number in element, start from ``1``.
   ========================   ====================================================================


.. method:: element.nDMat(num)

   Return the ``num`` th |ndmat| in the element.
   If no such section, return |none|.

   ========================   ====================================================================
   ``num`` |int|              The material number in element, start from ``1``.
   ========================   ====================================================================


