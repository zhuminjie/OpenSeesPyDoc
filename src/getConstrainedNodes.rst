.. include:: sub.txt

=====================
 getConstrainedNodes command
=====================

.. function:: getConstrainedNodes()

   Returns all constrained (slave) node tags for multi-point constraints in the domain.

   The command retrieves all slave nodes associated with multi-point constraints (MP_Constraint)
   in the domain.

**Arguments**

   None.

**Return Value**

   Returns a list of all constrained (slave) node tags (e.g., ``[2, 5, 7]``) in the domain.
   Returns an empty list ``[]`` if no multi-point constraints exist.

**Notes**

   - This command does not accept any arguments. Calling with a node tag (e.g., ``getConstrainedNodes(2)``) returns an empty list.
   - To find the master node for a specific slave node, use ``getRetainedNodes(slaveNodeTag)``.

