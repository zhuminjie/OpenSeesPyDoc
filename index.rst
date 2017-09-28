.. OpenSeesPy documentation master file, created by
   sphinx-quickstart on Tue Sep 26 12:56:27 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to OpenSeesPy Documentation
======================================

`OpenSeesPy`_ is a `Python 3`_ application of `OpenSees`_
for `Finite Element Analysis`_ together with
other applications in `OpenSees Wiki`_.



OpenSees
--------

OpenSees, the Open System for `Earthquake Engineering`_ Simulation, is
an `object-oriented`_, `open source`_ software framework.
It allows users to create both serial
and `parallel`_  `Finite Element Analysis`_ computer applications
for simulating the response of structural and geotechnical systems
subjected to `earthquakes`_ and other hazards.
OpenSees is primarily written in `C++`_ and uses
several `Fortran`_ and `C`_ numerical libraries for linear
equation solving, and material and element routines. 


OpenSeesPy
----------



In `OpenSeesPy`_, all OpenSees objects are created
and modified through functions defined in the :doc:`docs/opensees`,
which can be imported as::

  import opensees

  import opensees as ops

  from opensees import*

.. _OpenSeesPy: https://github.com/zhuminjie/OpenSeesPyDoc
.. _OpenSees: http://opensees.berkeley.edu/
.. _OpenSees Wiki: http://opensees.berkeley.edu/wiki/index.php/Main_Page
.. _Finite Element Analysis: https://en.wikipedia.org/wiki/Finite_element_method
.. _Python 3: https://docs.python.org/3/
.. _Earthquake Engineering: http://en.wikipedia.org/wiki/Earthquake_engineering
.. _object-oriented: http://en.wikipedia.org/wiki/Object-oriented
.. _parallel: http://en.wikipedia.org/wiki/Parallel_computing
.. _earthquakes: http://en.wikipedia.org/wiki/Earthquakes
.. _C++: http://en.wikipedia.org/wiki/C%2B%2B
.. _Fortran: http://en.wikipedia.org/wiki/Fortran
.. _C: http://en.wikipedia.org/wiki/C_programming_language
.. _open source: http://en.wikipedia.org/wiki/Open_source

The main documentation is organized into a couple sections:


* :ref:`core-docs`
* :ref:`fsi-docs`

.. _core-docs:

.. toctree::
   :maxdepth: 2
   :caption: Core Objects Documentation

   docs/coremodel
   docs/coreanalysis


.. _fsi-docs:

.. toctree::
   :maxdepth: 2
   :caption: Fluid-Structure Interaction Documentation

   docs/mmesh
   docs/bgmesh
   docs/fsiother


.. toctree::
   :hidden:
   :caption: Modules

   docs/opensees


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
