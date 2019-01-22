.. include:: sub.txt

==================
 PM4Sand
==================

.. function:: nDMaterial('PM4Sand', matTag, Dr, G0, hpo, Den, patm, h0, emax, emin, nb, nd, Ado, zmax, cz, ce, phic, nu, cgd, cdr, ckaf, Q, R, m, Fsed_min, p_sedo)
   :noindex:

   This command is used to construct a 2-dimensional PM4Sand material.

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``Dr`` |float|                     Relative density, in fraction
   ``G0`` |float|                     Shear modulus constant
   ``hpo`` |float|                    Contraction rate parameter
   ``Den`` |float|                    Mass density of the material
   ``P_atm`` |float|                  Optional, Atmospheric pressure
   ``h0`` |float|                     Optional, Variable that adjusts the ratio of plastic modulus
                                      to elastic modulus
   ``emax`` |float|                   Optional, Maximum and minimum void ratios
   ``emin`` |float|                   Optional, Maximum and minimum void ratios
   ``nb`` |float|                     Optional, Bounding surface parameter, :math:`nb \ge 0`
   ``nd`` |float|                     Optional, Dilatancy surface parameter :math:`nd \ge 0`
   ``Ado`` |float|                    Optional, Dilatancy parameter, will be computed at the time
                                      of initialization if input value is negative
   ``z_max`` |float|                  Optional, Fabric-dilatancy tensor parameter
   ``cz`` |float|                     Optional, Fabric-dilatancy tensor parameter
   ``ce`` |float|                     Optional, Variable that adjusts the rate of strain accumulation
                                      in cyclic loading
   ``phic`` |float|                   Optional, Critical state effective friction angle
   ``nu`` |float|                     Optional, Poisson's ratio
   ``cgd`` |float|                    Optional, Variable that adjusts degradation of elastic modulus
                                      with accumulation of fabric
   ``cdr`` |float|                    Optional, Variable that controls the rotated dilatancy surface
   ``ckaf`` |float|                   Optional, Variable that controls the effect that sustained
                                      static shear stresses have on plastic modulus
   ``Q`` |float|                      Optional, Critical state line parameter
   ``R`` |float|                      Optional, Critical state line parameter
   ``m`` |float|                      Optional, Yield surface constant (radius of yield surface
                                      in stress ratio space)
   ``Fsed_min`` |float|               Optional, Variable that controls the minimum value the
                                      reduction factor of the elastic moduli can get during reconsolidation
   ``p_sedo`` |float|                 Optional, Mean effective stress up to which reconsolidation
                                      strains are enhanced
   ================================   ===========================================================================

The material formulations for the PM4Sand object are:

* ``'PlaneStrain'``

See als `here <http://opensees.berkeley.edu/wiki/index.php/PM4Sand_Material>`_


References

R.W.Boulanger, K.Ziotopoulou. "PM4Sand(Version 3.1): A Sand Plasticity Model for Earthquake Engineering Applications". Report No. UCD/CGM-17/01 2017
