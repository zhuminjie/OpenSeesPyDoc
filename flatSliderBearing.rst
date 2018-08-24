.. include:: sub.txt

===========================
Flat Slider Bearing Element
===========================

This command is used to construct a flatSliderBearing element object, which is defined by two nodes. The iNode represents the flat sliding surface and the jNode represents the slider. The element can have zero length or the appropriate bearing height. The bearing has unidirectional (2D) or coupled (3D) friction properties for the shear deformations, and force-deformation behaviors defined by UniaxialMaterials in the remaining two (2D) or four (3D) directions. To capture the uplift behavior of the bearing, the user-specified UniaxialMaterial in the axial direction is modified for no-tension behavior. By default (sDratio = 0.0) P-Delta moments are entirely transferred to the flat sliding surface (iNode). It is important to note that rotations of the flat sliding surface (rotations at the iNode) affect the shear behavior of the bearing. To avoid the introduction of artificial viscous damping in the isolation system (sometimes referred to as "damping leakage in the isolation system"), the bearing element does not contribute to the Rayleigh damping by default. If the element has non-zero length, the local x-axis is determined from the nodal geometry unless the optional x-axis vector is specified in which case the nodal geometry is ignored and the user-defined orientation is utilized.

.. function:: element('flatSliderBearing', eleTag,*eleNodes,frnMdlTag, kInit,'-P', matTag,'-Mz', matTag,['-orient', x1, x2, x3, y1, y2, y3],['-shearDist', sDratio],['-doRayleigh'],['-mass', m],['-iter', maxIter, tol])
   :noindex:

   For a two-dimensional problem

.. function:: element('flatSliderBearing', eleTag,*eleNodes,frnMdlTag, kInit,'-P', matTag,'-T', matTag,'-My', matTag,'-Mz', matTag,['-orient',[x1, x2, x3], y1, y2, y3],['-shearDist', sDratio],['-doRayleigh'],['-mass', m],['-iter', maxIter, tol])
   :noindex:

   For a three-dimensional problem

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of two element nodes
   ``frnMdlTag`` |float|                 tag associated with previously-defined FrictionModel
   ``kInit`` |float|                     initial elastic stiffness in local shear direction
   ``'-P'``  ``matTag`` |int|            tag associated with previously-defined UniaxialMaterial in axial direction
   ``'-T'``  ``matTag`` |int|            tag associated with previously-defined UniaxialMaterial in torsional direction
   ``'-My'``  ``matTag`` |int|           tag associated with previously-defined UniaxialMaterial in moment direction around local y-axis
   ``'-Mz'``  ``matTag`` |int|           tag associated with previously-defined UniaxialMaterial in moment direction around local z-axis
   ``x1``  ``x2``  ``x3`` |float|        vector components in global coordinates defining local x-axis (optional)
   ``y1``  ``y2``  ``y3`` |float|        vector components in global coordinates defining local y-axis (optional)
   ``sDratio`` |float|                   shear distance from iNode as a fraction of the element length (optional, default = 0.0)
   ``'-doRayleigh'`` |str|               to include Rayleigh damping from the bearing (optional, default = no Rayleigh damping contribution)
   ``m`` |float|                         element mass (optional, default = 0.0)
   ``maxIter`` |int|                     maximum number of iterations to undertake to satisfy element equilibrium (optional, default = 20)
   ``tol`` |float|                       convergence tolerance to satisfy element equilibrium (optional, default = 1E-8)
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Flat_Slider_Bearing_Element>`_
