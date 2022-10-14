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

.. #. :doc:`Hardening`
.. #. :doc:`Cast`
.. #. :doc:`ViscousDamper`
.. #. :doc:`BilinearOilDamper`
.. #. :doc:`Bilin`
.. #. :doc:`ModIMKPeakOriented`
.. #. :doc:`ModIMKPinching`
.. #. :doc:`SAWS`
.. #. :doc:`BarSlip`
.. #. :doc:`Bond_SP01`