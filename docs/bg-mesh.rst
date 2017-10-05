Background subcommands for meshing
==================================

.. py:currentmodule:: opensees

These are subcommands to set up the background mesh domain and boundaries.

#. :ref:`bg-meshsize`
#. :ref:`bg-variableMesh`
#. :ref:`bg-fix`

.. _bg-meshsize:

meshsize
---------

.. py:function:: background('meshsize', size)
   :noindex:
   
   set the basic mesh size and domain size for background mesh, must be called before other subcommands

   :param float size: mesh size


.. _bg-variableMesh:

variableMesh
-------------

.. py:function:: background('variableMesh', level, *lower, *upper)
   :noindex:
   
   set up an area with variable mesh size

   :param int level: the highest level for coarser mesh sizes, :math:`h = \frac{h_0}{2^{level}}`.
   :param lower: coordinates of lower point of the variable mesh domain
   :type lower: list[float]
   :param upper: coordinates of  upper point of the variable mesh domain
   :type upper: list[float]

.. _bg-fix:

fix
----

.. py:function:: background('fix', btype, *range, *args)
   :noindex:
   
   set up the boundary condition for the background mesh

   :param str btype: the boundary type
      
      * ``'p'`` -- a point
      * ``'x'`` -- a line along x axis
      * ``'y'`` -- a line along y axis
      * ``'rect'`` -- a rectangular area
   :param range: the range of the boundary
      
      * ``'p'`` -- ``range = [*pcoords]``, ``pcoords`` is the coordinate of the point
      * ``'x'`` -- ``range = [x, y1, y2]``, ``x`` is the x coordinate of the line and ``y1, y2`` is the starting and end point the line
      * ``'y'`` -- ``range = [y, x1, x2]``, ``y`` is the y coordinate of the line and ``x1, x2`` is the starting and end point the line
      * ``'rect'`` -- ``range = [*lower, *upper]``, lower and upper coordinates of the rectangle
   :type range: list[float]
   :param args: the fixity for fixed boundary or values for velocity and pressure boundaries
      
      * fixed boundary -- ``args`` is a list of 1 and 0
      * velocity boundary -- ``args = ['-vel', *vals]``, ``vals`` is a list velocity values
      * pressure boundary -- ``args = ['-pressure', p]``, ``p`` is the pressure values
   :type upper: list


