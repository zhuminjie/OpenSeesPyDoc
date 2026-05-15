.. include:: sub.txt

=====================
 getRetainedNodes command
=====================

.. function:: getRetainedNodes(nodeTag=None)

   Returns the master (retained) node tag(s) for multi-point constraints.

   The command retrieves master nodes associated with multi-point constraints (MP_Constraint)
   in the domain.

**Arguments**

   ========================   ===========================================================================
   ``nodeTag`` |int|          Optional. Constrained (slave) node tag to query.
                             If provided, returns the master node that constrains this slave node.
                             If omitted, returns all master nodes in the domain.
   ========================   ===========================================================================

**Return Value**

   - If called without arguments: Returns a list of all master (retained) node tags in the domain.
   - If called with a node tag: Returns a list containing the master node tag (e.g., ``[1]``) if the specified node is a constrained (slave) node. Returns an empty list ``[]`` if the node is not a constrained node.

**Notes**

   - The input `nodeTag` must be a **constrained (slave) node**. If a master node is provided, the command returns an empty list without an error message.
   - This command does not provide reverse lookup (i.e., finding all slave nodes constrained by a master node).

