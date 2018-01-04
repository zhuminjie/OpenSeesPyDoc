.. include:: sub.txt

=================================
 fullGen -- General Dense solver
=================================

.. class:: FullGen()

   Create a FullGen system for full matrix.
   When a solution is required, the Lapack routines DGESV and DGETRS are used.
   This type of system should almost never be used! A subclass of :class:`system`.
