.. include:: sub.txt

========================
 rigidDiaphragm command
========================

.. function:: rigidDiaphragm(perpDirn, rNodeTag, *cNodeTags)

   Create a multi-point constraint between nodes.
   These objects will constrain certain degrees-of-freedom at the listed secondary nodes to move as if in a rigid plane with the primary (retained) node. To enforce this constraint, ``Transformation`` constraint handler is recommended. 

	      
   ========================   ===========================================================================
   ``perpDirn`` |int|         direction perpendicular to the rigid plane (i.e. direction 3 corresponds to the 1-2 plane)
   ``rNodeTag`` |int|         integer tag identifying the retained (primary) node
   ``cNodeTags`` |listi|      integar tags identifying the constrained (secondary) nodes
   ========================   ===========================================================================


