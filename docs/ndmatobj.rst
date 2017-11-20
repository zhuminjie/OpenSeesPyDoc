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

.. attribute:: NDMaterial.tag
      
   An object attribute (get) |int|.
   The tag of the :class:`NDMaterial` object.

.. attribute:: NDMaterial.strain
      
   An object attribute (get/set) |listf|.
   The material strains.

.. attribute:: NDMaterial.stress

   An object attribute (get) |listf|.
   The material stress.

.. attribute:: NDMaterial.tangent

   An object attribute (get) |listl|.
   The material tangent at current strain.


Object methods
-------------------

#. :meth:`NDMaterial.__str__`
#. :meth:`NDMaterial.remove`
		  
.. method:: NDMaterial.__str__()

   The string reprsentation of the :class:`NDMaterial`. Usually
   used in the |print| function.

.. method:: NDMaterial.remove()

   Remove the corresponding OpenSees ``NDMaterial`` object.
   It will not remove the materials in :class:`element`.
	       
   .. seealso::

      :meth:`node.remove`


.. _ndmat-class-methods:

Class methods
--------------

#. :meth:`NDMaterial.ElasticIsotropic`

.. classmethod:: NDMaterial.ElasticIsotropic(tag, E, nu, rho=0.0)

   Create a ElasticIsotropic :class:`NDMaterial` object.
   The material formulations for the ElasticIsotropic object are ``'ThreeDimensional'``, ``'PlaneStrain'``, ``'Plane Stress'``, ``'AxiSymmetric'`` and ``'PlateFiber'``.

   ========================   =============================================================
   ``tag`` |int|              :class:`NDMaterial` tag.
   ``E`` |float|              Tangent stiffness.
   ``nu`` |float|             Poisson's ratio.
   ``rho`` |float|            Mass density. (optional)
   ========================   =============================================================

Examples
----------

::

     mat = NDMaterial.ElasticIsotropic(1, E=1e6, nu=0.3)
     print(mat.strain, mat.stress, mat.tangent)
     print(mat)

