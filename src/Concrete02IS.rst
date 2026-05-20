.. include:: sub.txt

==============================================
 Concrete02IS material
==============================================

This command constructs a uniaxial concrete material with the same compressive envelope and tension/cyclic behavior as :doc:`Concrete02`, but with **user-defined initial stiffness** :math:`E_0`. In Concrete02 the initial stiffness is fixed at :math:`E_c = 2 f'_c / \varepsilon_{c0}`; Concrete02IS allows any :math:`E_0` (for example :math:`57000\sqrt{f'_c}` in psi units, or a secant stiffness to peak).

.. function:: uniaxialMaterial('Concrete02IS', matTag, E0, fpc, epsc0, fpcu, epsU, *optional)

   Optional trailing arguments (in order): ratio between unloading slope at ``epsU`` and initial slope, tensile strength ``ft``, tension softening stiffness ``Ets``.

   ================================   ===========================================================================
   ``matTag`` |int|                  unique material tag
   ``E0`` |float|                    initial (elastic) stiffness
   ``fpc`` |float|                   concrete compressive strength at 28 days (compression negative)
   ``epsc0`` |float|                 concrete strain at maximum strength (negative)
   ``fpcu`` |float|                  concrete crushing strength (negative)
   ``epsU`` |float|                  concrete strain at crushing strength (negative)
   ================================   ===========================================================================

.. note::

   Compressive parameters are taken as negative; if given positive, they are converted internally. Input :math:`E_0` affects unloading/reloading stiffness in compression. The ascending branch uses the Popovics equation (Concrete02 uses the Hognestad parabola).

.. admonition:: Example

   .. code-block:: python

      import openseespy.opensees as ops

      fc, epsc0 = 4000.0, -0.002
      fcu, epscu = -1000.0, -0.006
      Ec = 2.0 * fc / (-epsc0)
      ops.uniaxialMaterial('Concrete02IS', 1, Ec, fc, epsc0, fcu, epscu)
      ops.uniaxialMaterial('Concrete02IS', 2, Ec, fc, epsc0, fcu, epscu, 0.1, 500.0, 1738.33)

.. seealso::

   :doc:`Concrete02`.

Code developed by: Filip Filippou (Concrete02); Nasser Marafi (Concrete02IS).
