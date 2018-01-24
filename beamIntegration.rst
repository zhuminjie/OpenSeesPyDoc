.. include:: sub.txt

=========================
 beamIntegration command
=========================

.. function:: beamIntegration(type, tag, *args)

   A wide range of numerical integration options are available in OpenSees to represent distributed plasticity or non-prismatic section details in Beam-Column Elements, i.e., across the entire element domain [0, L].


Following are beamIntegration types available in the OpenSees:

Integration Methods for Distributed Plasticity.
Distributed plasticity methods permit yielding at any integration point along the element
length.


.. toctree::
   :maxdepth: 2

   Lobatto
   Legendre
   NewtonCotes
   Radau
   Trapezoidal
   CompositeSimpson
   userDefined
   FixedLocation
   LowOrder
   MidDistance



Plastic Hinge Integration Methods. Plastic hinge integration methods confine material yielding to regions of the element of  specified length while the remainder of the element is linear elastic. A summary of plastic hinge integration methods is found in (`Scott and Fenves 2006`_).

.. toctree::
   :maxdepth: 2

   UserHinge
   HingeMidpoint
   HingeRadau
   HingeRadauTwo
   HingeEndpoint






