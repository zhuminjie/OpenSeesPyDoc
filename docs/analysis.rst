analysis
========

.. py:currentmodule:: opensees

.. py:function:: analysis(type[,*opt])

   create an analysis

   :param str type: analysis type, see :ref:`available types <analysis-types>`
   :param opt: type specific options
   :type opt: list

.. _analysis-types:

Available analysis types

#. :ref:`Static-Analysis`
#. :ref:`Transient-Analysis`
#. :ref:`VariableTransient-Analysis`
#. :ref:`PFEM-Analysis`

      
.. _Static-Analysis:

Static Analysis
---------------

.. py:function:: analysis( 'Static' )
   :noindex:


   create a static analysis



.. _Transient-Analysis:


Transient Analysis
------------------
		 

.. py:function:: analysis( 'Transient' )
   :noindex:

   create a dynamic analysis with constant time step




.. _VariableTransient-Analysis:

VariableTransient Analysis
--------------------------

.. py:function:: analysis( 'VariableTransient' )
   :noindex:

   create a dynamic analysis with variable time step

   


.. _PFEM-Analysis:

PFEM Analysis
-------------


.. py:function:: analysis('PFEM', dtmax, dtmin, gravity[, ratio])
   :noindex:

   create a dynamic FSI analysis using Particle Finite Element Method (PFEM).

   :param float dtmax: maximum time step
   :param float dtmin: minimum time step
   :param float gravity: the gravity acceleration for fly-out nodes, up is positive.
   :param float ratio: the ratio for automatic reducing time step size (optional)

