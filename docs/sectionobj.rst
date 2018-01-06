.. include:: sub.txt

===========================================
 section 
===========================================

.. class:: section()

   A subclass of :class:`tagged`
   and a base class of the OpenSees Section objects.

   One cannot create an :class:`section` object
   directly, but only through its subclasses.


   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`section.deformation`
     #. :attr:`section.stress`
     #. :attr:`section.stiff`
     #. :attr:`section.flexibility`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`
     #. :meth:`section.uniMat`
     #. :meth:`section.nDMat`


Following are available section subclasses in the OpenSees:

.. toctree::
   :maxdepth: 2

   elasticSection
   fiberSection
   ndfiberSection
   biaxialHysteretic

.. attribute:: section.deformation
      
   An object attribute (get/set) |listf|.
   The section deformation.

   ::

      sec.deformation = [0.01,0.01]

.. attribute:: section.stress

   An object attribute (get) |listf|.
   The section stress.

   ::

      print(sec.stress)

.. attribute:: section.stiff

   An object attribute (get) |listl|.
   The section stiffness.

   ::

      print(sec.tangent)

.. attribute:: section.flexibility

   An object attribute (get) |listl|.
   The section flexibility.

.. method:: section.uniMat(num)

   Return the ``num`` th |unimat| in the section.
   If no such material, return |none|.

   ========================   ====================================================================
   ``num`` |int|              The material number in element, start from ``1``.
   ========================   ====================================================================


.. method:: section.nDMat(num)

   Return the ``num`` th |ndmat| in the section.
   If no such material, return |none|.

   ========================   ====================================================================
   ``num`` |int|              The material number in element, start from ``1``.
   ========================   ====================================================================

