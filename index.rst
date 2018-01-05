.. OpenSeesPy documentation master file, created by
   sphinx-quickstart on Tue Sep 26 12:56:27 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. include:: docs/sub.txt

The OpenSeesPy Library
======================================

`OpenSees`_, the Open System for `Earthquake Engineering`_ Simulation, is
an `object-oriented`_, `open source`_ software framework.
It widely uses the class inheritance and object
composition in its design (`McKenna, Scott and Fenves`_).
It allows users to create both serial
and `parallel`_  `Finite Element Analysis`_ computer applications
for simulating the response of structural and geotechnical systems
subjected to `earthquakes`_ and other hazards.
OpenSees is primarily written in `C++`_ and uses
several `Fortran`_ and `C`_ numerical libraries for linear
equation solving, and material and element routines. 


`OpenSeesPy`_ is a `Python`_ 3 interpreter of `OpenSees`_,
which makes an effort to represent
the OO design at the script level.
All user related OpenSees objects are
exported as python objects even the :class:`model`.
Everything users do will be creating objects
and calling object and class methods.
Users
of OpenSees will have a very different
experience in writing OpenSees scirpts in
a more efficient and organized way. 


All functions and objects in `OpenSeesPy`_
accept keywords arguments, which means
the order of keywords arguments can be
arbitrary. But if positional arguments are
given, they should in the order given
in definition. The `OpenSeesPy`_ library
can be imported as::

  import sys
  sys.path.append('/path/to/OpenSeesPy')

  from OpenSees import*

The document is organized in chapters of OpenSees objects.
Every object has its attributes and methods, which
reassemble original OpenSees commands.
For abstract classes such as :class:`element`, :class:`uniaxialMaterial`,
class methods are defined for creating objects of subclasses.

Examples can be found in the last chapter.


.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Model

   docs/tagged
   docs/modelobj
   docs/nodeobj
   docs/elementobj
   docs/spobj
   docs/mpobj
   docs/timeSeriesobj
   docs/patternobj
   docs/loadobj
   docs/eleloadobj
   docs/sectionobj
   docs/meshobj
   docs/regionobj
   docs/unimatobj
   docs/ndmatobj
   docs/geomTransfobj
   docs/beamIntegrationobj
   docs/recorderobj

.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Analysis
   
   docs/analysisobj
   docs/algorithmobj
   docs/constraintobj
   docs/integratorobj
   docs/numbererobj
   docs/systemobj
   docs/ctestobj
   docs/examples

Indices and tables
==================

* :ref:`genindex`

..   * :ref:`modindex`
..   * :ref:`search`
