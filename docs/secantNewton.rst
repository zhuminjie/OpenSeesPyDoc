.. include:: sub.txt

=====================
 secantNewton  class
=====================

.. class:: secantNewton(iterate='current',increment='current',maxDim=3)

   Create a SecantNewton algorithm which uses the two-term update to accelerate the convergence of the :class:`modified`. A subclass of :class:`algorithm`.

   The default "cut-out" values recommended by Crisfield (R1=3.5, R2=0.3) are used.

   See :class:`krylovNewton` for parameters.




