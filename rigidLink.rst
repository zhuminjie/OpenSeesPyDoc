.. include:: sub.txt

=====================
 rigidLink func
=====================

.. function:: rigidLink(type, masterNodeTag, slaveNodeTag)

   Create MP constraints.

   ============================   ===========================================================================
   ``type`` |str|                 type:

                                  * ``'bar'`` translational constraints
				  * ``'beam'`` translational and rotational constraints
   ``masterNodeTag`` |int|        master node
   ``slaveNodeTag`` |int|         slave node
   ============================   ===========================================================================

