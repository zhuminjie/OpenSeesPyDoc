.. include:: sub.txt

=============
 sdfResponse
=============

.. function:: sdfResponse(m, zeta, k, Fy, alpha, dtF, filename, dt[, uresidual, umaxprev])
   :noindex:

   It is a command that computes bilinear single degree of freedom response in C++, and is much quicker than using the OpenSees model builder.  The command implements Newmark’s method with an inner Newton loop.
      
   ========================   =============================================================
   ``m`` |float|              mass
   ``zeta`` |float|           damping ratio
   ``k`` |float|              stiffness
   ``Fy`` |float|             yielding strength
   ``alpha`` |float|          strain-hardening ratio
   ``dtF`` |float|            time step for input data
   ``filename`` |str|         input data file
   ``dt`` |float|             time step for analysis
   ``uresidual`` |float|      displacement residual tolerence (optional)
   ``umaxprev`` |float|       displacement tolerence (optional)
   ========================   =============================================================

