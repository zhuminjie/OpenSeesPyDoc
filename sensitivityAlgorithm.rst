.. include:: sub.txt

==============================
 sensitivityAlgorithm command
==============================

.. function:: sensitivityAlgorithm(type)

   This command is used to create a sensitivity algorithm.

   ========================   =============================================================
   ``type`` |str|             the type of the sensitivity algorithm,

                              * ``'-compuateAtEachStep'``  automatically compute
				at the end of each step
			      * ``'-compuateByCommand'``  compute by
				calling ``computeGradients``.
   ========================   =============================================================


