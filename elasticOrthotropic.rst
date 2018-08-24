.. include:: sub.txt

====================
 ElasticOrthotropic
====================

.. function:: nDMaterial('ElasticOrthotropic', matTag, Ex, Ey, Ez, vxy, vyz, vzx, Gxy, Gyz, Gzx, rho=0.0)
   :noindex:

   This command is used to construct an ElasticOrthotropic material object.

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``Ex`` |float|                     elastic modulus in x direction
   ``Ey`` |float|                     elastic modulus in y direction
   ``Ez`` |float|                     elastic modulus in z direction
   ``vxy`` |float|                    Poisson's ratios in x and y plane
   ``vyz`` |float|                    Poisson's ratios in y and z plane
   ``vzx`` |float|                    Poisson's ratios in z and x plane
   ``Gxy`` |float|                    shear modulii in x and y plane
   ``Gyz`` |float|                    shear modulii in y and z plane
   ``Gzx`` |float|                    shear modulii in z and x plane
   ``rho`` |float|                    mass density (optional)
   ================================   ===========================================================================

The material formulations for the ElasticOrthotropic object are:

* ``'ThreeDimensional'``
* ``'PlaneStrain'``
* ``'Plane Stress'``
* ``'AxiSymmetric'``
* ``'BeamFiber'``
* ``'PlateFiber'``
