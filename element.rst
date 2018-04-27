.. include:: sub.txt

==================
 element commands
==================

.. function:: element(eleType, eleTag, *eleNodes, *eleArgs)

   Create a OpenSees element.

   ================================   ===========================================================================
   ``eleType`` |str|                  element type
   ``eleTag`` |int|                   element tag.
   ``eleNodes`` |listi|               a list of element nodes, must be preceded with ``*``.
   ``eleArgs`` |list|                 a list of element arguments, must be preceded with ``*``.
   ================================   ===========================================================================

For example,

.. code-block:: python

   eleType = 'truss'
   eleTag = 1
   eleNodes = [iNode, jNode]
   eleArgs = [A, matTag]
   element(eleType, eleTag, *eleNodes, *eleArgs)



The following contain information about available ``eleType``:

.. toctree::
   :maxdepth: 2
   :caption: Zero-Length Elements

   ZeroLength
   zeroLengthND
   zeroLengthSection
   CoupledZeroLength
   zeroLengthContact2D
   zeroLengthContactNTS2D
   zeroLengthInterface2D
   zeroLengthImpact3D

.. toctree::
   :maxdepth: 2
   :caption: Truss Elements

   trussEle
   corotTruss

.. toctree::
   :maxdepth: 2
   :caption: Beam-Column Elements

   elasticBeamColumn
   ModElasticBeam2d
   ElasticTimoshenkoBeam
   beamWithHinges
   dispBeamColumn
   ForceBeamColumn
   dispBeamColumnInt
   MVLEM
   SFI_MVLEM

.. toctree::
   :maxdepth: 2
   :caption: Joint Elements

   beamColumnJoint
   ElasticTubularJoint
   Joint2D


.. toctree::
   :maxdepth: 2
   :caption: Link Elements

   twoNodeLink


.. toctree::
   :maxdepth: 2
   :caption: Bearing Elements

   elastomericBearingPlasticity
   elastomericBearingBoucWen
   flatSliderBearing
   singleFPBearing
   TFP
   TripleFrictionPendulum
   multipleShearSpring
   KikuchiBearing
   YamamotoBiaxialHDR
   ElastomericX
   LeadRubberX
   HDR
   RJWatsonEqsBearing
   FPBearingPTV


.. toctree::
   :maxdepth: 2
   :caption: Quadrilateral Elements

   quad
   ShellMITC4
   ShellDKGQ
   ShellDKGT
   ShellNLDKGQ
