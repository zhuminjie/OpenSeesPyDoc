.. include:: sub.txt

================================
 SimpleFracture material wrapper
================================

Constructs a **SimpleFracture** uniaxial material wrapper that imposes tensile fracture on the wrapped material: after strain exceeds a maximum tensile strain, the wrapper supplies compressive stress based on an estimate of the elastic strain.

.. function:: uniaxialMaterial('SimpleFracture', matTag, otherTag, maxStrain)

   ================================   ===========================================================================
   ``matTag`` |int|                  unique material tag
   ``otherTag`` |int|                tag of a previously defined uniaxial material
   ``maxStrain`` |float|             maximum tensile strain (fracture strain)
   ================================   ===========================================================================

.. admonition:: Example

   .. code-block:: python

      import openseespy.opensees as ops

      ops.uniaxialMaterial('Hardening', 1, 3.0, 1.0, 0.1)
      ops.uniaxialMaterial('SimpleFracture', 2, 1, 0.8)

Code developed by: **Michael H. Scott**
