.. include:: sub.txt

Analysis Object
=======================

.. class:: analysis()

   A python :class:`analysis` object
   is a wrapper to the OpenSees ``Analysis`` object.

   .. note::
   
      One cannot create an :class:`analysis` object
      directly, but only through the :ref:`analysis-class-methods`.

      There is only one global :class:`analysis` object.
      Creating another :class:`analysis` object
      will automatically invalid the previous :class:`analysis` objects.

      As the :class:`model` object, you must assign it
      to a variable in order to keep it from being destructed.
      See :ref:`analysisobj-example`.

      If the component objects are not defined before hand, the :class:`analysis` automatically creates default component objects and issues warning messages to this effect.


.. _analysis-class-methods:

Class methods
--------------

#. :meth:`analysis.Static`
	       
.. classmethod:: analysis.Static()

   Create a Static :class:`analysis`.

.. method:: analysis.analyze(numIncr)

   Perform the analysis.

   ======================   =============================================================
   ``numIncr`` |int|        Number of analysis steps to perform
   ======================   =============================================================

.. _analysisobj-example:

Examples
----------

::

   analy = analysis.Static()
   analy.analyze(numIncr = 10)


