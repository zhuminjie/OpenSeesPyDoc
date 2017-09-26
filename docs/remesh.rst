remesh
======

.. py:function:: remesh(alpha, numf, *frtags, numfi, *firtags)

   remesh nodes in :doc:`region` s to create new :doc:`element` s

   :param float alpha: the alpha parameter for `Alpha shape`_
   :param int numf: number of :doc:`region` s which contain freely moving nodes
   :param frtags: tags of above free regions
   :type frtags: list[int]
   :param int numfi: number of :doc:`region` s which contain fixed nodes
   :param firtags: tags of above fixed regions
   :type firtags: list[int]

   Element arguments:

   * PFEMElement2DBubble with ``'poly'`` mesh::

       eleargs = ['PFEMElement2DBubble',rho,mu,b1,b2,thk,kappa]

     where ``rho`` is fluid density, ``mu`` is fluid viscosity,
     ``b1`` and ``b2`` are
     body forces in x and y directions, ``thk`` is element thickness,
     and ``kappa`` is fluid bulk modulus.


   * PFEMElement2DQausi with ``'poly'`` mesh::

       eleargs = ['PFEMElement2DQausi',rho,mu,b1,b2,thk,kappa]

     where ``rho`` is fluid density, ``mu`` is fluid viscosity,
     ``b1`` and ``b2`` are
     body forces in x and y directions, ``thk`` is element thickness,
     and ``kappa`` is fluid bulk modulus.

   * Tri31 with ``'poly'`` mesh::

       eleargs = ['Tri31',thk,eletype,matTag,pressure, rho, b1, b2]

     where ``thk`` is element thickness, ``eletype`` is ``'PlaneStrain'``
     or ``'PlaneStress'``, ``matTag`` is a tag of :doc:`nDMaterial`,
     ``pressure`` is optional the uniform force on edge, ``rho`` is optional
     the solid density, and ``b1`` and ``b2`` are optional
     body forces in x and y directions.



.. _Alpha shape: https://en.wikipedia.org/wiki/Alpha_shape
