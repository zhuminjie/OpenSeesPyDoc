.. include:: sub.txt

plainHandler -- Handle homogeneous constraints
==============================================

.. class:: plainHandler()

   Create a plain constraint handler. A subclass of :class:`handler`.

   It can only enforce homogeneous :class:`sp` constraints (:meth:`node.fix`)
   and :class:`mp` constraints constructed where the constraint
   matrix is equal to the identity (:meth:`node.equalDOF`).
