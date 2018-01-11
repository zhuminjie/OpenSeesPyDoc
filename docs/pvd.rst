.. include:: sub.txt

====================
 pvd class
====================

.. class:: pvd(filename,automatic=1,dT=0.0,disp=0,vel=0,accel=0,incrDisp=0,reaction=0,pressure=0,unbalancedLoad=0,mass=0,eigen=0,precision=10,indent=2)

   Create a pvd recorder object, which can loaded in `ParaView`_.
   A subclass of :class:`recorder`.

   ========================   ======================================================================
   ``filename`` |str|         A string for the name of pvd files. A directory with the
		              name ``filename`` should be created by the user
                              and ``filename.pvd`` will be created by OpenSees.
   ``automatic`` |int|        Set the value of :attr:`recorder.automatic`. (optional)
   ``dT`` |float|             Time interval for recording. will record when next step
		              is ``dT`` greater than last recorder step.
                              (optional, ``dT=0`` means to record at every time step)
   ``disp`` |int|             Include nodal displacement in the outputs or not. (optional)
   ``vel`` |int|              Include nodal velocity in the outputs or not. (optional)
   ``accel`` |int|            Include nodal acceleration in the outputs or not. (optional)
   ``incrDisp`` |int|         Include nodal incremental displacement in the
                              outputs or not. (optional)
   ``reaction`` |int|         Include nodal reaction in the outputs or not. (optional)
   ``pressure`` |int|         Include nodal fluid pressure in the outputs or not. (optional)
   ``unbalancedLoad`` |int|   Include nodal unbalanced load in the outputs or not. (optional)
   ``mass`` |int|             Include nodal mass in the outputs or not. (optional)
   ``eigen`` |int|            The number of eigen values to be includeded
		              in the outputs. (optional)
   ``precision`` |int|        Output data precision. (optional)
   ``indent`` |int|           Indentation of output files. (optional)
   ========================   ======================================================================

   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`recorder.automatic`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`
     #. :meth:`recorder.record`



   ::

      pvd = recorder.pvd('test',automatic = 0)
      pvd.record()



