.. include:: sub.txt

==================
 Concrete02mod
==================

.. function:: uniaxialMaterial('Concrete02mod', matTag, fpc, epsc0, ec0, fpcu, epsU, lambda, ft, Ets)
   :noindex:

   This command is used to construct a uniaxial concrete material object with degraded linear unloading/reloading stiffness according to the work of Karsan-Jirsa and no tensile strength. 
   It is based on the Concrete02 material, but the pre-peak response follows the Popovic's equation isntead of the Hognestad parabola, therefore, the Young's modulus is defined by the user as an input.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``fpc`` |float|                       concrete compressive strength at 28 days (compression is negative)
   ``epsc0`` |float|                     concrete strain at maximum strength
   ``ec0`` |float|                       Young's modulus
   ``fpcu`` |float|                      concrete crushing strength
   ``epsU`` |float|                      concrete strain at crushing strength
   ``lambda`` |float|                    ratio between unloading slope at $epscu and initial slope
   ``ft`` |float|                        tensile strength
   ``Ets`` |float|                       tension softening stiffness (absolute value) (slope of the linear tension softening branch)

   ===================================   ===========================================================================

.. note::

   #. Compressive concrete parameters should be input as negative values.
   #. The initial slope for this model is ec0 (defined by the user)


.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Concrete02_Material_--_Linear_Tension_Softening>`_
