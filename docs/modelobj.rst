.. _model-obj:

Model Object
==============

.. index:: object: model

.. class:: model(type='basic', ndm=0, ndf=0)

   Create a model domain with the number of dimentions ``ndm`` and
   the number of degrees of freedoms ``ndf``. For compatibility reason,
   the ``type`` should always be 'basic', which can be omitted.
   A newly created model is always made the current model.

     


   .. attribute:: ndm
      
      An object attribute (get/set).
      The number of dimentions of the model.

   .. attribute:: ndf

      An object attribute (get/set).
      The default number of degrees of freedoms per :class:`node`.

   .. method:: __str__()

      The string reprsentation of the model. Usually
      used in the `print`_ function.

   .. method:: fix(nd, fix=[])

      Fix a :class:`node`. The list ``fix``
      contains ``1`` and ``0`` to indicate
      corresponding dofs fixed or not.
      Return a list of :class:`sp` objects.

   .. method:: makeCurrent()

      Make this :class:`model` object the current model.

   .. method:: wipe()

      Wipe all data in this model. This method is
      differen to ``del`` the model object or :meth:`wipeDomain`. When
      you ``del`` the model object or set it to ``None``, it only deletes
      the domain, but leaves data such as materials, sections,
      timeSeries, etc.

   .. method:: wipeDomain()

      Wipe all data in the domain of this model
      but dose not delete the domain.

   Examples::

     m1 = model(ndm=2)

     m2 = model(ndm=2, ndf=2)

     m3 = model(2,3)

     m4 = model('basic', ndm = 3, ndf = 6)

     m = model(ndm = 2, ndf = 2)
   
     m.fix(nd, fix=[1,1])

     m.ndf = 3
     for nd in nds:
       fix(nd, [1,1,1])


     m1.makeCurrent()

     del m

     m1 = None


.. _print: https://docs.python.org/3/library/functions.html#print
