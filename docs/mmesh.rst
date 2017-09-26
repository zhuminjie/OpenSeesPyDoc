Moving Mesh Method
==================

The moving mesh moves with the Lagrangian nodes.
The `Delaunay Triangulation in 2D`_ or
the `DT in 3D`_ will be constructed between
moving nodes and the `Alpha shape`_ will be found
to form the moving mesh.


.. _Delaunay Triangulation in 2D: https://www.cs.cmu.edu/~quake/triangle.html
.. _DT in 3D: http://wias-berlin.de/software/index.jsp?id=TetGen&lang=1
.. _Alpha shape: https://en.wikipedia.org/wiki/Alpha_shape

The moving mesh can be created for both structure and fluid.
There are several functions related to the moving mesh:


.. toctree::
   :maxdepth: 2

   mesh
   remesh
   region


