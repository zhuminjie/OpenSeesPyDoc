.. include:: sub.txt

==========================================
 nDMaterial 
==========================================

.. class:: nDMaterial()

   A subclass of :class:`tagged`
   and a base class for nDMaterial objects.

   One cannot create an :class:`nDMaterial` object
   directly, but only through its subclasses.

   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`nDMaterial.strain`
     #. :attr:`nDMaterial.stress`
     #. :attr:`nDMaterial.tangent`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`

Following are  available subclasses in the OpenSees:

.. toctree::
   :maxdepth: 2

   elasticIsotropic

.. attribute:: nDMaterial.strain
      
   An object attribute (get/set) |listf|.
   The material strains.

.. attribute:: nDMaterial.stress

   An object attribute (get) |listf|.
   The material stress.


.. attribute:: nDMaterial.tangent

   An object attribute (get) |listl|.
   The material tangent at current strain.





