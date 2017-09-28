algorithm
==========

.. py:currentmodule:: opensees

.. py:function:: algorithm(type[,*opt])

   create an algorithm

   :param str type:  :ref:`algorithm types <algorithm-types>`
   :param opt: type specific options
   :type opt: list

.. _algorithm-types:

Available algorithm types

#. :ref:`Linear-Algorithm`
#. :ref:`Newton-Algorithm`
#. :ref:`NewtonLineSearch-Algorithm`
#. :ref:`ModifiedNewton-Algorithm`
#. :ref:`KrylovNewton-Algorithm`
#. :ref:`RaphsonNewton-Algorithm`
#. :ref:`MillerNewton-Algorithm`
#. :ref:`SecantNewton-Algorithm`
#. :ref:`PeriodicNewton-Algorithm`
#. :ref:`Broyden-Algorithm`
#. :ref:`BFGS-Algorithm`

      
.. _Linear-Algorithm:

Linear-Algorithm
----------------

.. py:function:: algorithm( 'Linear' )




.. _Newton-Algorithm:

Newton-Algorithm
----------------

.. py:function:: algorithm( 'Newton' )




.. _NewtonLineSearch-Algorithm:

NewtonLineSearch-Algorithm
--------------------------

.. py:function:: algorithm( 'NewtonLineSearch' )



.. _ModifiedNewton-Algorithm:

ModifiedNewton-Algorithm
------------------------

.. py:function:: algorithm( 'ModifiedNewton' )



.. _KrylovNewton-Algorithm:

KrylovNewton-Algorithm
-----------------------

.. py:function:: algorithm( 'KrylovNewton' )



.. _RaphsonNewton-Algorithm:

RaphsonNewton-Algorithm
-------------------------

.. py:function:: algorithm( 'RaphsonNewton' )



.. _MillerNewton-Algorithm:

MillerNewton-Algorithm
-----------------------

.. py:function:: algorithm( 'MillerNewton' )



.. _SecantNewton-Algorithm:

SecantNewton-Algorithm
-----------------------

.. py:function:: algorithm( 'SecantNewton' )



.. _PeriodicNewton-Algorithm:

PeriodicNewton-Algorithm
------------------------

.. py:function:: algorithm( 'PeriodicNewton' )



.. _Broyden-Algorithm:

Broyden-Algorithm
------------------

.. py:function:: algorithm( 'Broyden' )



.. _BFGS-Algorithm:

BFGS-Algorithm
----------------

.. py:function:: algorithm( 'BFGS' )


