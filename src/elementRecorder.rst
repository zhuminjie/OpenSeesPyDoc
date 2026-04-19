.. include:: sub.txt

.. _elementRecorder:

========================
element recorder command
========================

.. function:: recorder('Element','-file',filename,'-xml',filename,'-binary',filename,'-precision',nSD=6,'-timeSeries',tsTag,'-time','-dT',deltaT=0.0,'-closeOnWrite','-ele',*eleTags=[],'-eleRange',startEle,endEle,'-region',regionTag,*args)
   :noindex:

   The Element recorder type records the response of a number of elements at every converged step. The response recorded is element-dependent and also depends on the arguments which are passed to the setResponse() element method.

   ===========================   =====================================================================================================================================================
   ``filename`` |str|            name of file to which output is sent. file output is either in xml format (``'-xml'`` option), 
                                 textual (``'-file'`` option) or binary (``'-binary'`` option) which must pre-exist.
   ``nSD`` |int|                 number of significant digits (optional)
   ``'-time'`` |str|             using this option places domain time in first entry of each data line, default is to have time ommitted, (optional)
   ``'-closeOnWrite'`` |str|     using this option will instruct the recorder to invoke a close on the data handler after every timestep. 
                                 If this is a file it will close the file on every step and then re-open it for the next step. 
                                 Note, this greatly slows the execution time, but is useful if you need to monitor the data during the analysis. (optional) 
   ``deltaT`` |float|            time interval for recording. will record when next step is ``deltaT`` greater than last recorder step. 
                                 (optional, default: records at every time step)
   ``tsTag`` |int|               the tag of a previously constructed TimeSeries, results from node at each time step are added to load factor from series (optional)  
   ``eleTags`` |listi|           list of tags of elements whose response is being recorded (optional)
   ``startEle`` |int|            tag for start node whose response is being recorded (optional)
   ``endEle`` |int|              tag for end node whose response is being recorded (optional)     
   ``regionTag`` |int|           a region tag; to specify all nodes in the previously defined region. (optional)
   ``args`` |list|               arguments which are passed to the setResponse() element method, all arguments must be in string format even for double and integer numbers because internally the setResponse() element method only accepts strings.
   ===========================   =====================================================================================================================================================

.. note::

   The ``setResponse()`` behavior depends on the element type; see the :doc:`element` command.

Recording fiber response
-------------------------

For elements with fiber sections (e.g. **zeroLengthSection**, **forceBeamColumn**, **dispBeamColumn**, **mixedBeamColumn**), you can record a single fiber. Options depend on the uniaxial material’s ``setResponse()`` (common: ``stressStrain``).

Choose the fiber by:

1. **Index** — ``fiber``, index (0 … :math:`N_f-1`), response type.
2. **Location** — ``fiber``, *y*, *z*, response type (closest fiber to section coordinates; 2D bending about *z* still uses *y* and *z*, e.g. ``z = 0``).
3. **Material tag at location** — ``fiber``, *y*, *z*, ``matTag``, response type (disambiguate overlapping fibers).

Prefix with ``section`` for **zeroLengthSection** (one section). For beam–columns use ``section`` *secNum* (integration point 1 … :math:`N_p` from node *I* to *J*), or :ref:`elementRecorderSectionX` with coordinate *x* along the element.

.. code-block:: python

   # zeroLengthSection: fiber near (y, z)
   ops.recorder('Element', '-ele', 1, '-file', 'fiber.out', 'section', 'fiber', 0.1, 0.0, 'stressStrain')

   # Beam-column: section 1, steel fiber at tension face (h = depth)
   h = 0.5
   ops.recorder('Element', '-ele', 1, '-file', 'steelFiber.out', 'section', 1, 'fiber', -h / 2, 0, 2, 'stressStrain')

.. _elementRecorderSectionX:

Recording section response by location (``sectionX``)
-----------------------------------------------------

For beam–columns you can record section quantities by index (``section`` *i*) or by **physical position**: ``sectionX``, *x* with :math:`x \in [0, L]` from node *I* to *J*. OpenSees picks the integration section **closest** to *x*. Remaining tokens match the usual section recorder (e.g. ``deformation``, ``force``, or ``fiber`` …).

.. code-block:: python

   ops.recorder('Element', '-ele', 1, '-file', 'sec25.out', 'sectionX', 25.0, 'deformation')

.. note::

   One *x* per recorder; use multiple recorders for multiple locations.

.. seealso::

   :doc:`Fatigue` (damage recorders).
