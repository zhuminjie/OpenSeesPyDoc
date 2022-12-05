.. include:: sub.txt

==============
  Change Log
==============

* **Version `3.4.0.6 <>`_**
  * Add ``pyversion`` command
  * Add new Series3D material wrapper
  * Add ten-node tetrahedron element
  * Rename ``getFixedNodes``, ``getFixedDOFs``, ``getConstrainedNodes``, ``getConstrainedDOFs``, ``getRetainedNodes``, ``getRetainedDOFs``.

* **Version `3.4.0.5<https://github.com/zhuminjie/OpenSeesPy/tree/v3.4.0.5>`_** (11/29/2022) 

  * update to commit.
  * Fix ElasticBilin.
  * Update SimpleFractureMaterial.
  * Update ASDShellQ4 element.
  * Update LineMesh so that last element nodes not flipped.
  * Update BoucWenMaterial with parallel.
  * Fix ElasticMaterial tangent.
  * ZeroLength not require yaxis input for 2D and 3D models.
  * Add a, b parameter in ENTMaterial.
  * Add material testing command.
  * Add HystereticSmooth and Hysteretic Asym materials.
  * Update ElasticTimoshenkoBeam2D and ElasticTimoshenkoBeam3D
  * Update PM4Sand and PM4Silt materials.
  * Add ConcreteMcftNonlinear5 and ConcreteMcftNonlinear7 materials
  * Add Elastic Isotropic thermal material
  * Add Plate fiber thermal material
  * Add J2PlasticityTermal material
  * Add PlateRebarThermal material
  * Add PlateFromPlaneStressThermal material
  * Add beamWithHinges element
  * Update Parallel and Series materials
  * Update ElasticTubeSection3d 
  * Add HSSSectionIntegration
  * Add FRCC material
  * Add ElasticBDShearSection2d
  * Add ``OpenSeesInfo`` variable
  * Allow strings for section codes in SectionAggregator
  * Add GNG Material
  * Add Orthotropic material wrapper
  * Update PFEM with SSI only structure
  * Add getRVParamTag, getRVValue, gradPerformanceFunction for reliability
  * Add ``'-ele'`` and ``'-node'`` to ``rayleigh`` command
  * Add ``ResponseSpectrumAnalysis`` command
  * Add ``CoulombDamper`` material
  * Add `damping <https://github.com/OpenSees/OpenSees/pull/359>`_
  * Add command ``getPatterns``
  * Add PFEM 3D contact element
  * Add ``'-noFlush'`` option to ``analyze``
  * Add ``ConcentratedPlasticity`` and ``ConcentratedCurvature`` beam integrations

* **Version 3.4.0.2** (7/20/2022)

  * Update to commit `abebbee <https://github.com/OpenSees/OpenSees/tree/abebbeeb5006d9f1c623e713972787eb7db49746>`_.
  * Update sectionForce and sectionDeformation commands.
  * Update Tcl to Python converter.
  * Add IGA to OpenSees.
  * Update reliability commands.
  * Add DuctileFracture material
  * Update mass normalization for full gen lapack eigen solver
  * Add ReeseStiffClayBelowWS, ReeseStiffClayAboveWS, VuggyLimestone, CementedSoil, WeakRock backbone functions
  * Add 2D version of rigidDiaphragm
  * Add ShellNLDKGQ to mesh command
  * Update performanceFunction command
  * Add PythonEvaluator
  * Update startPoint, gradientEvaluator, randomNumberGenerator, searchDirection, meritFunctionCheck, stepSizeRule, rootFinding commands
  * Add runFOSMAnalysis command
  * Add findDesignPoints command
  * Add runFORMAnalysis command
  * Add BoucWenInfill material
  * Add TDConcrete material
  * Add MultiplierMaterial
  * Add TzSimple, PySimple2, SAniSandMS to OpenSeesPy
  * Add SPSW02 to OpenSeesPy
  * Add RegularizedHinge to beam integration
  * Add HystereticAsym and HystereticSmooth materials
  * Add fixedNodes and fixedDOFs commands
  * Add fixed/constrained/retained-Nodes/DOFs commands
  * Add constrainedDOFs and retainedDOFs commands
  * Add getConstraintMatrix command
  * Add timoshenkoBeamColumn element
  * Update NDFiberSection command
  * Update SFI_MVLEM_3D element
  * Update NDFiberSectionWarping2d material
  * Add MaterialBackbone
  * Update GradientInelasticBeamColumn3d
  * Update ElasticBeam2d and 3d

