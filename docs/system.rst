system
======

.. py:currentmodule:: opensees

.. py:function:: system(type[,*opt])

   create a LinearSOE and a LinearSolver object to solve the system of equations

   :param str type: system type, see :ref:`available system types <system-types>`
   :param opt: type specific options
   :type opt: list


.. _system-types:

Available system types

#. :ref:`PFEM-System`


.. _PFEM-System:

PFEM System
-----------


.. py:function:: system('PFEM'[,opt])
   :noindex:

   create a PFEM SOE and Solver

   :param str opt:
      * no option, use incompressible solver with `CSparse`_ package
      * ``'-umfpack'``, use incompressible solver with `UMFPACK`_ package
      * ``'-mumps'``, use incompressible solver with `MUMPS`_ package, it requires the parallel version
      * ``'-quasi'``, use quasi-incompressible solver with discrete pressure tangent stiffness matrix
      * ``'-quasi2'``, use quasi-incompressible solver with continuous pressure tangent stiffness matrix
      * ``'-quasi-mumps'``, use quasi-incompressible solver with discrete pressure tangent stiffness matrix and `MUMPS`_ package, it requires the parallel version




.. _CSparse: http://faculty.cse.tamu.edu/davis/suitesparse.html
.. _UMFPACK: http://faculty.cse.tamu.edu/davis/suitesparse.html
.. _MUMPS: http://mumps.enseeiht.fr/
