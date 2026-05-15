.. include:: sub.txt

=====================
 getFixedNodes command
=====================

.. function:: getFixedNodes()

   Returns a list of node tags that are fixed (via the ``fix`` command) in the domain.

   The command iterates over all single-point constraints (SP_Constraint) in the domain,
   extracts the node tags, sorts them, and removes duplicates.

   **Return Value**

   A list of integers containing the tags of nodes that have at least one fixed DOF.
   Returns an empty list if no fixed nodes are found.
