.. include:: sub.txt

.. _ReMesh:

================
 remesh command
================

.. function:: remesh(alpha=-1.0)

   * :math:`\alpha \ge 0` for updating moving mesh.
   * :math:`\alpha < 0` for updating background mesh.




   ========================   ===========================================================================
   ``alpha`` |float|          Parameter for the :math:`\alpha` method to construct a mesh
	                      from the node cloud of moving meshes. (optional)

			      * :math:`\alpha = 0` : no elements are created
			      * large :math:`\alpha` : all elements in the convex hull are created
			      * :math:`1.0 < \alpha < 2.0` : usually gives a good shape
   ========================   ===========================================================================
