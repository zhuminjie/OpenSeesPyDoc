.. include:: sub.txt

=============================
 setNodeTemperature command
=============================

.. function:: setNodeTemperature(nodeTag, value)

   set the nodal temperature for :doc:`pipe` and :doc:`curvedPipe` elements.

   ========================   =================================================================================================================================================================================================================================
   ``nodeTag`` |int|          node tag.
   ``value`` |float|          the temperature value for the node. The nodal temperature will affect the thermal expansion for both :doc:`pipe` and :doc:`curvedPipe` elements.
   ========================   =================================================================================================================================================================================================================================
