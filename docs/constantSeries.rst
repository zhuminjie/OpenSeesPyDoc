.. include:: sub.txt

==========================================
 constantSeries class
==========================================

.. class:: constantSeries(factor=1.0)

   Create a Constant :class:`timeSeries` object, in which the load
   factor applied remains constant and is independent of the time in the
   domain, i.e. :math:`\lambda = f(t) = C`. A subclass of :class:`timeSeries`.

   ========================   =============================================================
   ``factor`` |float|         The load factor. (optional)
   ========================   =============================================================

   * attributes

     #. :attr:`tagged.tag`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`



