.. include:: sub.txt

====================================
 fiberSection
====================================

.. class:: fiberSection(GJ=0.0)

   Create a Fiber :class:`section` object, which is composed of :meth:`fiberSection.fiber`, with each fiber containing a :class:`uniaxialMaterial`, an area and a location (y,z). A subclass of :class:`section`.

   ========================   =============================================================
   ``GJ`` |float|             Linear-elastic torsional stiffness assigned to the section.
   ========================   =============================================================

   ::

      sec = fiberSection()
      sec.fiber(yLoc=1.0, zLoc=0.0, A=0.01,mat=mat)
      sec.patch(mat=mat, num=[10,10], vertex=[[0.0,0.0],[1.0,0.0],[1.0,1.0],[0.0,1.0]])


   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`section.deformation`
     #. :attr:`section.stress`
     #. :attr:`section.stiff`
     #. :attr:`section.flexibility`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`
     #. :meth:`section.uniMat`
     #. :meth:`section.nDMat`
     #. :meth:`fiberSection.fiber`
     #. :meth:`fiberSection.patch`
     #. :meth:`fiberSection.layer`




.. method:: fiberSection.fiber(yLoc,zLoc,A,mat)

   Create and add a fiber into a :class:`fiberSection`.

   ============================   =============================================================
   ``yLoc`` |float|               y coordinate of the fiber in the section (local coordinate system)
   ``zLoc`` |float|               z coordinate of the fiber in the section (local coordinate system)
   ``A`` |float|                  Cross-sectional area of fiber.
   ``mat`` |unimat|               material for the fiber.
   ============================   =============================================================

   ::

      sec.fiber(yLoc=1.0, zLoc=0.0, A=0.01,mat=mat)

.. method:: fiberSection.patch(mat,num,I=[],J=[],K=[],L=[],C=[],radius=[],angle=[])

   Generate a number of :meth:`fiberSection.fiber` over a cross-sectional area for a :class:`fiberSection`. Currently there are three types of cross-section that :meth:`fiberSection.fiber` can be generated: quadrilateral, rectangular and circular.

   * A quadrilateral patch is defined by four vertices: ``I``, ``J``, ``K``, ``L``. The coordinates of each of the four vertices is specified in COUNTER CLOCKWISE sequence.
   * A rectangular patch is defined by coordinates of vertices: ``I`` and ``J``. The first vertex, ``I``, is the bottom-left point and the second vertex, ``J``, is the top-right point, having as a reference the local y-z plane.
   * A circular patch is defined by a center vertex ``C``, internal and external ``radius``, and starting and ending ``angle``.

   =================================   =============================================================
   ``mat`` |unimat|                    Material for the patch.
   ``num`` |listf|                     Number of subdivisions in the IJ and JK directions (quad), local y and z directions (rect), or in circumferential and radial directions (circular).
   ``I`` |listf|                       y and z cordinates of vertex I (optional)
   ``J`` |listf|                       y and z cordinates of vertex J (optional)
   ``K`` |listf|                       y and z cordinates of vertex K (optional)
   ``L`` |listf|                       y and z cordinates of vertex L (optional)
   ``C`` |listf|                       y and z cordinates of vertex C (optional)
   ``radius`` |listf|                  internal and external radius (optional)
   ``angle`` |listf|                   starting and ending angles (optional)
   =================================   =============================================================

   ::

      # quad patch
      sec.patch(mat=mat, num=[10,10], I=[0.0,0.0], J=[1.0,0.0], K=[1.0,1.0], L=[0.0,1.0])

      # rect patch
      sec.patch(mat=mat, num=[2,2], I=[0.0,0.0], J=[1.0,1.0])

      # circ patch
      sec.patch(mat=mat, num=[5,5], C=[0.0,0.0], radius=[0.0,0.8], angle=[0.0, 180.0])

.. method:: fiberSection.layer(mat,num,A,I=[],J=[],C=[],radius=0.0,angle=[0.0,360.0-360.0/num])

   Generate a number of :meth:`fiberSection.fiber` along a line or a circular arc for a :class:`fiberSection`.

   * A straight layer is defined by two vertices: ``I``, ``J``.
   * A circular arc layer is defined by a center vertex ``C``, a ``radius``, and starting and ending ``angle``.

   =================================   =============================================================
   ``mat`` |unimat|                    Material for the patch.
   ``num`` |float|                     Number of fibers along line.
   ``A`` |float|                       Area of each fiber.
   ``I`` |listf|                       y and z cordinates of vertex I  (optional)
   ``J`` |listf|                       y and z cordinates of vertex J (optional)
   ``C`` |listf|                       y and z cordinates of vertex C (optional)
   ``radius`` |float|                  Radius of circular arc (optional)
   ``angle`` |listf|                   starting and ending angles (optional)
   =================================   =============================================================

   ::

      # straight layer
      sec.layer(mat=mat, num=10, I=[0.0,0.0], J=[1.0,1.0])

      # circ layer
      sec.patch(mat=mat, num=5, C=[0.0,0.0], radius=0.8, angle=[0.0, 180.0])
