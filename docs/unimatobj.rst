.. include:: sub.txt

==============================================
 uniaxialMaterial 
==============================================

.. class:: uniaxialMaterial()

   A subclass of :class:`tagged`
   and a base class for UniaxialMaterial objects.

   One cannot create an :class:`uniaxialMaterial` object
   directly, but only through its subclasses.

   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`uniaxialMaterial.tag`
     #. :attr:`uniaxialMaterial.strain`
     #. :attr:`uniaxialMaterial.plasticStrain`
     #. :attr:`uniaxialMaterial.stress`
     #. :attr:`uniaxialMaterial.tangent`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`

Following are  available uniaxial material subclasses in the OpenSees:

.. toctree::
   :maxdepth: 2

   elasticMaterial
   hardening

.. attribute:: uniaxialMaterial.strain
      
   An object attribute (get/set) |float|.
   The material strains.


.. attribute:: uniaxialMaterial.plasticStrain
      
   An object attribute (get/set) |float|.
   The approximate plastic strains.


.. attribute:: uniaxialMaterial.stress

   An object attribute (get) |float|.
   The material stress.


.. attribute:: uniaxialMaterial.tangent

   An object attribute (get) |float|.
   The material tangent at current strain.
 
