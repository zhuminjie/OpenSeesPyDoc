.. include:: sub.txt

==============
 node command
==============

.. function:: node(nodeTag, *crds, '-mass', *mass, '-disp', *disp, '-vel', *vel, '-accel', *accel, '-ndf', ndf)

   Create a OpenSees node.

   ========================   ===========================================================================
   ``nodeTag`` |int|          node tag.
   ``crds`` |listf|           nodal coordinates.
   ``mass`` |listf|           nodal mass. (optional)
   ``vel`` |listf|            nodal velocities. (optional)
   ``accel`` |listf|          nodal accelerations. (optional)
   ``ndf`` |float|            nodal ndf. (optional)
   ========================   ===========================================================================

