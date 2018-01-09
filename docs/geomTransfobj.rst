.. include:: sub.txt

============================================================
 geomTransf 
============================================================

.. class:: geomTransf()

   A subclass of :class:`tagged`
   and a base class for CrdTransf objects.

   One cannot create an :class:`geomTransf` object
   directly, but only through its subclasses.

   * attributes

     #. :attr:`tagged.tag`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`

Following are  available subclasses in the OpenSees:

.. toctree::
   :maxdepth: 2

   linearTransf
   pdelta
   corotational