* **Version 3.4.0.1** (12/22/2021)

  * Update to OpenSees version `3.4.0 <https://github.com/OpenSees/OpenSees/releases/tag/v3.4.0>`_ at commit `3b28d0c <https://github.com/OpenSees/OpenSees/commit/3b28d0c8d34e5632e62d313585df8e8656277a5a>`_.
  * Add command for QzSimple2 material
  * Updates to PFEM
  * Add masonry elements
  * Add DBNL3D
  * Update to MixedBeamColumn
  * Add SMA material
  * Update to material test
  * Update to IMKBilin material
  * Update to J2CyclicBoundingSurface model
  * Add InertiaTruss element
  * Add SteelFractureDI material
  * Update to SectionIngegration
  * Update to HystereticMaterial
  * Add PySimple2 and TzSimple2 materials
  * Update to MultiLinear material
  * Add eleType command
  * Add ExpressNewton command
  * Add sectionTag command
  * Update to ASDAbsorbingBoundary3D element
  * Add TDConcrete elements
  * Update to forceBeamColumn
  * Add HSS to section command
  * Add SteelDRC material
  * Add SAniSandMS material
  * Add getNodeLoadTags command
  * Add getNDF command
  * Add startPoint command
  * Add getCrdTransfTags command
  * Add randomNumberGenerator command
  * Add commands for step size rule, function evaluator, and root finding
  * Add gradientEvaluator and performanceFunction commands
  * Add HarmonicSteadyState integrator
  * Add DowelType material
  * Add double membrane plate fiber section

* **Version 3.3.0.0** (6/4/2021)

  * Update to `3.3.0.0 <https://github.com/OpenSees/OpenSees/releases/tag/v3.3.0>`_ at commit `5c925e6 <https://github.com/OpenSees/OpenSees/commit/5c925e6a24bf3fbda58e57dde32cde658b3c5d5b>`_.


* **Version 3.2.2.9** (1/28/2021)

  * The pip installation will only install needed libraries based on the
    Operating System, i.e. Windows, Linux, or Mac. The installation time
    and size are now one third of before.
  * Bug fixes for Pinching4Material, Concrete07, H5DRM,
    RCCircularSectionIntegration, ResponseSpectrumAnalysis,
    PML, FiberSection2d, DriftRecorder,

* **Version 3.2.2.8** (1/8/2021)

  * Linux version is tested with Centos 7, 8, Ubuntu 18.04, 20.04, Fedora, and Debian.
  * Mac version uses MacPorts for installing Python and dependencies.
  * Bug fixes for recorders, FourNodeTetrahedron, ASD_SMA_3K, nodeMass,
  * Add ExpressNewton, RockingBC, CBDI3d, Concrete02IS
  * Update PETSc Solver, ZeroLengthSection, ForceBeamColumn3d, OOHystereticMaterial, SSPbrickUP, HardeningMaterial, BilinearOilDamper, 

* **Version 3.2.2.6** (10/15/2020)

  * OpenSeesPy is available now on Mac, just type `import openseespy.opensees as ops` on the MacOS. Python3.8 is required and HomeBrew Python is strongly recommended.
  * SixNodeTri element by Seweryn
  * PostProcessing package ops_vis by Seweryn
  

* **Version 3.2.2.5** (9/16/2020)

  * Fix a Windows issue for virtual environment

* **Version 3.2.2.4** (9/10/2020)

  * Bug fixes in Truss and ForceBeamColumn2d
  * Adding `ops.__version__` variable
  * Bug fixes in 3D elastic beam
  * Bug fixes in Tri31
  * Adding `ops_vis` module for plotting
  * OpenSees commit b0f6b06

* **Version 3.2.2.3** (8/11/2020)

  * Fix typos in documentation
  * Add `testNorm` and `testIter` commands
  * Add Python3.7 and Python 3.8 support
  * Support latest Anaconda
  * Improvements of ploting commands
  * `ShellDKGT` command
  * Include OpenSees commits upto 380239c on 8/9

* **Version 3.2.2.1** (5/18/2020)

  * add gimmeMCK integrator

