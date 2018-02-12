.. OpenSeesPy documentation master file, created by
   sphinx-quickstart on Tue Sep 26 12:56:27 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. include:: sub.txt

.. warning::

   The OpenSeesPy library is still in beta version.
   Please send any questions,
   comments and wishlist to `zhum@oregonstate.edu <zhum@oregonstate.edu>`_.

========================
 The OpenSeesPy Library
========================
`OpenSeesPy`_ is a `Python 3`_ interpreter of `OpenSees`_,
which can be imported as,

::

  import sys
  sys.path.append('/path/to/OpenSeesPy')

  from opensees import*


* :ref:`Installation <installation>`
* :ref:`Available Elements and Materials <availablelib>`
* :ref:`From Tcl to Python <conversion>`
* :ref:`Changed Commands <changedcmds>`
* :ref:`New Commands <newcmds>`
* :ref:`Fluid-Structure Interaction commands <fsicmds>`
* :ref:`Examples <examples>`


.. _installation:

.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Installation

   windows
   linux
   license

.. _availablelib:

.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Available Elements and Materials

   availableEles
   availableUniMats
   availableNDMats


.. _conversion:

.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: From Tcl to Python

   model
   element
   fix
   timeSeries
   pattern
   uniaxialMaterial
   ndMaterial
   section
   geomTransf

Most of `OpenSeesPy`_ commands have the same syntax and arguments as the
OpenSees `Tcl commands <http://opensees.berkeley.edu/wiki/index.php/Command_Manual>`_.
The conversion from Tcl to Python is easy and straightforward
as demonstrated with few commands above.


.. _changedcmds:

.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Changed Commands

   node
   block2D
   block3D
   ForceBeamColumn
   dispBeamColumn
   analyze
   getNodeTags
   getEleTags


.. _newcmds:

.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: New Commands

   pvdRecorder
   beamIntegration

.. _fsicmds:

.. toctree::
  :maxdepth: 2
  :numbered:
  :caption: FSI Commands

  mesh
  remesh
  particle
  pfemIntegrator
  pfemSystem
  pfemTest
  pfemAnalysis


.. _examples:

.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Examples

   truss
   nonlinearTruss
   PortalFrame2d
   dambreak
   elasticobstacle
