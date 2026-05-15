.. include:: sub.txt

=====================
 getRetainedDOFs command
=====================

.. function:: getRetainedDOFs(nodeTag)

   Returns the retained (master) DOF numbers for a multi-point constraint.

   The command retrieves the DOF numbers on the master node that participate in
   the constraint.

**Arguments**

   ========================   ===========================================================================
   ``nodeTag`` |int|          **Master (retained) node** tag to query.
   ========================   ===========================================================================

**Return Value**

   A list of integers containing the retained DOF numbers (1-based) on the master node.
   Returns an empty list if the node is not a master node or has no constraints.

