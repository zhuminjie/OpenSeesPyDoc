.. OpenSeesPy documentation master file, created by
   sphinx-quickstart on Tue Sep 26 12:56:27 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. include:: sub.txt

.. warning::

   The OpenSeesPy library is still in beta version and its
   functions are limited. Please send any questions and
   comments to `zhum@oregonstate.edu <zhum@oregonstate.edu>`_.

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
which can be imported as::

  import sys
  sys.path.append('/path/to/OpenSeesPy')

  from opensees import*

.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Model

   model
   element
   node
   fix
   fixX
   fixY
   fixZ
   equalDOF
   rigidDiaphragm
   rigidLink
   timeSeries
   pattern
   mass

.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Analysis
   
  


.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Examples
      


