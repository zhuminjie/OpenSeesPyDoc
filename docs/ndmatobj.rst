.. include:: sub.txt

==========================================
 nDMaterial -- Multi Dimentional Material
==========================================

.. class:: nDMaterial()

   A subclass of :class:`tagged`
   and a base class for NDMaterial objects.

   One cannot create an :class:`NDMaterial` object
   directly, but only through its subclasses.

   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`NDMaterial.strain`
     #. :attr:`NDMaterial.stress`
     #. :attr:`NDMaterial.tangent`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`

Following are  available subclasses in the OpenSees:

.. toctree::
   :maxdepth: 2
      

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


