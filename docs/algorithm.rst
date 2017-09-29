algorithm
==========

.. py:currentmodule:: opensees

.. py:function:: algorithm(type[,*opt])

   create an algorithm

   :param str type:  :ref:`algorithm types <algorithm-types>`
   :param opt: type specific options
   :type opt: list

.. _algorithm-types:

.. toctree::
   :maxdepth: 2
   :caption: Available algorithm types

   Linear-Algorithm
   Newton-Algorithm
   NewtonLineSearch-Algorithm
   ModifiedNewton-Algorithm
   KrylovNewton-Algorithm
   RaphsonNewton-Algorithm
   MillerNewton-Algorithm
   SecantNewton-Algorithm
   PeriodicNewton-Algorithm
   Broyden-Algorithm
   BFGS-Algorithm
	     




