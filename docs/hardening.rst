.. include:: sub.txt

==========================================
 harderning class
==========================================

.. class:: hardening(E, sigmaY, Hiso, Hkin, eta=0.0)

   Create a Hardening :class:`uniaxialMaterial` object
   with combined linear kinematic and isotropic hardening. The model includes optional visco-plasticity using a Perzyna formulation. A subclass of :class:`uniaxialMaterial`.

   ========================   =============================================================
   ``E`` |float|              Tangent stiffness.
   ``sigmaY`` |float|         Yield stress or force.
   ``Hiso`` |float|           Isotropic hardening modulus.
   ``Hkin`` |float|           Kinematic hardening modulus.
   ``eta`` |float|            Visco-plastic coefficient. (optional)
   ========================   =============================================================

   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`uniaxialMaterial.tag`
     #. :attr:`uniaxialMaterial.strain`
     #. :attr:`uniaxialMaterial.plasticStrain`
     #. :attr:`uniaxialMaterial.stress`
     #. :attr:`uniaxialMaterial.tangent`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`

