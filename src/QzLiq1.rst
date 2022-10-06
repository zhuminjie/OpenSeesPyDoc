.. include:: sub.txt

===============
QzLiq1 Material
===============

   The command constructs a uniaxial q-z material that incorporates liquefaction effects. This q-z material is used with a zeroLength element to connect a pile (beam-column element) to a 2 D plane-strain FE mesh. The q-z material obtains the average mean effective stress (which decreases with increasing excess pore pressure) from two specified soil elements or from the mean effective stress provided explicitly as a timeseries data. Currently, in order to compute the mean effective stress from connected elements, the implementation requires that the specified soil elements consist of FluidSolidPorousMaterials in FourNodeQuad elements. There are two possible forms:


.. function:: uniaxialMaterial('QzLiq1', matTag,soilType, qult, Z50, Cd, c, alpha, ele1, ele2)
   :noindex:

.. function:: uniaxialMaterial('QzLiq1', matTag,soilType, qult, Z50, Cd, c, alpha, '-timeSeries', timeSeriesTag)
   :noindex:


   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``soilType`` |int|                    soilType = 1 Backbone of q-z curve approximates Matlock 
                                         (1970) soft clay relation.

                                         soilType = 2 Backbone of q-z curve approximates API (1993) sand relation.
   ``qult`` |float|                      Ultimate capacity of the q-z material. 
   ``Z50`` |float|                       Displacement at which 50% of qult is mobilized in monotonic loading.
   ``suction`` |float|                   Uplift resistance is equal to suction*qult. 

                                         Default=0.0. The value of suction must be 0.0 to 0.1.

   ``c`` |float|                         The viscous damping term (optional Default = 0.0).
   ``alpha`` |float|                     The constant ``alpha``  defines the extent of non-linearity in element’s capacity and stiffness with excess pore pressure ratio (:math:`r_u`). 
   ``ele1``    ``ele2`` |int|            are the eleTag (element numbers) for the two solid elements from which QzLiq1 will obtain mean effective stresses and excess pore alphasures
   ``timeSeriesTag`` |int|               Alternatively, mean effective stress can be supplied by a time series by specifying the text string ``'-timeSeries'`` and the tag of the series    ``seriesTag``.
   ===================================   ===========================================================================

.. note::

   #. ``qult``: Ultimate capacity of the q-z material. Note that ``q`` or ``qult`` are stresses [force per unit area of pile tip] in common design equations, but are both loads for this uniaxialMaterial [i.e., stress times tip area].
   #. ``Z50``: Displacement at which 50% of qult is mobilized in monotonic loading. Note that Vijayvergiya's relation (``qzType=2``) refers to a "critical" displacement (``zcrit``) at which qult is fully mobilized, and that the corresponding ``z50`` would be 0. ``125zcrit``.
   #. Nonzero ``c`` values are used to represent radiation damping effects   
   #. To model the effects of liquefaction with ``QzLiq1``, it is necessary to use the ``updateMaterialStage`` command. When material stage is 0 (which is the default value), the ``QzLiq1`` behavior will be independent of any pore alphasure in the specified solidElem’s. When material stage is set to 1, the behviour of ``QzLiq1`` will depend on the mean effective stresses (and hence excess pore alphasures) in the solidElem’s. 

.. seealso::

   `Notes <https://opensees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/QzLiq1.html>`_
