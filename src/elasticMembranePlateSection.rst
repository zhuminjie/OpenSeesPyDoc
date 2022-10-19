.. include:: sub.txt

================================
 Elastic Membrane Plate Section
================================

.. function:: section('ElasticMembranePlateSection',secTag,E_mod,nu,h,rho,<Ep_modifier>)
   :noindex:

   This command allows the user to construct an ElasticMembranePlateSection object, which is an isotropic section appropriate for plate and shell analysis.

   ================================   =========================================================================================
   ``secTag`` |int|                   unique section tag
   ``E_mod`` |float|                      Young's Modulus
   ``nu`` |float|                     Poisson's Ratio
   ``h`` |float|                      depth of section
   ``rho`` |float|                    mass density
   ``Ep_modifier`` |float|             factor to modify out-of-plane bending stiffness (optional). E_plate = Ep_modifier*E_mod
   ================================   =========================================================================================
