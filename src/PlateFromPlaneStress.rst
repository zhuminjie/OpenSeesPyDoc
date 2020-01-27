.. include:: sub.txt

=========================
 PlateFromPlaneStress
=========================

.. function:: nDMaterial('PlateFromPlaneStress', newmatTag, matTag, OutofPlaneModulus)
   :noindex:

   This command is used to create the multi-dimensional concrete material model that is based on the damage mechanism and smeared crack model.

   ================================   ===========================================================================
   ``newmatTag`` |int|                new integer tag identifying material deriving from pre-defined
                                      PlaneStress material
   ``matTag`` |int|                   integer tag identifying PlaneStress material
   ``OutofPlaneModulus`` |float|      shear modulus for out of plane stresses
   ================================   ===========================================================================
