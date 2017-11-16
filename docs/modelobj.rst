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
      See :ref:`modelobj-example`.
     
Object attributes
------------------------

.. attribute:: model.ndm
      
   An object attribute (get/set) |int|.
   The number of dimentions of the model.

.. attribute:: model.ndf

   An object attribute (get/set) |int|.
   The default number of degrees of freedoms per :class:`node`.




Object methods
---------------------

#. :meth:`model.__str__`
#. :meth:`model.fix`
#. :meth:`model.wipe`

.. method:: model.__str__()

   The string reprsentation of the :class:`model`. Usually
   used in the |print| function.

.. method:: model.fix(nd, fix=[])

   Fix a :class:`node`. The  ``fix`` |listi|
   contains ``1`` and ``0`` to indicate
   corresponding dofs fixed or not.
   Return :class:`sp` objects  |list|.

.. method:: model.wipe()

   Wipe all data in this model. 


.. _modelobj-example:

Examples
---------

::

  m = model(ndm=2, ndf=2)

  m.fix(nd, fix=[1,1])

  m.ndf = 3
  for nd in nds:
      fix(nd, [1,1,1])


  print(m)



