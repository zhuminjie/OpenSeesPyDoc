.. include:: sub.txt

=================
 Pipe Section
=================

.. function:: section('Pipe', secTag, do, t, <'-alphaV', alphaV>, <'-defaultAlphaV'>, <'-rho', rho>)
   :noindex:

   The pipe section should be used with :doc:`pipe` and :doc:`curvedPipe` for pipes.

   ================================   =============================================================================================================================================================================================================================================================================================================================
   ``secTag`` |int|                   unique section tag
   ``do`` |float|                     the outside diameter of the pipe
   ``t`` |float|                      the thickness of the pipe wall
   ``alphaV`` |float|                 the shape factor for shear distortion and must follow the option ``'-alphaV'``. This is optional to be set by the user.
   ``'-defaultAlphaV'`` |str|         use the option to set the shape factor to the default value :math:`\alpha_V = \frac{4}{3}\frac{r_o^3-r_i^3}{(r_o^2+r_i^2)(r_o-r_i)}` where :math:`r_o=d_o/2` and :math:`r_i=r_o-t`. If neither ``'-alphaV'`` nor ``'-defaultAlphaV'`` is used, the shear distortion is ignored. If both are given, the last one is used.
   ``rho`` |float|                    the mass per unit length of the section, which is used as mass coefficient in the dynamic analysis and will **not** be used to apply the gravity load, which should be added using the :doc:`ops.eleLoad` command. Default is ``0``.
   ================================   =============================================================================================================================================================================================================================================================================================================================

