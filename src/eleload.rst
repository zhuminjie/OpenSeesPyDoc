.. include:: sub.txt

===================
 eleLoad command
===================

.. function:: eleLoad('-ele', *eleTags, '-range', eleTag1, eleTag2, '-type', '-beamUniform', Wy, <Wz>, Wx=0.0, '-beamPoint',Py,<Pz>,xL,Px=0.0,'-beamThermal',*tempPts)

   The eleLoad command is used to construct an ElementalLoad object and add it to the enclosing LoadPattern.

   ========================   =============================================================
   ``eleTags`` |listi|        tag of PREVIOUSLY DEFINED element
   ``eleTag1`` |int|          element tag
   ``eleTag2`` |int|          element tag
   ``Wx`` |float|             mag of uniformily distributed ref load acting in direction
	                      along member length. (optional)
   ``Wy`` |float|             mag of uniformily distributed ref load acting in local y
	                      direction of element
   ``Wz`` |float|             mag of uniformily distributed ref load acting in local z
	                      direction of element. (required only for 3D)
   ``Px`` |float|             mag of ref point load acting in direction along member
	                      length. (optional)
   ``Py`` |float|             mag of ref point load acting in local y direction of element
   ``Pz`` |float|             mag of ref point load acting in local z direction of
	                      element. (required only for 3D)
   ``xL`` |float|             location of point load relative to node I,
	                      prescribed as fraction of element length
   ``tempPts`` |listf|        temperature points:
	                      ``temPts = [T1, y1, T2, y2, ..., T9, y9]``
			      Each point ``(T1, y1)`` define a temperature and
			      location. This command may accept 2,5 or 9
			      temperature points.
   ========================   =============================================================

**Uniform (full span)** — ``NDM`` = 2:

.. code-block:: python

   ops.eleLoad('-ele', eleTag, '-type', '-beamUniform', Wy, Wx)

**Trapezoidal (partial span, 2D)** — intensity varies linearly between normalized positions ``aOverL`` and ``bOverL`` (fraction of length, 0 to 1). Give transverse and axial intensities at start (:math:`W_{ya}`, :math:`W_{xa}`) and end (:math:`W_{yb}`, :math:`W_{xb}`). Supported by 2D ``elasticBeamColumn`` and ``forceBeamColumn``:

.. code-block:: python

   ops.eleLoad('-ele', eleTag, '-type', '-beamUniform',
               Wya, Wxa, aOverL, bOverL, Wyb, Wxb)

**Uniform** — ``NDM`` = 3:

.. code-block:: python

   ops.eleLoad('-ele', eleTag, '-type', '-beamUniform', Wy, Wz, Wx)

For **trapezoidal** loads in 3D, pass ``Wy``, ``Wz``, ``Wx``, ``aOverL``, ``bOverL``, then end values ``Wyb``, ``Wzb``, ``Wxb``. Some 3D ``elasticBeamColumn`` paths may approximate a segment as triangular; combine loads if you need an exact trapezoid.

**Point load** — ``NDM`` = 2:

.. code-block:: python

   ops.eleLoad('-range', eleTag1, eleTag2, '-type', '-beamPoint', Py, xL, Px)

``NDM`` = 3:

.. code-block:: python

   ops.eleLoad('-range', eleTag1, eleTag2, '-type', '-beamPoint', Py, Pz, xL, Px)

.. admonition:: Example

   Uniform span load and a 2D trapezoidal segment from :math:`0.2L` to :math:`0.8L`.

   .. code-block:: python

      import openseespy.opensees as ops

      width = 20.0
      W = 4000.0
      wya, wxa = -0.5, 0.0
      a_over_l, b_over_l = 0.2, 0.8
      wyb, wxb = -1.0, 0.0
      ops.timeSeries('Linear', 1)
      ops.pattern('Plain', 1, 1)
      ops.eleLoad('-ele', 3, '-type', '-beamUniform', -W / width)
      ops.eleLoad('-ele', 4, '-type', '-beamUniform',
                  wya, wxa, a_over_l, b_over_l, wyb, wxb)


.. note::


   #. The load values are reference load values, it is the time series that provides the load factor. The load factor times the reference values is the load that is actually applied to the element.
   #. At the moment, eleLoads do not work with 3D beam-column elements if Corotational geometric transformation is used.
