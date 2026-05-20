.. include:: sub.txt

============================
 Multiplier material wrapper
============================

Constructs a **Multiplier** uniaxial material wrapper: stress and tangent of the wrapped material are multiplied by a factor. Typical uses include overstrength factors and p-y multipliers (e.g. pile group shadowing).

.. function:: uniaxialMaterial('Multiplier', matTag, otherTag, multiplier)

   ================================   ===========================================================================
   ``matTag`` |int|                  unique material tag
   ``otherTag`` |int|                tag of a previously defined uniaxial material
   ``multiplier`` |float|           factor applied to stress and tangent
   ================================   ===========================================================================

.. admonition:: Example

   .. code-block:: python

      import openseespy.opensees as ops

      ops.uniaxialMaterial('Elastic', 1, 100.0)
      ops.uniaxialMaterial('Multiplier', 2, 1, 0.8)

Code developed by: **Michael H. Scott**
