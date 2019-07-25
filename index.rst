.. OpenSeesPy documentation master file, created by
   sphinx-quickstart on Tue Sep 26 12:56:27 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. include:: src/sub.txt

.. important::

   Version |opspy_version| is released.

   OpenSeesPy has been official in `DesignSafe`_.

   The latest version of this document can be found at
   `<https://openseespydoc.readthedocs.io/en/latest/>`_.
   
..
   .. note::

      If you use OpenSeesPy, I would like very much to hear from you. A short email to
      `zhum@oregonstate.edu <zhum@oregonstate.edu>`_
      describing who you are and how you use OpenSeesPy will mean a lot to me.
      I can justify spending time on improvements that I hope will benefit you.


.. note::

   Please send any questions to `github issues <https://github.com/zhuminjie/OpenSeesPyDoc/issues>`_.

   You are very welcome to contribute to OpenSeesPy with new command
   documents and examples
   by sending pull requests
   through `github pulls <https://github.com/zhuminjie/OpenSeesPyDoc/pulls>`_.


========================
 The OpenSeesPy Library
========================
`OpenSeesPy`_ is a `Python 3`_ interpreter of `OpenSees`_.
A minimum script is shown below:

::

   # import OpenSeesPy
   import openseespy.opensees as ops

   # wipe model
   ops.wipe()
   

Most of `OpenSeesPy`_ commands have the same syntax and arguments as the
OpenSees `Tcl commands <http://opensees.berkeley.edu/wiki/index.php/Command_Manual>`_.
The conversion from Tcl to Python is easy and straightforward
as demonstrated with commands below.



.. topic::
   *Minjie Zhu* <`zhum@oregonstate.edu <zhum@oregonstate.edu>`_>

   | Faculty Research Assistant
   | Civil and Construction Engineering
   | Oregon State University

   
.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Contents
      
   src/installation
   src/compile
   src/changelog
   src/modelcmds
   src/analysiscmds
   src/outputcmds
   src/utilitycmds
   src/fsicmds
   src/senscmds
   src/reliabilitycmds
   src/parallelcmds
   src/examples


   

.. raw:: html

   <script type='text/javascript' id='clustrmaps' src='//cdn.clustrmaps.com/map_v2.js?cl=ffffff&w=70&t=n&d=SKQBbxa32RopNU9415W5PDNgdO0XjXnxv2wJdeH0CHw&co=2d78ad&cmo=3acc3a&cmn=ff5353&ct=ffffff'></script>
