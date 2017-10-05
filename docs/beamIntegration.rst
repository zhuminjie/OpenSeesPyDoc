beamIntegration
===============

.. py:currentmodule:: opensees

.. py:function:: beamIntegration(type[,*opt])

   create an beam integration object for force-based and displacement-based Beam-Column elements

   :param str type:  :ref:`beamIntegreation types <beamIntegration-types>`
   :param opt: type specific options
   :type opt: list

.. _beamIntegration-types:

.. toctree::
   :maxdepth: 2
   :caption: Available beamIntegration types

   Lobatto-BI
   Legendre-BI
   NewtonCotes-BI
   Radau-BI
   Trapezoidal-BI
   CompositeSimpson-BI
   UserDefined-BI
   FixedLocation-BI
   LowOrder-BI
   MidDistance-BI
   UserHinge-BI
   HingeMidpoint-BI
   HingeRadau-BI
   HingeRadauTwo-BI
   HingeEndpoint-BI
	     




