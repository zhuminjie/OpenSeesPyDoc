.. include:: sub.txt

==================
 Masonry
==================

.. function:: uniaxialMaterial('Masonry', matTag, Fm, Ft, Um, Uult, Ucl, Emo, L, a1, a2, D1, D2, Ach, Are, Ba, Bch, Gun, Gplu, Gplr, Exp1, Exp2, IENV)
   :noindex:

   This command is used to construct a uniaxialMaterial Masonry (Crisafulli, 1997; Torrisi, 2012), which is a uniaxial hysteretic constitutive model for Masonry developed by Crisafulli (1997) and modified by Torrisi (2012).

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``Fm`` |float|                        Compression strength of Masonry (Fm<0)
   ``Ft`` |float|                        Tension Strength of Masonry (Ft>0)
   ``Um`` |float|                        Strain at maximum Strength (Um<0)
   ``Uult`` |float|                      Maximum compression strain (Uult<0)
   ``Ucl`` |float|                       Crack Closing strain (Ucl>0)
   ``Emo`` |float|                       Initial Elastic Modulus
   ``L`` |float|                         Initial Length (just add 1.0)
   ``a1`` |float|                        Initial strut area as ratio of initial area (=1)
   ``a2`` |float|                        Ratio of residual strut area as inicitial strut area (Final area / Initial Area)
   ``D1`` |float|                        Strain where strut degradation starts (D1<0)(For strain>D1 Area/Initial Area=a1)
   ``D2`` |float|                        Strain where strut degradation ends (D2<0) (For strain <D2 Area/Initial Area=a2)
   ``Ach`` |float|                       Hysteresis parameter(0.3 to 0.6) See Crisafulli's thesis
   ``Are`` |float|                       Strain reloading factor (0.2 to 0.4) See Crisafulli's thesis
   ``Ba`` |float|                        Hysteresis parameter(1.5 to 2.0) See Crisafulli's thesis
   ``Gun`` |float|                       Stiffness unloading factor (1.5 to 2.5) See Crisafulli's thesis   
   ``Gplu`` |float|                      Hysteresis parameter(0.5 to 0.7) See Crisafulli's thesis
   ``Gplr`` |float|                      Hysteresis parameter(1.1 to 1.5) See Crisafulli's thesis
   ``Exp1`` |float|                      Hysteresis parameter(1.5 to 2.0) See Crisafulli's thesis
   ``Exp2`` |float|                      Hysteresis parameter(1.0 to 1.5) See Crisafulli's thesis
   ``IENV`` |int|                        Envelope: =0: Sargin stress-strain envelope descending branch; =1: Parabolic stress-strain envelope descending branch

   ===================================   ===========================================================================

.. seealso::
