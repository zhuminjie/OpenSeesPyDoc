.. include:: sub.txt

==================
MaterialBackbone
==================

.. function:: hystereticBackbone('Material', backboneTag, matTag, '-compression')
   :noindex:

   The backbone function treats a uniaxial material as a hysteretic backbone by removing path dependency, i.e. commitState is never called on the uniaxial material.

   ===================================   ===========================================================================
   ``backboneTag`` |int|                 integer tag identifying the backbone function.
   ``matTag`` |int|                      tag for a predefined uniaxial material
   ===================================   ===========================================================================

