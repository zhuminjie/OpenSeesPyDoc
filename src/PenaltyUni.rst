.. include:: sub.txt

==========================
 Penalty material wrapper
==========================

Constructs a **Penalty** uniaxial material wrapper that adds a small stiffness to the wrapped material. Helps avoid singular stiffness from perfect plasticity; lightweight alternative to placing the wrapped material in parallel with an elastic material.

.. function:: uniaxialMaterial('Penalty', matTag, otherTag, penalty, *args)

   Optional ``'-noStress'``: penalty stiffness is added only to the tangent, not to stress.

   ================================   ===========================================================================
   ``matTag`` |int|                  unique material tag
   ``otherTag`` |int|                tag of a previously defined uniaxial material
   ``penalty`` |float|               stiffness added to tangent (and optionally stress); same units as tangent
   ================================   ===========================================================================

.. note::

   Use a small penalty value so the response stays dominated by the wrapped material.

.. admonition:: Example

   .. code-block:: python

      import openseespy.opensees as ops

      E = 29000.0
      penalty = 0.05 * E
      ops.uniaxialMaterial('Elastic', 1, E)
      ops.uniaxialMaterial('Penalty', 2, 1, penalty)

Code developed by: **Michael H. Scott**
