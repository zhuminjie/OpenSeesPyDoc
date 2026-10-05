.. include:: sub.txt

==============================================================================
Dynamic Lateral Response of a Monopile Foundation Subjected to Lateral Spreading
==============================================================================

#. The source code was developed by `Dr Alessandro Tombari <https://github.com/AntroxEV>`_
   (*University of Exeter*, UK) and **Dr Giovanni Li Destri Nicosia**
   (*COWI A/S*, Denmark).

#. The source code was developed as part of research funded by **COWIfonden**
   under the *Rapid Innovation Initiatives* scheme.

#. This example implements the simplified hybrid p-y spring model for liquefied
   soils proposed by Franke and Rollins (2013), which was originally implemented
   in LPILE Plus v5.0 (Reese et al., 2004).

#. The case study corresponds to Model 3b presented by Franke and Rollins (2013)
   and is based on the experimental tests conducted by Abdoun et al. (2003).

#. The source code is shown below and can also be downloaded
   `here </pyExamples/PilewithDynamicPY_FRANKE_Abdoun2003_MWE.py>`_.

#.  Displacement time-history files are required to run the dynamic analyses. These files are available in the `LATERALSPREAD  <https://github.com/zhuminjie/OpenSeesPyDoc/tree/master/pyExamples/LATERALSPREAD>`_ directory. Download the full folder LATERALSPREAD and add it in the same working directory of the main script. Alternatively, you may want to change the loading path in the main script at lines 88 and 497.

#. Run the source code in your preferred Python environment to reproduce the
   plot and animations presented below.


References
----------

* Abdoun, T., Dobry, R., O'Rourke, T.D., and Goh, S.H. (2003).
  “Pile Response to Lateral Spreads: Centrifuge Modeling.”
  *Journal of Geotechnical and Geoenvironmental Engineering*, 129(10),
  869–878.
  `https://doi.org/10.1061/(ASCE)1090-0241(2003)129:10(869) <https://doi.org/10.1061/(ASCE)1090-0241(2003)129:10(869)>`_.

* Franke, K.W. and Rollins, K.M. (2013).
  “Simplified Hybrid p-y Spring Model for Liquefied Soils.”
  *Journal of Geotechnical and Geoenvironmental Engineering*, 139(4),
  564–576.
  `https://doi.org/10.1061/(ASCE)GT.1943-5606.0000750 <https://doi.org/10.1061/(ASCE)GT.1943-5606.0000750>`_.
  
* Ledezma, C.L. and Bray, J.D. (2010).
  “Probabilistic Performance-Based Procedure to Evaluate Pile Foundations at Sites with Liquefaction-induced Lateral Displacement.”
  *Journal of Geotechnical and Geoenvironmental Engineering*, 136(3),
  464–476.
  `https://ascelibrary.org/doi/10.1061/%28ASCE%29GT.1943-5606.0000226>`_.
  
* Reese, L.C., Wang, S.T., Isenhower, W.M., and Arrellaga, J.A. (2004).
  *LPILE Plus 5.0 Technical Manual*. Ensoft, Austin, Texas.


Model and Results
-----------------


.. list-table::
   :widths: 50 50
   :align: center

   * - .. image:: /_static/PileModel.png
         :alt: Numerical model of the monopile and soil springs
         :align: center
         :width: 80%

     - .. image:: /_static/dynpy_curve_at_z2.0_m.png
            :alt: Franke and Rollins (2013) hybrid p-y relationship at 2.0 m depth
            :align: center
            :width: 80%


.. list-table::
   :widths: 50 50 
   :align: center

   * - .. image:: /_static/pileBM_Dynamic_animation.gif
            :alt: Animated bending moment profile and envelope
            :align: center
            :width: 100%

     - .. image:: /_static/pilePY_Dynamic_animation.gif
            :alt: Animated force-displacement path of the p-y spring at 2.0 m depth
            :align: center
            :width: 100%


 .. image:: /_static/pileD_Dynamic_animation.gif
            :alt: Animated lateral response of the monopile
            :align: center
            :width: 80%


Source Code
-----------

.. literalinclude:: /pyExamples/PilewithDynamicPY_FRANKE_Abdoun2003_MWE.py
   :language: python
   :linenos:
