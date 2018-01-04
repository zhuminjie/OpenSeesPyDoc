.. include:: sub.txt

trbdf2 -- Time Integration with the TRBDF2 method
====================================================

.. class:: trbdf2()

      Create a TRBDF2 integrator. The TRBDF2 integrator is a composite scheme that alternates between the Trapezoidal scheme and a 3 point backward Euler scheme. It does this in an attempt to conserve energy and momentum, something :class:`newmark` does not always do. A subclass of :class:`integrator`.

   As opposed to dividing the time-step in 2 as outlined in the `Bathe2007`_, we just switch alternate between the 2 integration strategies,i.e. the time step in our implementation is double that described in the `Bathe2007`_.

   ::

      trbdf2()

