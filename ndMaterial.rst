.. include:: sub.txt

===========================
 nDMaterial commands
===========================

.. function:: nDMaterial(matType, matTag, *matArgs)

   This command is used to construct an NDMaterial object which represents the stress-strain relationship at the gauss-point of a continuum element.

   ================================   ===========================================================================
   ``matType`` |str|                  material type
   ``matTag`` |int|                   material tag.
   ``matArgs`` |list|                 a list of material arguments, must be preceded with ``*``.
   ================================   ===========================================================================

For example,

.. code-block:: python

   matType = 'ElasticIsotropic'
   matTag = 1
   matArgs = [E, v]
   nDMaterial(matType, matTag, *matArgs)



The following contain information about available ``matType``:

.. toctree::
   :maxdepth: 2

   elasticIsotropic
   elasticOrthotropic
   J2Plasticity
   DrunkerPrager
   Damage2p
   PlaneStress
   PlaneStrain
   MultiAxialCyclicPlasticity
   BoundingCamClay
   PlateFiber
   FSAM
   ManzariDafalias
   PM4Sand
   StressDensityModel
   AcousticMedium

.. toctree::
   :maxdepth: 2
   :caption: Tsinghua Sand Models

   CycLiqCP
   CycLiqCPSP



.. toctree::
   :maxdepth: 2
   :caption: Materials for Modeling Concrete Walls

   PlaneStressUserMaterial
   PlateFromPlaneStress
   PlateRebar



.. toctree::
   :maxdepth: 2
   :caption: Contact Materials for 2D and 3D

   ContactMaterial2D
   ContactMaterial3D


.. toctree::
   :maxdepth: 2
   :caption: Wrapper material for Initial State Analysis

   InitialStateAnalysisWrapper


.. toctree::
   :maxdepth: 2
   :caption: UC San Diego soil models

   PressureIndependMultiYield
   PressureDependMultiYield
   PressureDependMultiYield02


.. toctree::
   :maxdepth: 2
   :caption: UC San Diego Saturated Undrained soil

   FluidSolidPorousMaterial
