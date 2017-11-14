.. OpenSeesPy documentation master file, created by
   sphinx-quickstart on Tue Sep 26 12:56:27 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

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


`OpenSeesPy`_ is a `Python`_ interpreter of `OpenSees`_.
In `OpenSeesPy`_, OpenSees objects are wrapped
in `Python`_ objects
and manipulated through `Python`_
object interface. Therefore, users of `OpenSees`_ could
use `object-oriented`_ to write the scripts, which
is very different to the traditional `OpenSees`_
scripts, which are functional.
Global built-in functions
are also provided to
get and set information about
the program.

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

.. _OpenSeesPy: https://github.com/zhuminjie/OpenSeesPyDoc
.. _OpenSees: http://opensees.berkeley.edu/
.. _OpenSees Wiki: http://opensees.berkeley.edu/wiki/index.php/Main_Page
.. _Finite Element Analysis: https://en.wikipedia.org/wiki/Finite_element_method
.. _Python: https://docs.python.org/3/
.. _Earthquake Engineering: http://en.wikipedia.org/wiki/Earthquake_engineering
.. _object-oriented: http://en.wikipedia.org/wiki/Object-oriented
.. _parallel: http://en.wikipedia.org/wiki/Parallel_computing
.. _earthquakes: http://en.wikipedia.org/wiki/Earthquakes
.. _C++: http://en.wikipedia.org/wiki/C%2B%2B
.. _Fortran: http://en.wikipedia.org/wiki/Fortran
.. _C: http://en.wikipedia.org/wiki/C_programming_language
.. _open source: http://en.wikipedia.org/wiki/Open_source

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
   docs/patternobj

Indices and tables
==================

* :ref:`genindex`

..   * :ref:`modindex`
..   * :ref:`search`
