.. include:: sub.txt

NDMaterial Object
=======================

.. class:: NDMaterial()

   A python :class:`NDMaterial` object
   is a wrapper to the OpenSees ``NDMaterial`` object.

   .. note::
   
      One cannot create an :class:`NDMaterial` object
      directly, but only through :ref:`ndmat-class-methods`.


Object attributes
-------------------

#. :attr:`NDMaterial.tag`
#. :attr:`NDMaterial.strain`
#. :attr:`NDMaterial.stress`
#. :attr:`NDMaterial.tangent`

.. attribute:: NDMaterial.tag
      
   An object attribute (get) |int|.
   The tag of the :class:`NDMaterial` object.

   ::

      print(mat.tag)

.. attribute:: NDMaterial.strain
      
   An object attribute (get/set) |listf|.
   The material strains.

   ::

      mat.strain = [0.01,0.01]

.. attribute:: NDMaterial.stress

   An object attribute (get) |listf|.
   The material stress.

   ::

      print(mat.stress)

.. attribute:: NDMaterial.tangent

   An object attribute (get) |listl|.
   The material tangent at current strain.

   ::

      print(mat.tangent)


Object methods
-------------------

#. :meth:`NDMaterial.__str__`
#. :meth:`NDMaterial.remove`
		  
.. method:: NDMaterial.__str__()

   The string reprsentation of the :class:`NDMaterial`. Usually
   used in the |print| function.

   ::

      print(mat)

.. method:: NDMaterial.remove()

   Remove the corresponding OpenSees ``NDMaterial`` object.
   It will not remove the materials in :class:`element`.
	       
   .. seealso::

      :meth:`node.remove`


   ::

      mat.remove()

.. _ndmat-class-methods:

Class methods
--------------

#. :meth:`NDMaterial.ElasticIsotropic`

.. classmethod:: NDMaterial.ElasticIsotropic(E, nu, rho=0.0)

   Create a ElasticIsotropic :class:`NDMaterial` object.
   The material formulations for the ElasticIsotropic object are ``'ThreeDimensional'``, ``'PlaneStrain'``, ``'Plane Stress'``, ``'AxiSymmetric'`` and ``'PlateFiber'``.

   ========================   =============================================================
   ``E`` |float|              Tangent stiffness.
   ``nu`` |float|             Poisson's ratio.
   ``rho`` |float|            Mass density. (optional)
   ========================   =============================================================
		 
   ::

      mat = NDMaterial.ElasticIsotropic(E=1e6, nu=0.3)


