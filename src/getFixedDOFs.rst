.. include:: sub.txt

=====================
 getFixedDOFs command
=====================

.. function:: getFixedDOFs(nodeTag)

Returns a list of fixed DOF numbers for a specified node.

   The command retrieves all single-point constraints (SP_Constraint) applied to the given node
   and returns the DOF numbers that are fixed.

**Arguments**

   ========================   ===========================================================================
   ``nodeTag`` |int|          Node tag to query.
   ========================   ===========================================================================

**Return Value**

   A list of integers containing the fixed DOF numbers (1-based) for the specified node.
   Returns an empty list if the node has no fixed DOFs or the node does not exist.

