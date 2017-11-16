.. OpenSeesPy documentation master file, created by
   sphinx-quickstart on Tue Sep 26 12:56:27 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. include:: docs/sub.txt

The OpenSeesPy Library
======================================

`OpenSees`_, the Open System for `Earthquake Engineering`_ Simulation, is
an `object-oriented`_, `open source`_ software framework.
It allows users to create both serial
and `parallel`_  `Finite Element Analysis`_ computer applications
for simulating the response of structural and geotechnical systems
subjected to `earthquakes`_ and other hazards.
OpenSees is primarily written in `C++`_ and uses
several `Fortran`_ and `C`_ numerical libraries for linear
equation solving, and material and element routines. 


`OpenSeesPy`_ is a `Python`_ 3 interpreter of `OpenSees`_.
In `OpenSeesPy`_, OpenSees objects are wrapped
in `Python`_ objects
and manipulated through `Python`_
object interface. Therefore, users of `OpenSees`_ could
use `object-oriented`_ to write the scripts, which
is very different to the traditional `OpenSees`_
scripts, which are functional.

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



.. toctree::
   :maxdepth: 2
   :numbered: 

   docs/intro
   docs/modelobj
   docs/nodeobj
   docs/spobj
   docs/unimatobj
   docs/elementobj
   docs/timeSeriesobj
   docs/loadobj
   docs/patternobj
   docs/systemobj
   docs/numbererobj
   docs/constraintobj
   docs/integratorobj
   docs/algorithmobj
   docs/ctestobj
   docs/analysisobj
   docs/examples

Indices and tables
==================

* :ref:`genindex`

..   * :ref:`modindex`
..   * :ref:`search`
