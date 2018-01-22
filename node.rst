.. include:: sub.txt

============
 node func
============

.. function:: node(nodeTag, *crds, '-mass', *mass, '-disp', *disp, '-vel', *vel, '-accel', *accel, '-ndf', ndf)

   Create a OpenSees node.

   ========================   ===========================================================================
   ``nodeTag`` |int|          node tag.
   ``crds`` |listf|           nodal coordinates.
   ``mass`` |listf|           nodal mass.
   ``vel`` |listf|            nodal velocities.
   ``accel`` |listf|          nodal accelerations.
   ``ndf`` |float|            nodal ndf.
   ========================   ===========================================================================

