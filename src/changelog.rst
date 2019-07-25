==============
  Change Log
==============

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
