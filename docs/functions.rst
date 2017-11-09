.. _built-in-funcs:

Built-in Functions
===================

The OpenSeesPy interpreter has a number of functions and types built into it that
are always available.  They are listed here in alphabetical order.


===================  =================  ==================  ================  ====================
..                   ..                 Built-in Functions  ..                ..
===================  =================  ==================  ================  ====================
:func:`model`         :func:`wipe`
===================  =================  ==================  ================  ====================


.. function:: model(type='basic', ndm=0, ndf=0)

   Set the number of dimentions and the number of degrees of freedoms
   of the model. Currently, only basic type is available. For example::

     model(ndm=2)

     model(ndm=2, ndf=2)

     model(2,3)

     model('basic', ndm = 3, ndf = 6)
	      




.. function:: wipe()

   Wipe all model in the OpenSees
