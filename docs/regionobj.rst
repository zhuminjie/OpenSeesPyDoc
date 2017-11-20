.. include:: sub.txt

Region Object
=====================

.. class:: region(tag,eles=[],elesOnly=[],nds=[],ndsOnly=[],rayleigh=[])

   A python :class:`region` object is a wrapper to the OpenSees ``MeshRegion`` object.

   ========================   ===========================================================
   ``tag`` |int|              Tag of :class:`region`.
   ``eles`` |liste|           The region includes
	                      these :class:`element` objects and all connected
	                      :class:`node` objects. (optional)
   ``elesOnly`` |liste|       The region includes only
	                      these :class:`element` objects. (optional)
   ``nds`` |listn|            The region includes
	                      these :class:`node` objects and all 
	                      :class:`element` objects of which all
			      :class:`node` objects are prescribed to be in
			      the :class:`region`. (optional)
   ``ndsOnly`` |listn|        The region includes only
	                      these :class:`node` objects. (optional)
   ``rayleigh`` |listf|       Set Rayleigh damping factors for this :class:`region`.
	                      See :attr:`model.rayleigh`. (optional)
   ========================   ===========================================================



Object attributes
------------------

.. attribute:: region.tag
      
   An object attribute (get) |int|.
   The unique tag of the :class:`sp` object.
      
.. attribute:: region.nds

   An object attribute (get/set) |listn|.
   The :class:`node` objects in the :class:`region`.

.. attribute:: region.ndsOnly

   An object attribute (get/set) |listn|.
   The :class:`node` objects in the :class:`region`. Only set :class:`node` objects.

.. attribute:: region.eles

   An object attribute (get/set) |liste|.
   The :class:`element` objects in the :class:`region`.

.. attribute:: region.elesOnly

   An object attribute (get/set) |listn|.
   The :class:`element` objects in the :class:`region`. Only set :class:`element` objects.

.. attribute:: region.rayleigh

   An object attribute (set) |listf|.
   Set Rayleigh damping factors for this :class:`region`.
   See :attr:`model.rayleigh`.

Object methods
-----------------

#. :meth:`region.__str__`
	       
.. method:: region.__str__()

      The string reprsentation of the :class:`region` object. Usually
      used in the |print| function.



Examples
--------

::

     reg = region(eles=eles)

     reg.ndsOnly = nds

