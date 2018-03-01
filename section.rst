.. include:: sub.txt

==================
 section commands
==================

Use the fiber section as an example.

The Tcl section command can be found 
`here <http://opensees.berkeley.edu/wiki/index.php/Fiber_Section>`_.

The Tcl version of the section command:

.. code-block:: tcl

   section Fiber $secTag {
       fiber $yLoc $zLoc $A $matTag
   }

The corresponding Python version of the section command

.. code-block:: python

   section('Fiber', secTag)
   fiber(yLoc,zLoc,A,matTag)

As shown above, the Tcl section commands include the subcommands,
fiber, as the last parameter. While this is not possible
in Python, in which subcommands issued after a section command are
considered as in that section.
