.. include:: sub.txt

=========================
 PlaneStressUserMaterial
=========================

.. function:: nDMaterial('PlaneStressUserMaterial', matTag, fc, ft, fcu, epsc0, epscu, epstu, stc)
   :noindex:

   This command is used to create the multi-dimensional concrete material model that is based on the damage mechanism and smeared crack model.

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``fc`` |float|                     concrete compressive strength at 28 days (positive)
   ``ft`` |float|                     concrete tensile strength (positive)
   ``fcu`` |float|                    concrete crushing strength (negative)
   ``epsc0`` |float|                  concrete strain at maximum strength (negative)
   ``epscu`` |float|                  concrete strain at crushing strength (negative)
   ``epstu`` |float|                  ultimate tensile strain (positive)
   ``stc`` |float|                    shear retention factor
   ================================   ===========================================================================
