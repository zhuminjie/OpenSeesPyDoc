test
====

.. py:currentmodule:: opensees

.. py:function:: test(type[,*opt])

   create a convergence test object

   :param str type: test type, see :ref:`available test types <test-types>`
   :param opt: type specific options
   :type opt: list


.. _test-types:

Available convergence test types

#. :ref:`PFEM-Test`


.. _PFEM-Test:

PFEM Test
---------


.. py:function:: test('PFEM', tolv, tolp, tolrv, tolrp, tolvrel, tolprel, maxIter[, maxIncr[, printFlag[, normType]]])
   :noindex:

   create a PFEM convergence test object

   :param float tolv, tolp: The tolerance for absolute values of velocity and pressure.
   :param float tolrv, tolrp: The tolerance for residual of velocity and pressure equations.
   :param float tolvrel, tolprel: The tolerance for relative values of velocity and pressure.
   :param int maxIter: The maximum number interations.
   :param int maxIncr: the maximum number that errors increase.
   :param int printFlag: Flag for printing messages (default is 0 -- print nothing).
   :param int normType: which norm is used (default is 2).
