Background subcommands for recorders
====================================

.. py:currentmodule:: opensees

   
These are the subcommands to create recorders.

#. :ref:`bg-pvdRecorder`
#. :ref:`bg-nodeRecorder`
#. :ref:`bg-waveRecorder`


      

.. _bg-pvdRecorder:

pvdRecorder
-----------

.. py:function:: background('pvdRecorder', *args)
   :noindex:

   create the pvd recorder for background mesh

   :param args: same as in :ref:`PVD-Recorder`
   :type args: list


.. _bg-nodeRecorder:

nodeRecorder
------------

.. py:function:: background('nodeRecorder', *args)
   :noindex:
   

   create the node recorder for background mesh

   :param args: same as in :ref:`Node-Recorder`
   :type args: list


.. _bg-waveRecorder:

waveRecorder
------------

.. py:function:: background('waveRecorder', filename[, '-dT', dT[, *locs]])
   :noindex:

   create the wave recorder for background mesh to record wave height and velocity, as well as the time steps and number iterations.
   
   :param str filename: the filename for wave recorder
   :param float dT: the minimum time step to record
   :param locs: the coordinats of locations to record wave height and velocity
   :type locs: list[float]

