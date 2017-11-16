.. include:: sub.txt

System Object
=======================

.. class:: system()

   A python :class:`system` object
   is a wrapper to the OpenSees ``LinearSOE`` and
   ``LinearSOESolver`` objects.

   .. note::
   
      One cannot create an :class:`system` object
      directly, but only through the :ref:`system-class-methods`.

      There is only one global :class:`system` object.
      Creating another :class:`system` object
      will automatically invalid the previous :class:`system` objects.

.. _system-class-methods:

Class methods
--------------

#. :meth:`system.ProfileSPD`
#. :meth:`system.BandGen`
#. :meth:`system.BandSPD`
	       
.. classmethod:: system.ProfileSPD()

   Create a ProfileSPD :class:`system` for symmetric positive definite matrix.

.. classmethod:: system.BandGen()

   Create a BandGen :class:`system` for matrix which have a banded profile.

.. classmethod:: system.BandSPD()

   Create a BandSPD :class:`system` for symmetric positive definite matrix
   which have a banded profile.


   
Examples
----------

::

   system.ProfileSPD()


