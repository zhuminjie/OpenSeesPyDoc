.. include:: sub.txt

=========================
 PlateFromPlaneStress
=========================

.. function:: nDMaterial('PlateFromPlaneStress', matTag, newmatTag, matTag, OutofPlaneModulus)
   :noindex:

   This command is used to create the multi-dimensional concrete material model that is based on the damage mechanism and smeared crack model.

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``newmatTag`` |int|                new integer tag identifying material deriving from pre-defined
                                      PlaneStressUserMaterial
   ``matTag`` |int|                   integer tag identifying PlaneStressUserMaterial
   ``OutofPlaneModulus`` |float|      shear modulus of out plane
   ================================   ===========================================================================
