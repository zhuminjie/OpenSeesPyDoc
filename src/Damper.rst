.. include:: sub.txt

========================
 Damper material wrapper
========================

Constructs a **Damper** uniaxial material wrapper. The wrapper uses the stress–strain response of any uniaxial material as a **stress versus strain-rate** relationship for damping: strain rate is passed as strain, and the material tangent provides the damping tangent.

.. function:: uniaxialMaterial('Damper', matTag, otherTag, *args)

   ``*args`` may include ``'-factors'``, ``fact1``, ``fact2``, … for multiple materials.

   ================================   ===========================================================================
   ``matTag`` |int|                  unique material tag
   ``otherTag`` |int|                tag of a previously defined uniaxial material
   ================================   ===========================================================================

.. admonition:: Example

   .. code-block:: python

      import openseespy.opensees as ops

      ops.uniaxialMaterial('Elastic', 1, 100.0)
      ops.uniaxialMaterial('Damper', 2, 1)

Code developed by: **Michael H. Scott**
