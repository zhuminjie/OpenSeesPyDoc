mesh
====

.. py:function:: mesh(type, regTag, ndf, h, num, *nds, *bounds[, *eleargs])

   mesh a geometry to FE :doc:`node` s and :doc:`element` s

   :param str type: 'line' for line mesh; 'poly' for trangular mesh
   :param int regTag: tag of :doc:`region` to be created to store new nodes and elements
   :param int ndf: number of degrees of freedoms for new nodes
   :param float h: mesh size
   :param int num: number of predefined nodes to define the geometry. For line mesh, nodes are given from start to end of lines. The end node will not be connected to the starting node. For poly mesh, nodes are given in one direction of a polygon. The end node will be automatically connected to the starting node.
   :param nds: tags of predefined nodes
   :type nds: list[int]
   :param bounds: 1 or 0 indicates if the edge of a polygon or end point of a line is included.
   :type bounds: list[int]
   :param eleargs: see below for available elements
   :type eleargs: list

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

   * elasticBeamColumn with ``'line'`` mesh::

       eleargs = ['elasticBeamColumn',A,E,Iz,transfTag,*opts]

     where ``A`` is cross section area, ``E`` is elastic modulus,
     ``Iz`` is second moment of area about the local z-axis,
     ``transfTag`` is a tag of :doc:`geomTransf`,
     ``opts`` is an optional list of optional options::

       opts = ['-mass', mass, '-cMass']

     where ``mass`` is element mass per unit length and ``-cMass``
     is to form consistent mass matrix.


   * forceBeamColumn with ``'line'`` mesh::

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


   * dispBeamColumn with ``'line'`` mesh::

       eleargs = ['dispBeamColumn',transfTag,intTag,*opts]

     where ``transfTag`` is a tag of :doc:`geomTransf`,
     ``intTag`` is a tag of :doc:`beamIntegration`,
     ``opts`` is an optional list of optional options::

       opts = ['-mass', mass, '-cMass']

     where ``mass`` is element mass per unit length and ``-cMass``
     is to form consistent mass matrix.
