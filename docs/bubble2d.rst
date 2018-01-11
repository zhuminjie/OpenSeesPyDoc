.. include:: sub.txt

==========================================
 bubble class
==========================================

.. class:: bubble(nds, rho, mu, b1, b2, thk=1.0, kappa=-1)

   Create a PFEM :class:`element` object, which uses P1+P1 formulation, i.e.
   three velocity nodes and three pressure nodes. The bubble mode is
   condensed internally. A subclass of :class:`element`.

   ========================   =============================================================
   ``nds`` |list|             Six velocity and pressure :class:`node` objects in
		              the order of
		              ``[vnd1,pnd1,vnd2,pnd2,vnd3,pnd3]``.
   ``rho`` |float|            Fluid density.
   ``mu`` |float|             Fluid viscosity.
   ``b1`` |float|             Body acceleration in x direction.
   ``b2`` |float|             Body acceleration in y direction.
   ``thk`` |float|            Element thickness. (optional)
   ``kappa`` |float|          Fluid bulk modulus. Negative values mean incompressible
		              fluid. (optional)
   ========================   =============================================================





.. class:: bubble(ele)

   Convert an :class:`element` to :class:`bubble`.

   ========================   =============================================================
   ``ele`` |element|          A :class:`element` object.
   ========================   =============================================================


   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`element.nds`
     #. :attr:`element.ndf`
     #. :attr:`element.stiff`
     #. :attr:`element.damp`
     #. :attr:`element.mass`
     #. :attr:`element.force`
     #. :attr:`element.dampingForce`
     #. :attr:`element.dynamicForce`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`
     #. :meth:`element.section`
     #. :meth:`element.uniMat`
     #. :meth:`element.nDMat`



