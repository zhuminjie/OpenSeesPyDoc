.. include:: sub.txt

=============
 fix command
=============

The Tcl fix command can be found 
`here <http://opensees.berkeley.edu/wiki/index.php/Fix_Command>`_.

The Tcl version of the fix command:

.. code-block:: tcl

   fix $nodeTag 1 1 1

The corresponding Python version of the fix command

.. code-block:: python

   fix(nodeTag, 1,1,1)

A more pythonic Python version using a list

.. code-block:: python

   vals = [1,1,1]
   fix(nodeTag, *vals)

