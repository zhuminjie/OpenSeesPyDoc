.. include:: sub.txt

.. _ReMesh:
   
================
 remesh command
================

.. function:: remesh(alpha=-1.0)

   Update the mesh with ``id <= 0``.


   ========================   ===========================================================================
   ``alpha`` |float|          Parameter for the :math:`\alpha` method to construct a mesh
	                      from the node cloud of all meshes.
	                      :math:`\alpha \ge 0`. (optional)

			      * :math:`\alpha = 0` : no elements are created
			      * large :math:`\alpha` : all elements in the convex hull are created
			      * :math:`1.0 \lt \alpha \lt 2.0` : usually gives a good shape
   ========================   ===========================================================================

