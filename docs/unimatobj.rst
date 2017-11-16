.. include:: sub.txt

UniaxialMaterial Object
=======================

.. class:: uniaxialMaterial()

   A python :class:`uniaxialMaterial` object
   is a wrapper to the OpenSees ``UniaxialMaterial`` object.

   .. note::
   
      One cannot create an :class:`uniaxialMaterial` object
      directly, but only through :ref:`unimat-class-methods`.


Object attributes
-------------------

.. attribute:: uniaxialMaterial.strain
      
   An object attribute (get/set) |float|.
   The material strains.

.. attribute:: uniaxialMaterial.stress

   An object attribute (get) |float|.
   The material stress.

.. attribute:: uniaxialMaterial.tangent

   An object attribute (get) |float|.
   The material tangent at current strain.

.. attribute:: uniaxialMaterial.dampTangent

   An object attribute (get) |float|.
   The material damp tangent at current strain.


Object methods
-------------------

#. :meth:`uniaxialMaterial.__str__`
#. :meth:`uniaxialMaterial.remove`
		  
.. method:: uniaxialMaterial.__str__()

   The string reprsentation of the :class:`uniaxialMaterial`. Usually
   used in the |print| function.

.. method:: uniaxialMaterial.remove()

   Remove the corresponding OpenSees ``UniaxialMaterial`` object.
   It will not remove the materials in :class:`element`.
	       
   .. seealso::

      :meth:`node.remove`


.. _unimat-class-methods:

Class methods
--------------

#. :meth:`uniaxialMaterial.Elastic`
#. :meth:`uniaxialMaterial.Hardening`

.. classmethod:: uniaxialMaterial.Elastic(tag, E, eta=0.0, Eneg=E)

   Create a Elastic :class:`uniaxialMaterial` object

   ========================   =============================================================
   ``tag`` |int|              :class:`uniaxialMaterial` tag.
   ``E`` |float|              Tangent stiffness.
   ``eta`` |float|            Damping tangent.
   ``Eneg`` |float|           Tangent in compression.
   ========================   =============================================================

.. classmethod:: uniaxialMaterial.Hardening(tag, E, sigmaY, Hiso, Hkin, eta=0.0)

   Create a Hardening :class:`uniaxialMaterial` object
   with combined linear kinematic and isotropic hardening. The model includes optional visco-plasticity using a Perzyna formulation.

   ========================   =============================================================
   ``tag`` |int|              :class:`uniaxialMaterial` tag.
   ``E`` |float|              Tangent stiffness.
   ``sigmaY`` |float|         Yield stress or force.
   ``Hiso`` |float|           Isotropic hardening modulus.
   ``Hkin`` |float|           Kinematic hardening modulus.
   ``eta`` |float|            Visco-plastic coefficient. (optional)
   ========================   =============================================================


Examples
----------

::

     mat = uniaxialMaterial.Hardening(1, E=1e6, sigmaY=36.0,
                                      Hiso=0.0, Hkin=alpha/(1-alpha)*E)
     mat.strain = 0.5
     print(mat.strain, mat.stress, mat.tangent, mat.dampTangent)
     print(mat)

