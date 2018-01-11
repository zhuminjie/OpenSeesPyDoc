.. include:: sub.txt

====================
 line class
====================

.. class:: line(nds)

   Create a line object. The line take 2 or
   more :class:`node` objects to form a consecutive line.
   A subclass of :class:`mesh`.

   ========================   ======================================================================
   ``nds`` |list|             A list of :class:`node`, which define the line.
   ========================   ======================================================================

   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`mesh.meshsize`
     #. :attr:`mesh.inclDisp`
     #. :attr:`mesh.ndf`
     #. :attr:`mesh.ele`
     #. :attr:`mesh.nds`
     #. :attr:`mesh.eles`
     #. :attr:`mesh.id`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`
     #. :meth:`mesh.clearEles`
     #. :meth:`mesh.clearNodes`

