.. include:: sub.txt

==================
 equalDOF command
==================

.. function:: equalDOF(rNodeTag, cNodeTag, *dofs)

   Create a multi-point constraint between nodes.

	      
   ========================   ===========================================================================
   ``rNodeTag`` |int|         integer tag identifying the retained, or primary node.
   ``cNodeTag`` |int|         integer tag identifying the constrained, or secondary node.
   ``dofs`` |listi|           nodal degrees-of-freedom that are constrained at the
	                      cNode to be the same as those at the rNode
			      Valid range is from 1 through
			      ndf, the number of nodal degrees-of-freedom.
   ========================   ===========================================================================


