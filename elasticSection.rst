.. include:: sub.txt

=================
 Elastic Section
=================

.. function:: section('Elastic', secTag, E, A, Iz, G=0.0, alphaY=0.0)
   :noindex:

.. function:: section('Elastic', secTag, E, A, Iz, Iy, G, J, alphaY=0.0, alphaZ=0.0)
   :noindex:

   This command allows the user to construct an ElasticSection. The inclusion of shear deformations is optional.

   ================================   ===========================================================================
   ``secTag`` |int|                   unique section tag
   ``E`` |float|                      Young's Modulus
   ``A`` |float|                      cross-sectional area of section
   ``Iz`` |float|                     second moment of area about the local z-axis
   ``Iy`` |float|                     second moment of area about the local y-axis
                                      (required for 3D analysis)
   ``G`` |float|                      Shear Modulus (optional for 2D analysis,
                                      required for 3D analysis)
   ``J`` |float|                      torsional moment of inertia of section
                                      (required for 3D analysis)
   ``alphaY`` |float|                 shear shape factor along the local y-axis (optional)
   ``alphaZ`` |float|                 shear shape factor along the local z-axis (optional)
   ================================   ===========================================================================


.. note::

   The elastic section can be used in the nonlinear beam column elements, which is useful in the initial stages of developing a complex model.
