.. include:: sub.txt

Section Object
=======================

.. class:: section()

   A python :class:`section` object
   is a wrapper to the OpenSees ``Section`` object.

   .. note::
   
      One cannot create an :class:`section` object
      directly, but only through :ref:`section-class-methods`.


Object attributes
-------------------

#. :attr:`section.tag`
#. :attr:`section.deformation`
#. :attr:`section.stress`
#. :attr:`section.tangent`

.. attribute:: section.tag
      
   An object attribute (get) |int|.
   The tag of the :class:`section` object.

   ::

      print(sec.tag)

.. attribute:: section.deformation
      
   An object attribute (get/set) |listf|.
   The section deformation.

   ::

      sec.deformation = [0.01,0.01]

.. attribute:: section.stress

   An object attribute (get) |listf|.
   The section stress.

   ::

      print(sec.stress)

.. attribute:: section.tangent

   An object attribute (get) |listl|.
   The section tangent.

   ::

      print(sec.tangent)


Object methods
-------------------

#. :meth:`section.__str__`
#. :meth:`section.fiber`
#. :meth:`section.patch`
#. :meth:`section.layer`
#. :meth:`section.remove`
		  
.. method:: section.__str__()

   The string reprsentation of the :class:`section`. Usually
   used in the |print| function.

   ::

      print(sec)

.. method:: section.fiber(yLoc,zLoc,A,mat)

   Create and add a fiber into a :meth:`section.Fiber` or :meth:`section.NDFiber`.

   ============================   =============================================================
   ``yLoc`` |float|               y coordinate of the fiber in the section (local coordinate system)
   ``zLoc`` |float|               z coordinate of the fiber in the section (local coordinate system)
   ``A`` |float|                  Cross-sectional area of fiber.
   ``mat`` |unimat| or |ndmat|    material for the fiber.
   ============================   =============================================================

   ::

      sec.fiber(yLoc=1.0, zLoc=0.0, A=0.01,mat=mat)

.. method:: section.patch(mat,num,I=[],J=[],K=[],L=[],C=[],radius=[],angle=[])

   Generate a number of :meth:`fiber` over a cross-sectional area for a :meth:`section.Fiber` or :meth:`section.NDFiber`. Currently there are three types of cross-section that :meth:`fiber` can be generated: quadrilateral, rectangular and circular.

   * A quadrilateral patch is defined by four vertices: ``I``, ``J``, ``K``, ``L``. The coordinates of each of the four vertices is specified in COUNTER CLOCKWISE sequence.
   * A rectangular patch is defined by coordinates of vertices: ``I`` and ``J``. The first vertex, ``I``, is the bottom-left point and the second vertex, ``J``, is the top-right point, having as a reference the local y-z plane.
   * A circular patch is defined by a center vertex ``C``, internal and external ``radius``, and starting and ending ``angle``.

   =================================   =============================================================
   ``mat`` |unimat| or |ndmat|         Material for the patch.
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

.. method:: section.layer(mat,num,A,I=[],J=[],C=[],radius=0.0,angle=[0.0,360.0-360.0/num])

   Generate a number of :meth:`fiber` along a line or a circular arc for a :meth:`section.Fiber` or :meth:`section.NDFiber`.

   * A straight layer is defined by two vertices: ``I``, ``J``.
   * A circular arc layer is defined by a center vertex ``C``, a ``radius``, and starting and ending ``angle``.

   =================================   =============================================================
   ``mat`` |unimat| or |ndmat|         Material for the patch.
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

.. method:: section.remove()

   Remove the corresponding OpenSees ``Section`` object.
	       
   .. seealso::

      :meth:`node.remove`


   ::

      sec.remove()

.. _section-class-methods:

Class methods
--------------

#. :meth:`section.Elastic`
#. :meth:`section.Fiber`
#. :meth:`section.NDFiber`

.. classmethod:: section.Elastic(E, A, Iz, Iy=0.0, G=0.0, J=0.0, alphaY=0.0, alphaZ=0.0)

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

   ::

      sec = section.Elastic(E=1e6,A=1.0,Iz=1.0)

.. classmethod:: section.Fiber(tag, GJ=0.0)

   Create a Fiber :class:`section` object, which is composed of :meth:`section.fiber`, with each fiber containing a :class:`uniaxialMaterial`, an area and a location (y,z). 

   ========================   =============================================================
   ``tag`` |int|              :class:`section` tag.
   ``GJ`` |float|             Linear-elastic torsional stiffness assigned to the section.
   ========================   =============================================================

   ::

      sec = section.Fiber()
      sec.fiber(yLoc=1.0, zLoc=0.0, A=0.01,mat=mat)
      sec.patch(mat=mat, num=[10,10], vertex=[[0.0,0.0],[1.0,0.0],[1.0,1.0],[0.0,1.0]])

.. classmethod:: section.NDFiber(tag, GJ=0.0)

   Create a NDFiber :class:`section` object, which is composed of :meth:`section.fiber`, with each fiber containing a :class:`NDMaterial`, an area and a location (y,z). 

   ========================   =============================================================
   ``tag`` |int|              :class:`section` tag.
   ``GJ`` |float|             Linear-elastic torsional stiffness assigned to the section.
   ========================   =============================================================

   ::

      sec = section.NDFiber()
      sec.fiber(yLoc=1.0, zLoc=0.0, A=0.01,mat=mat)
      sec.patch(mat=mat, num=[10,10], vertex=[[0.0,0.0],[1.0,0.0],[1.0,1.0],[0.0,1.0]])

