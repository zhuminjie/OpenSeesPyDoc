.. include:: sub.txt

Constraints Object
=======================

.. class:: constraints()

   A python :class:`constraints` object
   is a wrapper to the OpenSees ``ConstraintHandler`` object.

   .. note::
   
      One cannot create an :class:`constraints` object
      directly, but only through the :ref:`constraints-class-methods`.

      There is only one global :class:`constraints` object.
      Creating another :class:`constraints` object
      will automatically invalidate the previous :class:`constraints` objects.

.. _constraints-class-methods:

Class methods
--------------

#. :meth:`constraints.Plain`
#. :meth:`constraints.Penalty`
#. :meth:`constraints.Lagrange`
#. :meth:`constraints.Transformation`
	       
.. classmethod:: constraints.Plain()

   Create a Plain :class:`constraints`.

   It can only enforce homogeneous :class:`sp` constraints (:meth:`model.fix`)
   and :class:`mp` constraints constructed where the constraint
   matrix is equal to the identity (:meth:`model.equalDOF`).

.. classmethod:: constraints.Penalty(alphaS, alphaM)

   Create a Penalty :class:`constraints`.

   ========================   =============================================================
   ``alphaS`` |float|         Penalty :math:`\alpha_S` factor on :class:`sp` constraints.
   ``alphaM`` |float|         Penalty :math:`\alpha_M` factor on :class:`mp` constraints.
   ========================   =============================================================

   The degree to which the constraints are enforced is dependent on the penalty values chosen. Problems can arise if these values are too small (constraint not enforced strongly enough) or too large (problems associated with conditioning of the system of equations).

.. classmethod:: constraints.Lagrange(alphaS=1.0, alphaM=1.0)

   Create a Lagrange Multipliers :class:`constraints`.

   ========================   ================================================================
   ``alphaS`` |float|         Penalty :math:`\alpha_S` factor on :class:`sp` constraints.
		              (optional)
   ``alphaM`` |float|         Penalty :math:`\alpha_M` factor on :class:`mp` constraints.
		              (optional)
   ========================   ================================================================

   The Lagrange multiplier method introduces new unknowns to the system of equations. The diagonal part of the system corresponding to these new unknowns is 0.0. This ensure that the system IS NOT symmetric positive definite.

.. classmethod:: constraints.Transformation()

   Create a Transformation :class:`constraints`.

   * The :class:`sp` constraints when using the transformation method are done directly. The matrix equation is not manipulated to enforce them, rather the trial displacements are set directly at the nodes at the start of each analysis step.
   * Great care must be taken when :class:`mp` constraints are being enforced as the transformation method does not follow constraints:
      
     #. If a :class:`node` is fixed, constrain it with the :meth:`model.fix` command and not :meth:`model.equalDOF` or other type of constraint.
     #. If :class:`mp` are constrained, make sure that the retained node is not constrained in any other constraint.

   And remember if a node is constrained to multiple nodes in your model it probably means you have messed up.

   
