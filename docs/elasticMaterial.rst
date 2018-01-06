.. include:: sub.txt

====================================
 elasticMaterial
====================================

.. class:: elasticMaterial(E, eta=0.0, Eneg=E)

   Create a Elastic :class:`uniaxialMaterial` object. A subclass of :class:`uniaxialMaterial`.

   ========================   =============================================================
   ``E`` |float|              Tangent stiffness.
   ``eta`` |float|            Damping tangent.
   ``Eneg`` |float|           Tangent in compression.
   ========================   =============================================================

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
