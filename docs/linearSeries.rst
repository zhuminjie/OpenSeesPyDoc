.. include:: sub.txt

====================================
 linearSeries
====================================

.. class:: linearSeries(factor=1.0)

   Create a Linear :class:`timeSeries` object,  in which the load factor
   applied is linearly proportional to the time in the domain, i.e
   :math:`\lambda = f(t) = cFactor * t`. A subclass of :class:`timeSeries`.

   ========================   =============================================================
   ``factor`` |float|         Linear factor. (optional)
   ========================   =============================================================

   * attributes

     #. :attr:`tagged.tag`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`


