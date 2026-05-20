.. include:: sub.txt

=====================
 getConstrainedDOFs command
=====================

.. function:: getConstrainedDOFs(nodeTag)

   Returns the constrained (slave) DOF numbers for a multi-point constraint.

   The command retrieves the DOF numbers on the slave node that are constrained
   by a master node.

**Arguments**

   ========================   ===========================================================================
   ``nodeTag`` |int|          **Constrained (slave) node** tag to query.
   ========================   ===========================================================================

**Return Value**

   A list of integers containing the constrained DOF numbers (1-based) on the slave node.
   Returns an empty list ``[]`` if the node is not a slave node or has no constraints.

**Notes**

   - DOF numbers are 1-based (1, 2, 3 correspond to X, Y, Z translations in 2D).
   - This command requires a **slave node** as input.


