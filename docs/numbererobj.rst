.. include:: sub.txt

Numberer Object
=======================

.. class:: numberer()

   A python :class:`numberer` object
   is a wrapper to the OpenSees ``DOF_Numberer`` object.

   .. note::
   
      One cannot create an :class:`numberer` object
      directly, but only through the :ref:`numberer-class-methods`.

      There is only one global :class:`numberer` object.
      Creating another :class:`numberer` object
      will automatically invalidate the previous :class:`numberer` objects.

.. _numberer-class-methods:

Class methods
--------------

#. :meth:`numberer.Plain`
#. :meth:`numberer.RCM`
#. :meth:`numberer.AMD`
	       
.. classmethod:: numberer.Plain()

   Create a Plain :class:`numberer`, which takes whatever
   order the OpenSees ``Domain`` gives it ``Nodes`` and numbers them.

.. classmethod:: numberer.RCM()

   Create a Reverse Cuthill-McKee :class:`numberer`.

.. classmethod:: numberer.AMD()

   Create a Alternative Minimum Degree :class:`numberer`.


