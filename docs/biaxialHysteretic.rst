.. include:: sub.txt

====================================
 biaxialHysteretic
====================================

.. classmethod:: biaxialHysteretic(k,fc,fn,alp,als,eta=0.6,r0=0.0,rp=0.0,rs=0.0,rc=0.0,rn=0.0,Rs=0.0,sig=0.1,lmbda=0.0)

   Create a BiaxialHysteretic :class:`section` object. A subclass of :class:`section`.

   ========================   ===========================================================================================
   ``k`` |float|              The initial stiffness :math:`k`.
   ``fc`` |float|             Yielding strenth :math:`f_c`.
   ``fn`` |float|             Ultimate strenth :math:`f_n`.
   ``alp`` |float|            :math:`\alpha_p`, post-yielding stiffness = :math:`\alpha_pk`.
   ``als`` |float|            :math:`\alpha_s`, ultimate stiffness = :math:`\alpha_sk`.
   ``eta`` |float|            :math:`\eta`, parameter that controls the unloading shape of
		              the hysteretic spring.
   ``r0`` |float|             Stiffness deterioration parameter for :math:`k`.
   ``rp`` |float|             Stiffness deterioration parameter for :math:`\alpha_pk`.
   ``rs`` |float|             Stiffness deterioration parameter for :math:`\alpha_sk`.
   ``rc`` |float|             Strenth deterioration parameter for :math:`f_c`.
   ``rn`` |float|             Strenth deterioration parameter for :math:`f_n`.
   ``Rs`` |float|             Controls the pinching phenomenon of the hysteretic spring.
		              :math:`R_s = 0` means no pinching.
   ``sig`` |float|            Controls the pinching phenomenon of the hysteretic spring.
   ``lmbda`` |float|          Controls the pinching phenomenon of the hysteretic spring.
   ========================   ===========================================================================================


   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`section.deformation`
     #. :attr:`section.stress`
     #. :attr:`section.stiff`
     #. :attr:`section.flexibility`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`




   ::

      sec = section.BiaxialHysteretic(k=8e3, fc=40.0, fn=52.0, alp=0.15, als=-1.0/24, eta=0.6,
                                      r0=0.01, rp=0.01, rs=0.0, rc=0.005, rn=0.003,
                                      Rs=0.2,lmbda=0.1)

      bh1 = section.BiaxialHysteretic(k=1.0, fc=0.5, fn=1.0, alp=0.15, als=0.0, eta=0.9,
                                      r0=0.0, rp=0.0, rs=0.0, rc=0.0, rn=0.0, Rs=0.0,
				      sig=0.1,lmbda=0.0)

      bh2 = section.BiaxialHysteretic(k=1.0, fc=0.5, fn=1.0, alp=0.15, als=0.0, eta=0.9,
                                      r0=0.05, rp=0.05, rs=0.0, rc=0.0, rn=0.0, Rs=0.0,
				      sig=0.1, lmbda=0.0)

      bh3 = section.BiaxialHysteretic(k=1.0, fc=0.5, fn=1.0, alp=0.15, als=0.0, eta=0.9,
                                      r0=0.0, rp=0.0, rs=0.0, rc=0.05, rn=0.05, Rs=0.0,
				      sig=0.1,lmbda=0.0)

      bh4 = section.BiaxialHysteretic(k=1.0, fc=0.5, fn=1.0, alp=0.15, als=0.0, eta=0.6,
                                      r0=0.05, rp=0.05, rs=0.0, rc=0.0, rn=0.0, Rs=0.3,
				      sig=0.1,lmbda=0.0)

