.. include:: sub.txt

====================================
 bubble2d -- PFEM Bubble 2D Element
====================================

.. class:: bubble2d(nds, rho, mu, b1, b2, thk=1.0, kappa=-1)

   Create a PFEM :class:`element` object, which uses P1+P1 formulation, i.e.
   three velocity nodes and three pressure nodes. The bubble mode is
   condensed internally. 

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


   * attributes

     Inherited from :class:`element`

     #. :attr:`element.tag`
     #. :attr:`element.nds`
     #. :attr:`element.ndf`
     #. :attr:`element.stiff`
     #. :attr:`element.damp`
     #. :attr:`element.mass`

   * methods

     Inherited from :class:`element`
   
     #. :meth:`element.__str__`
     #. :meth:`element.remove`


   ::

      # create an element
      ele = bubble(nds=[vnd1,pnd1,vnd2,pnd2,vnd3,pnd3],
                   rho=1000.0, mu=1e-3, b1=0.0, b2=-9.81)



.. class:: bubble2d(ele)

   A converter to convert a :class:`element` object to :class:`bubble2d` object.
