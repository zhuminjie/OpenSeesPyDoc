.. _unimat-obj:

UniaxialMateria Object
=======================

.. index:: object: unimat

.. class:: uniaxialMaterial()

   A python uniaxialMaterial object
   is a wrapper to the OpenSees ``UniaxialMaterial`` object.

   One cannot create an uniaxialMaterial object
   directly, but only through the class methods below.

   .. attribute:: strain
      
      An object attribute (get/set).
      The material strains.

   .. attribute:: stress

      An object attribute (get).
      The material stress.

   .. attribute:: tangent

      An object attribute (get).
      The material tangent at current strain.

   .. attribute:: dampTangent

      An object attribute (get).
      The material damp tangent at current strain.

   .. method:: __str__()

      The string reprsentation of the node. Usually
      used in the `print`_ function.

   .. method:: remove()

      Remove the corresponding OpenSees ``UniaxialMaterial`` object.
	       
      .. note::
      
	 The python :class:`uniaxialMaterial` object is not removed, but
	 any operation on the python :class:`uniaxialMaterial` object will fail.
	 When you ``del`` a :class:`uniaxialMaterial` or set it to ``None``,
	 the python :class:`uniaxialMaterial` object is removed, but
	 the OpenSees ``UniaxialMaterial`` is not.
	       
   .. classmethod:: Hardening(tag, E, sigmaY, Hiso, Hkin, eta=0.0)

      Create a Hardening material, where
      ``tag`` is the material tag,
      ``E`` is tangent stiffness,
      ``sigmaY`` is the yield stress or force,
      ``Hiso`` is the isotropic hardening modulus,
      ``Hkin`` is the kinematic hardening modulus,
      and ``eta`` is visco-plastic coefficient.


   Examples::

     mat = uniaxialMaterial.Hardening(1, E=1e6, sigmaY=36.0,
                                      Hiso=0.0, Hkin=alpha/(1-alpha)*E)
     mat.strain = 0.5
     print(mat.strain, mat.stress, mat.tangent, mat.dampTangent)
     print(mat)

.. _print: https://docs.python.org/3/library/functions.html#print
