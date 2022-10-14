.. include:: sub.txt

==================
Backbone Material
==================

.. function:: uniaxialMaterial('Backbone', matTag, backboneTag)
   :noindex:

   This command uses a :ref:`HystereticBackbone` object to represent a path-independent uniaxial material. Since it is path-independent, no state information is stored by BackboneMaterial.



   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``backboneTag`` |int|                 integer tag identifying a predefined backbone function.
   ===================================   ===========================================================================

.. _HystereticBackbone:

Hysteretic Backbone
------------------------

HystereticBackbone represents a backbone curve for hysteretic models.


#. :doc:`ArctangentBackbone`
#. :doc:`BilinearBackbone`
#. :doc:`ManderBackbone`
#. :doc:`MultilinearBackbone`
#. :doc:`TrilinearBackbone`
#. :doc:`MaterialBackbone`
#. :doc:`ReeseStiffClayBelowWS`
#. :doc:`ReeseStiffClayAboveWS`
#. :doc:`VuggyLimestone`
#. :doc:`CementedSoil`
#. :doc:`WeakRock`
#. :doc:`LiquefiedSand`

.. toctree::
   :maxdepth: 2
   :hidden:
   
   ArctangentBackbone
   BilinearBackbone
   ManderBackbone
   MultilinearBackbone
   TrilinearBackbone
   MaterialBackbone
   ReeseStiffClayBelowWS
   ReeseStiffClayAboveWS
   VuggyLimestone
   CementedSoil
   WeakRock
   LiquefiedSand
