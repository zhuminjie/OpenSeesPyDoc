integrator
==========

.. py:currentmodule:: opensees

.. py:function:: integrator(type[,*opt])

   create an integrator

   :param string type: integrator type, see :ref:`available static integrator <static-integrator-types>` and :ref:`available dynamic integrator <dynamic-integrator-types>`
   :param opt: type specific options
   :type opt: list


.. _static-integrators:
      
Static Integrators
------------------

.. _static-integrator-types:

Available static integrator types

#.


.. _dynamic-integrators:

Dynamic Integrators
-------------------

.. _dynamic-integrator-types:

Available dynamic integrator types

#. :ref:`PFEM-Integrator`

      
.. _PFEM-Integrator:

PFEM Integrator
^^^^^^^^^^^^^^^

.. py:function:: integrator('PFEM')
   :noindex:

   create a PFEM integrator
   
   

