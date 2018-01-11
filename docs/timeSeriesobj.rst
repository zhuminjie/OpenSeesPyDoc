.. include:: sub.txt

========================================
 timeSeries  class
========================================

.. class:: timeSeries()

   A subclass of :class:`tagged` and
   a base class for the OpenSees TimeSeries object.

   One cannot create an :class:`timeSeries` object
   directly, but only through its subclasses.

   * attributes

     #. :attr:`tagged.tag`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`


Following are timeSeries subclasses available in the OpenSees:

.. toctree::
   :maxdepth: 2

   constantSeries
   linearSeries
   trigSeries
   triangleSeries
   rectangularSeries
   pulseSeries
   pathSeries



