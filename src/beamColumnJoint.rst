.. include:: sub.txt

=======================
BeamColumnJoint Element
=======================

This command is used to construct a two-dimensional beam-column-joint element object. The element may be used with both two-dimensional and three-dimensional structures; however, load is transferred only in the plane of the element.



.. function:: element('beamColumnJoint', eleTag,*eleNodes,Mat1, Mat2, Mat3, Mat4, Mat5, Mat6, Mat7, Mat8, Mat9, Mat10, Mat11, Mat12, Mat13, [eleHeightFac=1.0, eleWidthFac=1.0])
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of four element nodes
   ``Mat1`` |int|                        uniaxial material tag for left bar-slip spring at node 1
   ``Mat2`` |int|                        uniaxial material tag for right bar-slip spring at node 1
   ``Mat3`` |int|                        uniaxial material tag for interface-shear spring at node 1
   ``Mat4`` |int|                        uniaxial material tag for lower bar-slip spring at node 2
   ``Mat5`` |int|                        uniaxial material tag for upper bar-slip spring at node 2
   ``Mat6`` |int|                        uniaxial material tag for interface-shear spring at node 2
   ``Mat7`` |int|                        uniaxial material tag for left bar-slip spring at node 3
   ``Mat8`` |int|                        uniaxial material tag for right bar-slip spring at node 3
   ``Mat9`` |int|                        uniaxial material tag for interface-shear spring at node 3
   ``Mat10`` |int|                       uniaxial material tag for lower bar-slip spring at node 4
   ``Mat11`` |int|                       uniaxial material tag for upper bar-slip spring at node 4
   ``Mat12`` |int|                       uniaxial material tag for interface-shear spring at node 4
   ``Mat13`` |int|                       uniaxial material tag for shear-panel
   ``eleHeightFac`` |float|              floating point value (as a ratio to the total height of the element) to be considered for determination of the distance in between the tension-compression couples (optional, default: 1.0)
   ``eleWidthFac`` |float|               floating point value (as a ratio to the total width of the element) to be considered for determination of the distance in between the tension-compression couples (optional, default: 1.0)
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/BeamColumnJoint_Element>`_
