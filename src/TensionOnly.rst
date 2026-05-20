.. include:: sub.txt

===============================
 TensionOnly material wrapper
===============================

Constructs a **TensionOnly** uniaxial material wrapper: when the wrapped material would return negative stress, the wrapper returns zero stress and zero tangent and does **not** call ``commitState()`` on the wrapped material. Only tensile (positive) stress is returned.

.. function:: uniaxialMaterial('TensionOnly', matTag, otherTag, *args)

   Optional: ``'-min'``, ``minStrain``, ``'-max'``, ``maxStrain``.

   ================================   ===========================================================================
   ``matTag`` |int|                  unique material tag
   ``otherTag`` |int|                tag of a previously defined uniaxial material
   ================================   ===========================================================================

.. admonition:: Example

   .. code-block:: python

      import openseespy.opensees as ops

      ops.uniaxialMaterial('Elastic', 1, 100.0)
      ops.uniaxialMaterial('TensionOnly', 2, 1)

Code developed by: **Michael H. Scott**
