.. OpenSeesPy documentation master file, created by
   sphinx-quickstart on Tue Sep 26 12:56:27 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. include:: sub.txt

.. warning::

   The OpenSeesPy library is still in beta version.
   Please send any questions to `zhum@oregonstate.edu <zhum@oregonstate.edu>`_
   or requests for adding your commands through `github <https://github.com/zhuminjie/OpenSeesPyDoc/pulls>`_.

========================
 The OpenSeesPy Library
========================
`OpenSeesPy`_ is a `Python 3`_ interpreter of `OpenSees`_.
A minimum script is shown below:

::

  import sys

  # for Linux
  sys.path.append('/path/to/OpenSeesPy')

  # for Windows
  sys.path.append('C:/path/to/OpenSeesPy')

  from opensees import*

  # Using OpenSees ...

  # wipe before exiting
  wipe()

Most of `OpenSeesPy`_ commands have the same syntax and arguments as the
OpenSees `Tcl commands <http://opensees.berkeley.edu/wiki/index.php/Command_Manual>`_.
The conversion from Tcl to Python is easy and straightforward
as demonstrated with commands below.

Author
------

.. topic::
   *Minjie Zhu* <`zhum@oregonstate.edu <zhum@oregonstate.edu>`_>

   | Faculty Research Assistant
   | Civil and Construction Engineering
   | Oregon State University

   


.. _installation:

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Installation

   windows
   linux
   license


.. _cmdsmanual:

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Commands Manual

   modelcmds
   analysiscmds
   outputcmds
   utilitycmds
   fsicmds
   senscmds

.. _examples:

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Examples

   structure
   earthquake
   tsunami
   other

.. raw:: html

   <script type='text/javascript' id='clustrmaps' src='//cdn.clustrmaps.com/map_v2.js?cl=ffffff&w=70&t=n&d=SKQBbxa32RopNU9415W5PDNgdO0XjXnxv2wJdeH0CHw&co=2d78ad&cmo=3acc3a&cmn=ff5353&ct=ffffff'></script>
