.. include:: sub.txt

====================
 RCCircular Section
====================

.. function:: section('RCCircularSection',secTag,coreTag,coverTag,steelTag,d,cover_depth,As,NringsCore,NringsCover,Newedges,Nsteel)
   :noindex:

   This command allows the user to construct an RCCircularSection object, which is an encapsulated fiber representation of a circular reinforced concrete section with core and confined regions of concrete.

   ================================   ===========================================================================
   ``secTag`` |int|                   unique section tag
   ``coreTag`` |int|                  tag of uniaxialMaterial assigned to each fiber in the core region
   ``coverTag`` |int|                 tag of uniaxialMaterial assigned to each fiber in the cover region
   ``steelTag`` |int|                 tag of uniaxialMaterial assigned to each reinforcing bar
   ``d`` |float|                      section radius
   ``cover_depth`` |float|            cover depth (assumed uniform around perimeter)
   ``As`` |float|                     area of reinforcing bars 
   ``NringsCore`` |int|               number of fibers through the core depth
   ``NringsCover`` |int|              number of fibers through the cover depth
   ``Newedges`` |int|                 number of fibers through the edges
   ``Nsteel`` |int|                   number of fibers through the steels
   ================================   ===========================================================================

.. note::

   For more general reinforced concrete section definitions, use the Fiber Section command.
