.. OpenSeesPy documentation master file, created by
   sphinx-quickstart on Tue Sep 26 12:56:27 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. include:: src/sub.txt

.. important::

   Version |opspy_version| is released!

   Mac version is supported!

   OpenSeesPy has been official in :doc:`src/designsafe`.

   The Linux Version of OpenSeesPy can now run on Windows 10 (see :doc:`src/wsl`).

   New plotting commands are added (see :doc:`src/plotcmds`).

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

   # create model
   ops.model('basic', '-ndm', 2, '-ndf', 3)
   

Most of `OpenSeesPy`_ commands have the same syntax and arguments as the
OpenSees `Tcl commands <http://opensees.berkeley.edu/wiki/index.php/Command_Manual>`_.
The conversion from Tcl to Python is easy and straightforward
as demonstrated with commands below.

============
 Developer
============

*Minjie Zhu* <`zhum@oregonstate.edu <zhum@oregonstate.edu>`_>

| Research Associate Post Doc
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
   src/plotcmds
   src/examples


   

.. raw:: html

   <script type='text/javascript' id='clustrmaps' src='//cdn.clustrmaps.com/map_v2.js?cl=ffffff&w=70&t=n&d=SKQBbxa32RopNU9415W5PDNgdO0XjXnxv2wJdeH0CHw'></script>
