.. include:: sub.txt

==============================================
 uniaxialMaterial -- One Dimentional Material
==============================================

.. class:: uniaxialMaterial()

   A subclass of :class:`tagged`
   and a base class for UniaxialMaterial objects.

   One cannot create an :class:`uniaxialMaterial` object
   directly, but only through its subclasses.

   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`uniaxialMaterial.tag`
     #. :attr:`uniaxialMaterial.strain`
     #. :attr:`uniaxialMaterial.stress`
     #. :attr:`uniaxialMaterial.tangent`
     #. :attr:`uniaxialMaterial.dampTangent`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`

Following are  available uniaxial material subclasses in the OpenSees:

.. toctree::
   :maxdepth: 2


.. attribute:: uniaxialMaterial.strain
      
   An object attribute (get/set) |float|.
   The material strains.

   ::

      mat.strain = 0.01

.. attribute:: uniaxialMaterial.stress

   An object attribute (get) |float|.
   The material stress.

   ::

      print(mat.stress)

.. attribute:: uniaxialMaterial.tangent

   An object attribute (get) |float|.
   The material tangent at current strain.

   ::

      print(mat.tangent)

.. attribute:: uniaxialMaterial.dampTangent

   An object attribute (get) |float|.
   The material damp tangent at current strain.

   ::

      print(mat.dampTangent)




.. _unimat-class-methods:

Class methods
--------------

#. :meth:`uniaxialMaterial.Elastic`
#. :meth:`uniaxialMaterial.Hardening`

.. classmethod:: uniaxialMaterial.Elastic(E, eta=0.0, Eneg=E)

   Create a Elastic :class:`uniaxialMaterial` object

   ========================   =============================================================
   ``E`` |float|              Tangent stiffness.
   ``eta`` |float|            Damping tangent.
   ``Eneg`` |float|           Tangent in compression.
   ========================   =============================================================

   ::

      mat = uniaxialMaterial.Elastic(E)

.. classmethod:: uniaxialMaterial.Hardening(E, sigmaY, Hiso, Hkin, eta=0.0)

   Create a Hardening :class:`uniaxialMaterial` object
   with combined linear kinematic and isotropic hardening. The model includes optional visco-plasticity using a Perzyna formulation.

   ========================   =============================================================
   ``E`` |float|              Tangent stiffness.
   ``sigmaY`` |float|         Yield stress or force.
   ``Hiso`` |float|           Isotropic hardening modulus.
   ``Hkin`` |float|           Kinematic hardening modulus.
   ``eta`` |float|            Visco-plastic coefficient. (optional)
   ========================   =============================================================

   ::

      mat = uniaxialMaterial.Hardening(E=1e6, sigmaY=36.0, Hiso=0.0, Hkin=alpha/(1-alpha)*E)


