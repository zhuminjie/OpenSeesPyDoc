.. include:: sub.txt

Model Object
==============

.. class:: model(type='basic', ndm=0, ndf=0)

   Create a python :class:`model` object which is
   a wrapper to the OpenSees ``Domain`` object.

   ========================   ===============================================================
   ``ndm`` |int|              Number of dimentions. (optional)
   ``ndf`` |int|              Number of dofs. (optional)
   ``type`` |str|             Type of the model. (optional)
   ========================   ===============================================================

   .. note::

      For compatibility reason,
      ``type`` should always be ``'basic'``, which can be omitted.
   
      After creating a :class:`model`, you must assign it
      to a variable in order to keep it from being destructed.

   ::

      m = model(ndm=2, ndf=2)
      m = model(ndm=3, ndf=6)
     
Object attributes
------------------------

.. attribute:: model.ndm
      
   An object attribute (get) |int|.
   The number of dimentions of the model.

   ::
   
      print(m.ndm)

.. attribute:: model.ndf

   An object attribute (get/set) |int|.
   The default number of degrees of freedoms per :class:`node`.
	       
   ::
   
      m.ndf = 6
   
.. attribute:: model.rayleigh

   An object attribute (set) |listf|.
   Assign damping to all existing :class:`element` and :class:`node` objects.
   The Rayleigh damping factors are ``[alphaM,betaK,betaKinit,betaKcomm]``, where

   ========================   ====================================================================
   ``alphaM`` |float|         Factor applied to elements or nodes mass matrix.
   ``betaK`` |float|          Factor applied to elements current stiffness matrix.
   ``betaKinit`` |float|      Factor applied to elements initial stiffness matrix.
   ``betaKcomm`` |float|      Factor applied to elements committed stiffness matrix.
   ========================   ====================================================================

   ::

      m.rayleigh = [0.01, 0.02, 0.0, 0.0]



Object methods
---------------------

#. :meth:`model.__str__`
#. :meth:`model.wipe`

.. method:: model.__str__()

   The string reprsentation of the :class:`model`. Usually
   used in the |print| function.


   ::

      print(m)

.. method:: model.wipe()

   Wipe all objects in this model including analysis objects. 

   ::

      m.wipe()


