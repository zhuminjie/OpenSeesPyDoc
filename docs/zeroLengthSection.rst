.. include:: sub.txt

================================================
 zeroLengthSection
================================================

.. class:: zeroLengthSection(nds, sec, x=[1.0,0.0,0.0], yp=[0.0,1.0,0.0], doRayleigh=1)

   Create a zeroLengthSection :class:`element` object, which is defined by two |node| objects at the same location. The nodes are connected by a single |section| object to represent the force-deformation relationship for the element. A subclass of :class:`element`.

   ========================   =============================================================
   ``nds`` |list|             Two end :class:`node` objects.
   ``sec`` |section|          A |section| object.
   ``x`` |listf|              Vector components in global coordinates defining
		              local x-axis. (optional)
   ``yp`` |listf|             Vector components in global coordinates defining
		              vector yp which lies in the local x-y plane for
                              the element. (optional)
   ``doRayleigh`` |int|       Rayleigh damping flag (0 no rayleigh damping,
		              1 include rayleigh damping). (optional)
   ========================   =============================================================


.. class:: zeroLengthSection(ele)

   Convert an :class:`element` to :class:`zeroLengthSection`.

   ========================   =============================================================
   ``ele`` |element|          A :class:`element` object.
   ========================   =============================================================


   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`element.nds`
     #. :attr:`element.ndf`
     #. :attr:`element.stiff`
     #. :attr:`element.damp`
     #. :attr:`element.mass`
     #. :attr:`zeroLengthSection.force`
     #. :attr:`zeroLengthSection.localForce`
     #. :attr:`zeroLengthSection.deformation`
     #. :attr:`zeroLengthSection.sec`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`



.. attribute:: zeroLengthSection.force

   An object attribute (get) |listf|.
   The global force of zeroLengthSection.

.. attribute:: zeroLengthSection.localForce

   An object attribute (get) |listf|.
   The local force of zeroLengthSection.


.. attribute:: zeroLengthSection.deformation

   An object attribute (get) |listf|.
   The deformation of zeroLengthSection.


.. attribute:: zeroLengthSection.sec

   An object attribute (get) |section|.
   The :class:`section` of zeroLengthSection, which can be used
   to get the section responses.



