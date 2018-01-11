.. include:: sub.txt

==========================================
 elasticIsotropic class
==========================================

.. class:: elasticIsotropic(E, nu, rho=0.0)

   Create a ElasticIsotropic :class:`nDMaterial` object. A subclass of :class:`nDMaterial`.
   The material formulations for the ElasticIsotropic object are ``'ThreeDimensional'``, ``'PlaneStrain'``, ``'Plane Stress'``, ``'AxiSymmetric'`` and ``'PlateFiber'``.

   ========================   =============================================================
   ``E`` |float|              Tangent stiffness.
   ``nu`` |float|             Poisson's ratio.
   ``rho`` |float|            Mass density. (optional)
   ========================   =============================================================


   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`nDMaterial.strain`
     #. :attr:`nDMaterial.stress`
     #. :attr:`nDMaterial.tangent`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`

