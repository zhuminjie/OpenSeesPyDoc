.. include:: sub.txt

===============
 particle mesh
===============

.. function:: mesh('part',tag,type,*pArgs,eleType='',*eleArgs=[], '-vel', *vel0, '-pressure', p0)
   :noindex:

   Create a particle mesh which is used for background mesh.


   ========================   ===========================================================================
   ``tag`` |int|              mesh tag.
   ``type`` |str|             type of the mesh
   ``pArgs`` |listf|          coordinates of points defining the mesh region

                              * ``'quad'`` : [x1, y1, x2, y2, x3, y3, x4, y4, nx, ny]
			      
				Coordinates of four corners.
			      
			      * ``'cube'`` : [x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4,
				              z4, x5, y5, z5, x6, y6, z6, x7, y7, z7, x8,
				              y8, z8, nx, ny, nz]
				
				Coordinates of four corners at bottom and at top
			      * ``'tri'`` : [x1, y1, x2, y2, x3, y3, nx, ny]
			      
				Coordinates of three corners
                              * ``'line'`` : [x1, y1, x2, y2, nx]
			      
				Coordinates of two ends
                              * ``'point'`` : [x1, y1]
			      
				Coordinates of the point

			      ``nx``, ``ny``, ``nz`` are number of particles in x, y, and z directions
			      
   ``eleType`` |str|          the element type, (optional)

                              * :doc:`PFEMElementBubble`
			      * :doc:`PFEMElementCompressible`
			      * :doc:`tri31`

			      if no type is given, only nodes are created
			      
   ``eleArgs`` |list|         a list of element arguments. (optional, see :doc:`linemesh` and :doc:`trimesh`)
   ``vel0`` |listf|           a list of initial velocities. (optional)
   ``p0`` |float|             initial pressure. (optional)
   ========================   ===========================================================================