* **Version 3.2.2** (5/8/2020)

  * Fix Get_Renderiing tab problem
  * Ship with dependent libraries for more Linux systems

* **Version 3.2.0** (4.17.2020)

  * Add background mesh command
  * Add partition command
  * Add OpenSeesPy test
  * Many bug fixes

* **Version 3.1.5.11** (1.10.2020)

  * Change versioning method. First two digits match the current `OpenSees`_ framework version. The last two digits are the versions for OpenSeesPy.
  * For Windows, only support the Python version that corresponds to the current version of `Anaconda`_.
  * Add openseespy.postprocessing.Get_Rendering 
  * Add '-init' option to Newmark integrator
  * Some function can return empty or one-element lists
  * Spaces in string input will be automatically removed
  * Bug fixes

* **Version 0.5.4**

  * Support Mac
  * Support Python3.7 on Windows and Linux

* **Version 0.5.3**

  * Fix bug in LimitState UniaxialMaterial
  * Automatic trimming spaces for string inputs
  * Some output commands return lists instead of ints, such as nodeDisp etc.

* **Version 0.5.2**

  * Add package openseespy.postprocessing
  * Add setStartNodeTag command
  * modalDamping: bug fixes
  * Add Steel02Fatiuge material
  * Add Concrete02IS material
  * Add HardeningMaterial2 material
  * Add hystereticBackone command
  * Add stiffnessDegradation command
  * Add strengthDegradation command
  * Add unloadingRule command

* **Version 0.4.2019.7**

  * Parallel: the Linux version is enabled with parallel capability
  * Python stream: add no echo
  * Mesh: add CorotTruss
  * TriMesh: can create line elements
  * QuadMesh: can create line and triangular elements
  * Python inputs: more flexible input types
  * Commands: add ExplicitDifference integrator

* **Version 0.3.0**

  * Add logFile command
  * Add partial uniform load fo ForceBeamColumn
  * Add ShellDKGT element
  * Add '-V' option in Newmark and HHT
  * Fix bugs in wipe and Mesh
  * Various PFEM updates
  * Update to OpenSees 3.0.3

* **Version 0.2.0** (`8a3d622 <https://github.com/OpenSees/OpenSees/tree/8a3d6225a14ef52c7711248e1a9e65fe298454c6>`_)

  * OpenSeesPy now can print messages and errors in Jupyter Notebook and other Windows based Python applications
  * Add setParameter command
  * Add nodeDOFs command
  * Add setNumThread and getNumThread commands in a multi-threaded environment
  * Add logFile command
  * printA and prinbB can return matrix and vector as lists
  * Fix bugs in updateMaterialStage
  * PM4Sand improvements
  * Add CatenaryCable element to OpenSeesPy


* **Version 0.1.1** (`f9f45fe <https://github.com/OpenSees/OpenSees/tree/f9f45fe7cf0094cd99fd92c2f794187b42cf9289>`_)

  * Update to OpenSees 3.0.2




* **Version 0.0.7** (`b75db21 <https://github.com/zhuminjie/OpenSees/tree/b75db21028c2dbbca55ea86d081893ff9b0f0be3>`_)

  * Add "2D wheel-rail" element
  * PVD recorder allows to set a path
  * Add "sdfResponse" function for single dof dynamic analysis
  * Fix a bug in Joint2D
  * Fix typo in UCSD UP elements
  * Fix bugs in PressureIndependMultiYield
  * Add JSON print options to some materials and elements
  

* **Version 0.0.6** (`cead6e8 <https://github.com/OpenSees/OpenSees/tree/cead6e858e20b02345a28de379f962b41d0796e9>`_)

  * Add "nonlinearBeamColumn" element for backward compatability
  * Add "updateMaterialStage" function
  * Add "RCCircular" seciton
  * Add "quadr" patch for backward compatibility
  * Fix bugs in "Steel01Thermal" material
  * Fix bugs in Truss
  * Fix bugs in eleNodes function
  * Fix bugs in ZeroLength element
  * Fix bugs in FiberSection2d
  * Fix bugs in PFEMLinSOE

* **Version 0.0.5** (`215c63d <https://github.com/OpenSees/OpenSees/tree/215c63dec501438a166a9be67db0ff1427d316ba>`_)

  * Update to OpenSees 3.0.0
