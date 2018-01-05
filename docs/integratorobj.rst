.. include:: sub.txt

integrator 
======================================================

.. class:: integrator()

   A subclass of :class:`tagged` and 
   a base class for OpenSees Integrator.

Following are integrator subclasses available in the OpenSees:

Static integrator objects:

.. toctree::
   :maxdepth: 2

   loadControl
   displacementControl
   minUnbalDispNorm
   arcLength

.. _transient-integrators: 

Transient integrator objects:

.. toctree::
   :maxdepth: 2

   centralDifference
   newmark
   hht
   generalizedAlpha
   trbdf2
   explicitDifference
   pfemIntegrator



