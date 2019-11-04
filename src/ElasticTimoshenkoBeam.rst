.. include:: sub.txt

======================================
Elastic Timoshenko Beam Column Element
======================================

This command is used to construct an ElasticTimoshenkoBeam element object. A Timoshenko beam is a frame member that accounts for shear deformations. The arguments for the construction of an elastic Timoshenko beam element depend on the dimension of the problem, ndm:

.. function:: element('ElasticTimoshenkoBeam', eleTag,*eleNodes,E, G, A, Iz, Avy, transfTag,['-mass', massDens],['-cMass'])
   :noindex:

   For a two-dimensional problem:

.. function:: element('ElasticTimoshenkoBeam', eleTag,*eleNodes,E, G, A, Iz, Jx, Iy, Iz, Avy, Avz, transfTag,['-mass', mass],['-cMass])
   :noindex:

   For a three-dimensional problem:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of two element nodes
   ``E`` |float|                         Young's Modulus
   ``G`` |float|                         Shear Modulus
   ``A`` |float|                         cross-sectional area of element
   ``Jx`` |float|                        torsional moment of inertia of cross section
   ``Iy`` |float|                        second moment of area about the local y-axis
   ``Iz`` |float|                        second moment of area about the local z-axis
   ``Avy`` |float|                       Shear area for the local y-axis
   ``Avz`` |float|                       Shear area for the local z-axis
   ``transfTag`` |int|                   identifier for previously-defined coordinate-transformation (CrdTransf) object
   ``mass`` |float|                  element mass per unit length (optional, default = 0.0)
   ``'-cMass'`` |str|                    to form consistent mass matrix (optional, default = lumped mass matrix)
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Elastic_Timoshenko_Beam_Column_Element>`_
