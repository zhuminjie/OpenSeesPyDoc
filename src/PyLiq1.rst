.. include:: sub.txt

===============
PyLiq1 Material
===============

   This command constructs a uniaxial p-y material that incorporates liquefaction effects. This p y material is used with a zeroLength element to connect a pile (beam-column element) to a 2 D plane-strain FE mesh or displacement boundary condition. The p-y material obtains the average mean effective stress (which decreases with increasing excess pore pressure) either from two specified soil elements, or from a time series. Currently, the implementation requires that the specified soil elements consist of FluidSolidPorousMaterials in FourNodeQuad elements, or PressureDependMultiYield or PressureDependMultiYield02 materials in FourNodeQuadUP or NineFourQuadUP elements. There are two possible forms:


.. function:: uniaxialMaterial('PyLiq1', matTag,soilType, pult, Y50, Cd, c, pRes, ele1, ele2)
   :noindex:

.. function:: uniaxialMaterial('PyLiq1', matTag,soilType, pult, Y50, Cd, c, pRes, '-timeSeries', timeSeriesTag)
   :noindex:


   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``soilType`` |int|                    soilType = 1 Backbone of p-y curve approximates Matlock (1970) soft clay relation.
                                         soilType = 2 Backbone of p-y curve approximates API (1993) sand relation.
   ``pult`` |float|                      Ultimate capacity of the p-y material. Note that "p" or "pult" are distributed loads [force per length of pile] in common design equations, but are both loads for this uniaxialMaterial [i.e., distributed load times the tributary length of the pile].
   ``Y50`` |float|                       Displacement at which 50% of pult is mobilized in monotonic loading.
   ``Cd`` |float|                        Variable that sets the drag resistance within a fully-mobilized gap as Cd*pult.
   ``c`` |float|                         The viscous damping term (dashpot) on the far-field (elastic) component of the displacement rate (velocity). (optional Default = 0.0). Nonzero c values are used to represent radiation damping effects
   ``pRes`` |float|                      sets the minimum (or residual) peak resistance that the material retains as the adjacent solid soil elements liquefy
   ``ele1``    ``ele2`` |int|            are the eleTag (element numbers) for the two solid elements from which PyLiq1 will obtain mean effective stresses and excess pore pressures
   ``timeSeriesTag`` |int|               Alternatively, mean effective stress can be supplied by a time series by specifying the text string ``'-timeSeries'`` and the tag of the series    ``seriesTag``.
   ===================================   ===========================================================================

.. note::

   #. The argument ``pult`` is the ultimate capacity of the p-y material. Note that ``p`` or ``pult`` are lateral stresses [force per unit length of pile] in common design equations, but are both loads for this uniaxialMaterial [i.e.,  distributed load times the tributary length of the pile].
   #. Nonzero ``c`` values are used to represent radiation damping effects
   #. To model the effects of liquefaction with ``PyLiq1``, it is necessary to use the ``updateMaterialStage`` command. When material stage is 0 (which is the default value), the ``PyLiq1`` behavior will be independent of any pore pressure in the specified solidElem’s. When material stage is set to 1, the behviour of ``PyLiq1`` will depend on the mean effective stresses (and hence excess pore pressures) in the solidElem’s. 

.. seealso::

   `Notes <https://opensees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/PyLiq1.html>`_
