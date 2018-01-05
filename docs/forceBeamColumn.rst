.. include:: sub.txt

================================================
 forceBeamColumn
================================================

.. class:: forceBeamColumn(nds,transf,bi,mass=0.0,tol=1e-12,maxIter=10)

   Create a forceBeamColumn :class:`element` object. A subclass of :class:`element`.

   ========================   =============================================================
   ``nds`` |list|             Two end :class:`node` objects.
   ``transf`` |transf|        Previously-defined |transf| object.
   ``bi`` |bi|                Previously-defined |bi| object.
   ``mass`` |float|           Element mass per unit length, from which a lumped-mass matrix is formed  (optional)
   ``tol`` |float|            Tolerance for satisfaction of element compatibility (optional)
   ``maxIter`` |int|          maximum number of iterations to undertake to satisfy element compatibility (optional)
   ========================   =============================================================


.. class:: forceBeamColumn(ele)

   Convert an :class:`element` to :class:`forceBeamColumn`.

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
     #. :attr:`forceBeamColumn.force`
     #. :attr:`forceBeamColumn.localForce`
     #. :attr:`forceBeamColumn.basicForce`
     #. :attr:`forceBeamColumn.basicStiff`
     #. :attr:`forceBeamColumn.chordRotation`
     #. :attr:`forceBeamColumn.plasticRotation`
     #. :attr:`forceBeamColumn.inflectionPoint`
     #. :attr:`forceBeamColumn.tangentDrift`
     #. :attr:`forceBeamColumn.dvpdh`
     #. :attr:`forceBeamColumn.dqdh`
     #. :attr:`forceBeamColumn.integrationPoints`
     #. :attr:`forceBeamColumn.integrationWeights`
     #. :attr:`forceBeamColumn.rayleighForces`
     #. :attr:`forceBeamColumn.secs`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`



.. attribute:: forceBeamColumn.force

   An object attribute (get) |listf|.
   The global force of forceBeamColumn.

.. attribute:: forceBeamColumn.localForce

   An object attribute (get) |listf|.
   The force force of forceBeamColumn.

.. attribute:: forceBeamColumn.basicForce

   An object attribute (get) |listf|.
   The basic force of forceBeamColumn.


.. attribute:: forceBeamColumn.basicStiff

   An object attribute (get) |listf|.
   The basic stiffness of forceBeamColumn.


.. attribute:: forceBeamColumn.chordRotation

   An object attribute (get) |listf|.
   The chord rotation of the element.


.. attribute:: forceBeamColumn.plasticRotation

   An object attribute (get) |listf|.
   The plastic rotation of the element.

.. attribute:: forceBeamColumn.inflectionPoint

   An object attribute (get) |listf|.
   The inflection point of the element.

.. attribute:: forceBeamColumn.tangentDrift

   An object attribute (get) |listf|.
   The tangent drift of the element.

.. attribute:: forceBeamColumn.dvpdh

   An object attribute (get) |listf|.
   The plastic deformation sensitivity of the element.

.. attribute:: forceBeamColumn.dqdh

   An object attribute (get) |listf|.
   The basic force sensitivity of the element.

.. attribute:: forceBeamColumn.integrationPoints

   An object attribute (get) |listf|.
   The integration points of the element.

.. attribute:: forceBeamColumn.integrationWeights

   An object attribute (get) |listf|.
   The integration weights of the element.

.. attribute:: forceBeamColumn.rayleighForces

   An object attribute (get) |listf|.
   The rayleigh forces of the element.

.. attribute:: forceBeamColumn.secs

   An object attribute (get) |list|.
   The sections of the element, which can be used to get section responses.

