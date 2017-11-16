.. include:: sub.txt

Algorithm Object
=======================

.. class:: algorithm()

   A python :class:`algorithm` object
   is a wrapper to the OpenSees ``Algorithm`` object.

   .. note::
   
      One cannot create an :class:`algorithm` object
      directly, but only through the :ref:`algorithm-class-methods`.

      There is only one global :class:`algorithm` object.
      Creating another :class:`algorithm` object
      will automatically invalid the previous :class:`algorithm` objects.

.. _algorithm-class-methods:

Class methods
--------------

#. :meth:`algorithm.Linear`
#. :meth:`algorithm.Newton`
	       
.. classmethod:: algorithm.Linear(secant=False,initial=False,factorOnce=False)

   Create a Linear :class:`algorithm`.

   ================================   =============================================================
   ``secant`` |bool|                  Optional flag to indicate to use secant stiffness.
   ``initial`` |bool|                 Optional flag to indicate to use initial stiffness.
   ``factorOnce`` |bool|              Optional flag to indicate to only set up and factor matrix once.
   ================================   =============================================================

   As the tangent matrix typically will not change during the analysis in case of an elastic system it is highly advantageous to use the -factorOnce option. Do not use this option if you have a nonlinear system and you want the tangent used to be actual tangent at time of the analysis step.
   
.. classmethod:: algorithm.Newton(secant=False,initial=False,initialThenCurrent=False)

   Create a Newton :class:`algorithm`.

   ================================   =============================================================
   ``secant`` |bool|                  Optional flag to indicate to use secant stiffness.
   ``initial`` |bool|                 Optional flag to indicate to use initial stiffness.
   ``initialThenCurrent`` |bool|      Optional flag to indicate to use initial stiffness on first step, then use current stiffness for subsequent steps
   ================================   =============================================================


Examples
----------

::

   algorithm.Newton()


