.. include:: sub.txt

===============
 Layer Command
===============

.. function:: layer(type, *args)

   The layer command is used to generate a number of fibers along a line or a circular arc.

.. function:: layer('straight', matTag,numFiber,areaFiber,*start,*end)
   :noindex:

   This command is used to construct a straight line of fibers

   ================================   ===========================================================================
   ``matTag`` |int|                   material tag associated with this fiber (UniaxialMaterial tag for a FiberSection and NDMaterial tag for use in an NDFiberSection).
   ``numFiber`` |int|                 number of fibers along line
   ``areaFiber`` |float|              area of each fiber
   ``start`` |listf|                  y & z-coordinates of first fiber in line (local coordinate system)
   ``end`` |listf|                    y & z-coordinates of last fiber in line (local coordinate system)
   ================================   ===========================================================================


.. function:: layer('circ', matTag,numFiber,areaFiber,*center,radius,*ang=[0.0,360.0-360/numFiber])
   :noindex:

   This command is used to construct a line of fibers along a circular arc

   ================================   ===========================================================================
   ``matTag`` |int|                   material tag associated with this fiber (UniaxialMaterial tag for a FiberSection and NDMaterial tag for use in an NDFiberSection).
   ``numFiber`` |int|                 number of fibers along line
   ``areaFiber`` |float|              area of each fiber
   ``center`` |listf|                 y & z-coordinates of center of circular arc
   ``radius`` |float|                 radius of circlular arc
   ``ang`` |listf|                    starting and ending angle (optional)
   ================================   ===========================================================================


.. function:: layer('rect', matTag, numFiberY, numFiberZ, areaFiber, *center, distY, distZ)
   :noindex:

   This command is used to construct a line of fibers around a rectangle with specified center coordinate, extending +/-distY/2 and +/-distZ/2 from center. If numFiberY and numFiberZ are zero, there will be four corner fibers. The total number of fibers is 4+2*numFiberY+2*numFiberZ.

   ================================   ===========================================================================
   ``matTag`` |int|                   material tag associated with this fiber (UniaxialMaterial tag for a FiberSection and NDMaterial tag for use in an NDFiberSection).
   ``numFiberY`` |int|                number of intermediate fibers on each side along Y-direction
   ``numFiberZ`` |int|                number of intermediate fibers on each side along Z-direction
   ``areaFiber`` |float|              area of each fiber
   ``center`` |listf|                 y & z-coordinates of center of rectangle
   ``distY`` |float|                  height of rectangle in Y-direction
   ``distZ`` |float|                  width of rectangle in Z-direction
   ================================   ===========================================================================
