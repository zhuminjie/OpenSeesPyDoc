recorder
========

.. py:currentmodule:: opensees
   
.. py:function:: recorder(type[,*opt])

   create an recorder

   :param str type: recorder type, see :ref:`available types <recorder-types>`
   :param opt: type specific options
   :type opt: list



.. _recorder-types:

Available recorder types

#. :ref:`Node-Recorder`
#. :ref:`Element-Recorder`
#. :ref:`PVD-Recorder`

.. _Node-Recorder:

Node Recoder
------------

.. py:function:: recorder('Node'[, *opts], respType)
   :noindex:

   create a recorder to record nodal information

   :param opts: list of optional arguments, options can be mixed

      * ``'-node', *nds(list[int])``, tags of nodes to be recorded
      * ``'-nodeRange', startNode(int), endNode(int)``, starting and end node tag
      * ``'-region', regTag(int)``, tag of a region whose nodes to be recorded
      * ``'-dof', *dofs(list[int])``, dofs to be recorded
      * ``'-file', filename(str)``, save data in text format
      * ``'-csv', filename(str)``, save data in csv format
      * ``'-xml', filename(str)``, save data in xml format
      * ``'-binary', filename(str)``, save data in binary format
      * ``'-fileAdd', filename(str)``, append data to file
      * ``'-time'`` or ``'-load'``, include the doman time in first entry of each data line
      * ``'-dT'``, time interval for recording
      * ``'-scientific'``, use scientific form for data
      * ``'-precision', precision``, data precision
      * ``'-closeOnWrite'``, close the file after every time step
      * ``'-tcp', inetAddr(str), port(int)``, send date to remote machine with ip address ``inetAddr`` and port number ``port``
   :type opts: list
   :param str respType: a string indicating response required

      * ``'disp'``, displacement
      * ``'vel'``, velocity
      * ``'accel'``, acceleration
      * ``'incrDisp'``, incremental displacement
      * ``'incrDeltaDisp'``, incremental displacement in iterations
      * ``'unbalance'``, unbalance forces
      * ``'unbalanceIncInertia'``, unbalance dynamic forces
      * ``'eigen i'``, eigenvector for mode i
      * ``'reaction'``, nodal reaction
      * ``'reactionIncInertia'``, nodal dynamic reaction
      * ``'rayleighForces'``, damping forces
      * ``'pressure'``, fluid pressure




.. _Element-Recorder:

Element Recoder
---------------


.. _PVD-Recorder:

PVD Recoder
------------

.. py:function:: recorder('PVD', filename, respType)
   :noindex:

   create a recorder to record nodal information

   :param str filename: the file name not including the extension, a directory
      with the ``filename`` should exist and a ``filename.pvd`` will be created.
   :param str respType: a string indicating response required

      * ``'disp'``, displacement
      * ``'vel'``, velocity
      * ``'accel'``, acceleration
      * ``'pressure'``, fluid pressure
      * ``'incrDisp'``, incremental displacement
      * ``'eigen'``, eigenvector
      * ``'-precision', precision(int)``, data precision
      * ``'eleResponse', *args``, element responses
      * ``'-dT', dT``, time interval for recording
