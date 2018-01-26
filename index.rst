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



.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Conversion from Tcl to Python
      
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


.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: New Commands

   mesh
   pvdRecorder
   pfemIntegrator
   pfemSystem
   pfemTest
   pfemAnalysis
   beamIntegration

.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Tutorials

   truss
   nonlinearTruss

