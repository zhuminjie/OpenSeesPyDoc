.. include:: sub.txt

transformation 
=====================================================

.. class:: transformation()

   Create a transformation constraint handler. A subclass of :class:`handler`.

   * The :class:`sp` constraints when using the transformation method are done directly. The matrix equation is not manipulated to enforce them, rather the trial displacements are set directly at the nodes at the start of each analysis step.
   * Great care must be taken when :class:`mp` constraints are being enforced as the transformation method does not follow constraints:
      
     #. If a :class:`node` is fixed, constrain it with the :meth:`node.fix` command and not :meth:`node.equalDOF` or other type of constraint.
     #. If :class:`mp` are constrained, make sure that the retained node is not constrained in any other constraint.

   And remember if a node is constrained to multiple nodes in your model it probably means you have messed up.



