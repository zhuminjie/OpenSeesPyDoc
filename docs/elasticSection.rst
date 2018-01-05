.. include:: sub.txt

====================================
 elasticSection
====================================

.. class:: elasticSection(E, A, Iz, Iy=0.0, G=0.0, J=0.0, alphaY=0.0, alphaZ=0.0)

   Create a Elastic :class:`section` object. The inclusion of shear deformations is optional.
   The elastic section can be used in the nonlinear beam column elements, which is useful in the initial stages of developing a complex model.

   ========================   =============================================================
   ``E`` |float|              Tangent stiffness.
   ``A`` |float|              Cross-sectional area of section.
   ``Iz`` |float|             Second moment of area about the local z-axis.
   ``Iy`` |float|             Second moment of area about the local y-axis.
		              (required for 3D analysis).
   ``G`` |float|              Shear Modulus
		              (optional for 2D analysis, required for 3D analysis).
   ``J`` |float|              Torsional moment of inertia of section
		              (required for 3D analysis).
   ``alphaY`` |float|         Shear shape factor along the local y-axis (optional).
   ``alphaZ`` |float|         Shear shape factor along the local z-axis (optional).
   ========================   =============================================================

   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`section.deformation`
     #. :attr:`section.stress`
     #. :attr:`section.stiff`
     #. :attr:`section.flexibility`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`
