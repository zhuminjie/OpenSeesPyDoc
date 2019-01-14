.. include:: sub.txt

.. _BgMesh:

=================
 background mesh
=================

.. function:: mesh('bg',basicsize,*lower,*upper,'-tol',tol,'-wave',wavefilename,numl,*locations,'-numsub',numsub,'-fixed',numfnodes,*fNodes,'-structure',numsnodes,*sNodes)
   :noindex:

   Create a background mesh. Structural mesh must be created before
   the background mesh in order to be included.


   ========================   ===========================================================================
   ``basicsize`` |float|      basic mesh size
   ``lower`` |listf|          a list of coordinates of the lower point of the background region.
   ``upper`` |listf|          a list of coordinates of the uuper point of the background region.
   ``tol`` |float|            tolerance for boundary layers. (optional, default 1e-8)
   ``wavefilename`` |str|     a filename to record wave heights and velocities (optional)
   ``numl`` |int|             number of locations to record wave (optional)
   ``locations`` |listf|      coordinates of the locations (optional)
   ``numfnodes`` |int|        number of fixed nodes (optional)
   ``fNodes`` |listi|         a list of fixed nodes (optional)
   ``numsnodes`` |int|        number of structural nodes (optional)
   ``sNodes`` |listi|         a list of structural nodes (optional)
   ========================   ===========================================================================
