.. include:: sub.txt

.. _BgMesh:

=================
 background mesh
=================

.. function:: mesh('bg',basicsize,*lower,*upper,'-tol',tol,'-meshtol',meshtol,'-wave',wavefilename,numl,*locations,'-numsub',numsub,'-structure',id,numnodes,*snodes)
   :noindex:

   Create a background mesh. 


   ========================   ===========================================================================
   ``basicsize`` |float|      basic mesh size
   ``lower`` |listf|          a list of coordinates of the lower point of the background region.
   ``upper`` |listf|          a list of coordinates of the uuper point of the background region.
   ``tol`` |float|            tolerance for intri check. (optional, default 1e-10)
   ``meshtol`` |float|        tolerance for cell boundary check. (optional, default 0.1)
   ``wavefilename`` |str|     a filename to record wave heights and velocities (optional)
   
                              the recorded data are in the following format for columns:

                              ``time vx vy <vz> xmin xmax ymin ymax <zmin zmax> dt``
   ``numl`` |int|             number of locations to record wave (optional)
   ``locations`` |listf|      coordinates of the locations (optional)
   ``id`` |int|               structural id used to identify FSI and SSI (solid-solid-interaction)
   
                              * ``id`` = 0 : ignore the structure
                              * ``id`` > 0 : both FSI and SSI
                              * ``id`` < 0 : only SSI

   ``numsnodes`` |int|        number of structural nodes (optional)
   ``sNodes`` |listi|         a list of structural nodes (optional)
   ========================   ===========================================================================
