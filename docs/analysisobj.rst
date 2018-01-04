.. include:: sub.txt

analysis -- Perform Finite-Element Analysis
=============================================

.. class:: analysis()

   
   A subclass of :class:`tagged` and
   a base class for OpenSees analysis.

   * attributes

     #. :attr:`tagged.tag`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`

Following are analysis subclasses available in the OpenSees:

.. toctree::
   :maxdepth: 2

   staticAnalysis
   transientAnalysis
   variableTransientAnalysis
   PFEMAnalysis
