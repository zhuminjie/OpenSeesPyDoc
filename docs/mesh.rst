mesh
====

.. py:currentmodule:: opensees

.. py:function:: mesh(type, regTag, ndf, h, num, *nds, *bounds[, *eleargs])

   mesh a geometry to :doc:`node` s and :doc:`element` s

   :param str type: mesh type, see :ref:`available types <mesh-types>`
   :param int regTag: tag of :doc:`region` to be created to store new nodes and elements
   :param int ndf: number of degrees of freedoms for new nodes
   :param float h: mesh size
   :param int num: number of predefined nodes to define the geometry.
   :param nds: tags of predefined :doc:`node` s
   :type nds: list[int]
   :param bounds: 1 or 0 indicates if boundaries of the geometry are included.
   :type bounds: list[int]
   :param eleargs: element arguments, see :ref:`available line elements <line-eleargs>` and :ref:`available triangular elements <tri-eleargs>`
   :type eleargs: list


.. _mesh-types:

Available mesh types

#. :ref:`Line-Mesh`
#. :ref:`Tri-Mesh`

.. _Line-Mesh:

Line Mesh
---------

.. py:function:: mesh('line', regTag, ndf, h, num, *nds, *bounds[, *eleargs])
   :noindex:

   mesh a geometric line to :doc:`node` s and :doc:`element` s

   :param int num: number of predefined nodes to define the geometric line.
      :doc:`node` s are given from start to end of lines. The end :doc:`node`
      will not be connected to the starting node. 
   :param bounds: 1 or 0 indicates if end points of the line are included.
   :type bounds: list[int]
   :param eleargs: element arguments, if no elements are given, only nodes are created, see :ref:`available line elements <line-eleargs>`
   :type eleargs: list

.. _line-eleargs:

Available line elements

* elasticBeamColumn ::

    eleargs = ['elasticBeamColumn',A,E,Iz,transfTag,*opts]

  where ``A`` is cross section area, ``E`` is elastic modulus,
  ``Iz`` is second moment of area about the local z-axis,
  ``transfTag`` is a tag of :doc:`geomTransf`,
  ``opts`` is an optional list of optional options::

    opts = ['-mass', mass, '-cMass']

  where ``mass`` is element mass per unit length and ``-cMass``
  is to form consistent mass matrix.


* forceBeamColumn ::

    eleargs = ['forceBeamColumn',transfTag,intTag,*opts]

  where ``transfTag`` is a tag of :doc:`geomTransf`,
  ``intTag`` is a tag of :doc:`beamIntegration`,
  ``opts`` is an optional list of optional options::

    opts = ['-mass', mass, '-iter', maxIter, tol]

  where ``mass`` is element mass per unit length,
  ``maxIter`` is maximum number of
  iterations to undertake to satisfy element
  compatibility (optional, default=10) and ``tol``
  is tolerance for satisfaction of
  element compatibility (optional, default=10e-12)


* dispBeamColumn ::

    eleargs = ['dispBeamColumn',transfTag,intTag,*opts]

  where ``transfTag`` is a tag of :doc:`geomTransf`,
  ``intTag`` is a tag of :doc:`beamIntegration`,
  ``opts`` is an optional list of optional options::

    opts = ['-mass', mass, '-cMass']

  where ``mass`` is element mass per unit length and ``-cMass``
  is to form consistent mass matrix.



       
.. _Tri-Mesh:

Triangular Mesh
---------------

.. py:function:: mesh('tri', regTag, ndf, h, num, *nds, *bounds[, *eleargs])
   :noindex:

   mesh a geometric polygon to :doc:`node` s and :doc:`element` s

   :param int num: nodes are given in one direction of a polygon. The end node will be automatically connected to the starting node.
   :param bounds: 1 or 0 indicates if edges of the polygon are included.
   :type bounds: list[int]
   :param eleargs: element arguments, if no elements are given, only nodes are created, see :ref:`available triangular elements <tri-eleargs>`
   :type eleargs: list

.. _tri-eleargs:

Available triangular elements


* PFEMElement2DBubble::

    eleargs = ['PFEMElement2DBubble',rho,mu,b1,b2,thk,kappa]

  where ``rho`` is fluid density, ``mu`` is fluid viscosity,
  ``b1`` and ``b2`` are
  body forces in x and y directions, ``thk`` is element thickness,
  and ``kappa`` is fluid bulk modulus.


* PFEMElement2DQuasi::

    eleargs = ['PFEMElement2DQuasi',rho,mu,b1,b2,thk,kappa]

  where ``rho`` is fluid density, ``mu`` is fluid viscosity,
  ``b1`` and ``b2`` are
  body forces in x and y directions, ``thk`` is element thickness,
  and ``kappa`` is fluid bulk modulus.

* PFEMElement2DQausi2::

    eleargs = ['PFEMElement2DQuasi2',rho,mu,b1,b2,thk,kappa]

  where ``rho`` is fluid density, ``mu`` is fluid viscosity,
  ``b1`` and ``b2`` are
  body forces in x and y directions, ``thk`` is element thickness,
  and ``kappa`` is fluid bulk modulus.

* TaylorHood2D::

    eleargs = ['TaylorHood2D',rho,mu,b1,b2,thk,kappa]

  where ``rho`` is fluid density, ``mu`` is fluid viscosity,
  ``b1`` and ``b2`` are
  body forces in x and y directions, ``thk`` is element thickness,
  and ``kappa`` is fluid bulk modulus.

* Tri31::

    eleargs = ['Tri31',thk,eletype,matTag,pressure, rho, b1, b2]

  where ``thk`` is element thickness, ``eletype`` is ``'PlaneStrain'``
  or ``'PlaneStress'``, ``matTag`` is a tag of :doc:`nDMaterial`,
  ``pressure`` is optional the uniform force on edge, ``rho`` is optional
  the solid density, and ``b1`` and ``b2`` are optional
  body forces in x and y directions.


