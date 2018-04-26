.. include:: sub.txt

===========================
 uniaxialMaterial commands
===========================

.. function:: uniaxialMaterial(matType, matTag, *matArgs)

   This command is used to construct a UniaxialMaterial object which represents uniaxial stress-strain (or force-deformation) relationships.

   ================================   ===========================================================================
   ``matType`` |str|                  material type
   ``matTag`` |int|                   material tag.
   ``matArgs`` |list|                 a list of material arguments, must be preceded with ``*``.
   ================================   ===========================================================================

For example,

.. code-block:: python

   matType = 'Steel01'
   matTag = 1
   matArgs = [Fy, E0, b]
   uniaxialMaterial(matType, matTag, *matArgs)



The following contain information about available ``matType``:

.. toctree::
   :maxdepth: 2
   :caption: Steel & Reinforcing-Steel Materials

   steel01
   steel02
   steel4
   Hysteretic
   ReinforcingSteel
   Dodd_Restrepo
   RambergOsgoodSteel
   SteelMPF


.. toctree::
   :maxdepth: 2
   :caption: Concrete Materials

   Concrete01
   Concrete02
   Concrete04
   Concrete06
   Concrete07
   Concrete01WithSITC
   ConfinedConcrete01
   ConcreteD
   FRPConfinedConcrete
   ConcreteCM



.. toctree::
   :maxdepth: 2
   :caption: Standard Uniaxial Materials

   ElasticUni
   ElasticPP
   ElasticPPGap
   ENT
   ParallelUni
   SeriesUni

.. toctree::
   :maxdepth: 2
   :caption: PyTzQz uniaxial materials for p-y, t-z and q-z elements for modeling soil-structure interaction through the piles in a structural foundation

   PySimple1
   TzSimple1
   QzSimple1
   PyLiq1
   TzLiq1


.. toctree::
   :maxdepth: 2
   :caption: Other Uniaxial Materials

   Hardening
   Cast
   ViscousDamper
   BilinearOilDamper
   Bilin
   ModIMKPeakOriented
   ModIMKPinching
   SAWS
   BarSlip
   Bond_SP01
   Fatigue
   ImpactMaterial
   HyperbolicGapMaterial
   LimitState
   MinMax
   ElasticBilin
   ElasticMultiLinear
   MultiLinear
   InitStrainMaterial
   InitStressMaterial
   PathIndependent
   Pinching4
   ECC01
   SelfCentering
   Viscous
   BoucWen
   BWBN
   KikuchiAikenHDR
   KikuchiAikenLRB
   AxialSp
   AxialSpHD
   PinchingLimitStateMaterial
   CFSWSWP
   CFSSSWP
