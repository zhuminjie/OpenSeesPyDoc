.. include:: sub.txt

===============
 particle mesh
===============

.. function:: mesh('part',tag,type,*pArgs,eleType='',*eleArgs=[], '-vel', *vel0, '-pressure', p0)
   :noindex:

   Create a particle mesh which is used for background mesh.


   ========================   ===========================================================================
   ``tag`` |int|              mesh tag.
   ``type`` |str|             type of the mesh, ``'quad'``, ``'tri'``, ``'line'``, ``'point'``
   ``pArgs`` |listf|          coordinates of points defining the mesh region
      
                              * ``'quad'`` : [x1, y1, x2, y2, x3, y3, x4, y4]
                              * ``'tri'`` : [x1, y1, x2, y2, x3, y3]
                              * ``'line'`` : [x1, y1, x2, y2]
                              * ``'point'`` : [x1, y1]
   ``eleType`` |str|          the element type, (optional)

                              * ``'PFEMElement2DBubble'``
			      * ``'PFEMElement2DQuasi'``
			      * ``'tri31'``

			      if no type is given, only nodes are created
			      
   ``eleArgs`` |list|         a list of element arguments. (optional)
   ``vel0`` |listf|           a list of initial velocities. (optional)
   ``p0`` |float|             initial pressure. (optional)
   ========================   ===========================================================================

