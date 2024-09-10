.. include:: sub.txt

===========================
Curved Pipe Element
===========================

A 3D pipe element can be used for piping network similar to :doc:`pipe` for a curved-shape pipe.

The temperature is set through :doc:`setNodeTemperature`.


.. function:: element('Pipe', eleTag, *eleNodes, pipeMatTag, pipeSecTag,  xC, yC, zC, <'-Ti'>, <'-T0', T0>, <'-p', p>, <'-tolWall'>, <'-noThermalLoad'>, <'-noPressureLoad'>)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of two element nodes
   ``pipeMatTag`` |int|                  identifier for previously-defined :doc:`pipeMaterial`
   ``pipeSecTag`` |int|                  identifier for previously-defined :doc:`pipeSection`
   ``x_c``, ``y_C``, ``z_C`` |float|     the coordinates for the center of the curve or the tangent intersection point if the option ``'-Ti'`` is given.
   ``'-Ti'`` |str|                       if the option ``'-TI'`` is provided, the coordinates ``xC``, ``yC``, ``zC`` are for the tangent intersection point, which will be converted internally to the coordinates of the center point.
   ``T0`` |float|                        the stress-free temperature, which must follow the option ``'-T0'`` and will be added to the average temperature for the element. Default is ``0``.
   ``p`` |float|                         the internal pressure, which must follow the option ``'-p'``. The internal pressure will affect the axial deformation for the straight pipe element. Default is ``0``.
   ``'-tolWall'`` |str|                  the tolerance for checking radius and the optional interaction point as a fraction of wall thickness and must follow the option ``'-tolWall'``. Default is ``0.1``.
   ``'-noThermalLoad'`` |str|            Do not include the load due to thermal effects. Default is to include.
   ``'-noPressureLoad'`` |str|           Do not include the load due to internal pressure effects. Default is to include.
   ===================================   ===========================================================================

.. note::

    Only the uniform load is accepted by the pipe elements
    for applying the gravity load. Different to 
    regular :doc:`eleLoad`, the load values are interpreted 
    in the global coordinate system as it's convenient 
    for the curved pipe elements. For example,

    .. code-block:: python

        ops.eleLoad('-ele', *eleTags, '-type', '-beamUniform', wy, wz, wx)

    where ``wy``, ``wz``, and ``wx`` are the member load per length in the global axes.

.. note::

    The element responses can be obtained by

    .. code-block:: python

        res = ops.eleResponse(ele, 'sectionI')
        res = ops.eleResponse(ele, 'sectionC')
        res = ops.eleResponse(ele, 'sectionJ')
        res = ops.eleResponse(ele, 'sectionX', perc)

    where the commands above return
    the section forces at node I, center, node J,
    or any section X.

    - ``perc = -1``: section I, i.e. :math:`\theta = -\theta_0`
    - ``perc = 0``: center section, i.e. :math:`\theta = 0`
    - ``perc = 1``: section I, i.e. :math:`\theta = \theta_0`
    - other ``perc``: section at :math:`\theta = perc \times\theta_0`