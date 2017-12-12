.. include:: sub.txt

Recorder Object
================

.. class:: recorder()

   The :class:`recorder` object is to monitor what is happening during the
   analysis and generate output for the user.
   Use :ref:`recorder-class-methods` below to create recorderes.

Object methods
---------------------

#. :attr:`recorder.automatic`

   An object attribute (get) |int|.
   If it's ``1``, the recorder will be called in each time step to
   record outputs. Otherwise, the user should invoke the call.

   ::
   
      if re.automatic == 0:
          re.record()

	   
     
Object methods
---------------------

#. :meth:`recorder.__str__`
#. :meth:`recorder.record`

.. method:: recorder.__str__()

   The string reprsentation of the :class:`recorder`. Usually
   used in the |print| function.

   ::

      print(m)

.. method:: recorder.record()

   Record the outputs. This method will be called automatically
   after the analysis if :attr:`recorder.automatric` is ``1``.

   ::

      re.record()

.. _recorder-class-methods:


Class methods
---------------

#. :meth:`recorder.pvd`


.. classmethod:: recorder.pvd(filename,automatic=1,dT=0.0,disp=0,vel=0,accel=0,incrDisp=0,reaction=0,pressure=0,unbalancedLoad=0,mass=0,eigen=0,precision=10,indent=2)

   Create a pvd recorder object, which can loaded in `ParaView`_.

   ========================   ======================================================================
   ``filename`` |str|         A string for the name of pvd files. A directory with the
		              name ``filename`` should be created by the user
                              and ``filename.pvd`` will be created by OpenSees.
   ``automatic`` |int|        Set the value of :attr:`recorder.automatic`. (optional)
   ``dT`` |float|             Time interval for recording. will record when next step
		              is ``dT`` greater than last recorder step.
                              (optional, ``dT=0`` means to record at every time step)
   ``disp`` |int|             Include nodal displacement in the outputs or not. (optional)
   ``vel`` |int|              Include nodal velocity in the outputsor not. (optional)
   ``accel`` |int|            Include nodal acceleration in the outputsor not. (optional)
   ``incrDisp`` |int|         Include nodal incremental displacement in the
                              outputsor not. (optional)
   ``reaction`` |int|         Include nodal reaction in the outputsor not. (optional)
   ``pressure`` |int|         Include nodal fluid pressure in the outputsor not. (optional)
   ``unbalancedLoad`` |int|   Include nodal unbalanced load in the outputsor not. (optional)
   ``mass`` |int|             Include nodal mass in the outputsor not. (optional)
   ``eigen`` |int|            The number of eigen values to be includeded
		              in the outputsor not. (optional)
   ``precision`` |int|        Output data precision. (optional)
   ``indent`` |int|           Indentation of output files. (optional)
   ========================   ======================================================================


   ::

      pvd = recorder.pvd('test',automatic = 0)
      pvd.record()


