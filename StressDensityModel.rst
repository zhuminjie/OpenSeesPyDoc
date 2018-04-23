.. include:: sub.txt

====================
 StressDensityModel
====================

.. function:: nDMaterial('StressDensityModel', matTag, mDen, eNot, A, n, nu, a1, b1, a2, b2, a3, b3, fd, muNot, muCyc, sc, M, patm, ssl1, ssl2, ssl3, ssl4, ssl5, ssl6, ssl7, ssl8, ssl9, ssl10, hsl, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
   :noindex:

   This command is used to construct a multi-dimensional stress density material object for modeling sand behaviour following the work of Cubrinovski and Ishihara (1998a,b).

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``mDen`` |float|                   mass density
   ``eNot`` |float|                   initial void ratio
   ``A`` |float|                      constant for elastic shear modulus
   ``n`` |float|                      pressure dependency exponent for elastic shear modulus
   ``nu`` |float|                     Poisson's ratio
   ``a1`` |float|                     peak stress ratio coefficient (:math:`etaMax = a1 + b1*Is`)
   ``b1`` |float|                     peak stress ratio coefficient (:math:`etaMax = a1 + b1*Is`)
   ``a2`` |float|                     max shear modulus coefficient (:math:`Gn_max = a2 + b2*Is`)
   ``b2`` |float|                     max shear modulus coefficient (:math:`Gn_max = a2 + b2*Is`)
   ``a3`` |float|                     min shear modulus coefficient (:math:`Gn_min = a3 + b3*Is`)
   ``b3`` |float|                     min shear modulus coefficient (:math:`Gn_min = a3 + b3*Is`)
   ``fd`` |float|                     degradation constant
   ``muNot`` |float|                  dilatancy coefficient (monotonic loading)
   ``muCyc`` |float|                  dilatancy coefficient (cyclic loading)
   ``sc`` |float|                     dilatancy strain
   ``M`` |float|                      critical state stress ratio
   ``patm`` |float|                   atmospheric pressure (in appropriate units)
   ``ssl1`` |float|                   void ratio of quasi steady state (QSS-line) at pressure p1 (default = 0.877)
   ``ssl2`` |float|                   void ratio of quasi steady state (QSS-line) at pressure p2 (default = 0.877)
   ``ssl3`` |float|                   void ratio of quasi steady state (QSS-line) at pressure p3 (default = 0.873)
   ``ssl4`` |float|                   void ratio of quasi steady state (QSS-line) at pressure p4 (default = 0.870)
   ``ssl5`` |float|                   void ratio of quasi steady state (QSS-line) at pressure p5 (default = 0.860)
   ``ssl6`` |float|                   void ratio of quasi steady state (QSS-line) at pressure p6 (default = 0.850)
   ``ssl7`` |float|                   void ratio of quasi steady state (QSS-line) at pressure p7 (default = 0.833)
   ``ssl8`` |float|                   void ratio of quasi steady state (QSS-line) at pressure p8 (default = 0.833)
   ``ssl9`` |float|                   void ratio of quasi steady state (QSS-line) at pressure p9 (default = 0.833)
   ``ssl10`` |float|                  void ratio of quasi steady state (QSS-line) at pressure p10 (default = 0.833)
   ``hsl`` |float|                    void ratio of upper reference state (UR-line) for all pressures
                                      (default = 0.895)
   ``p1`` |float|                     pressure corresponding to ssl1 (default = 1.0 kPa)
   ``p2`` |float|                     pressure corresponding to ssl1 (default = 10.0 kPa)
   ``p3`` |float|                     pressure corresponding to ssl1 (default = 30.0 kPa)
   ``p4`` |float|                     pressure corresponding to ssl1 (default = 50.0 kPa)
   ``p5`` |float|                     pressure corresponding to ssl1 (default = 100.0 kPa)
   ``p6`` |float|                     pressure corresponding to ssl1 (default = 200.0 kPa)
   ``p7`` |float|                     pressure corresponding to ssl1 (default = 400.0 kPa)
   ``p8`` |float|                     pressure corresponding to ssl1 (default = 400.0 kPa)
   ``p9`` |float|                     pressure corresponding to ssl1 (default = 400.0 kPa)
   ``p10`` |float|                    pressure corresponding to ssl1 (default = 400.0 kPa)
   ================================   ===========================================================================

The material formulations for the StressDensityModel object are:

* ``'ThreeDimensional'``
* ``'PlaneStrain'``

References

Cubrinovski, M. and Ishihara K. (1998a) 'Modelling of sand behaviour based on state concept,' Soils and Foundations, 38(3), 115-127.

Cubrinovski, M. and Ishihara K. (1998b) 'State concept and modified elastoplasticity for sand modelling,' Soils and Foundations, 38(4), 213-225.

Das, S. (2014) Three Dimensional Formulation for the Stress-Strain-Dilatancy Elasto-Plastic Constitutive Model for Sand Under Cyclic Behaviour, Master's Thesis, University of Canterbury.
