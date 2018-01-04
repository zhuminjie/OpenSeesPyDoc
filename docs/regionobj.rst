.. include:: sub.txt

============================================
 region -- A Region of Finite-Element Model
============================================

.. class:: region()

   
   Create a OpenSees MeshRegion object.
   A subclass of :class:`tagged`.

   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`region.nds`
     #. :attr:`region.ndsOnly`
     #. :attr:`region.eles`
     #. :attr:`region.elesOnly`
     #. :attr:`region.rayleigh`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`

   

.. attribute:: region.nds

   An object attribute (get/set) |listn|.
   The :class:`node` objects in the :class:`region`.

   ::

      reg.nds = nds

.. attribute:: region.ndsOnly

   An object attribute (get/set) |listn|.
   The :class:`node` objects in the :class:`region`. Only set :class:`node` objects.

   ::

      reg.ndsOnly = nds[::2]

.. attribute:: region.eles

   An object attribute (get/set) |liste|.
   The :class:`element` objects in the :class:`region`.

   ::

      reg.eles = eles[:]

.. attribute:: region.elesOnly

   An object attribute (get/set) |listn|.
   The :class:`element` objects in the :class:`region`. Only set :class:`element` objects.

   ::

      reg.elesOnly = eles[0:4]

.. attribute:: region.rayleigh

   An object attribute (set) |listf|.
   Set Rayleigh damping factors for this :class:`region`.
   See :attr:`model.rayleigh`.

   ::

      reg.rayleigh = [0.01, 0.01, 0.0, 0.0]

