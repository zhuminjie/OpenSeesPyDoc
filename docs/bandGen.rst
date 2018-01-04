.. include:: sub.txt

==================================
 bandGen -- General Banded solver
==================================

.. class:: bandGen()

   Create a BandGen system for matrix which have a banded profile.
   When a solution is required, the Lapack routines DGBSV and SGBTRS are used.
   A subclass of :class:`system`.
