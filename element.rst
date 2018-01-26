.. include:: sub.txt

=================
 element command
=================

Use truss as an example.

The Tcl truss command can be found 
`here <http://opensees.berkeley.edu/wiki/index.php/Truss_Element>`_.

The Tcl version of the truss command:

.. code-block:: tcl

   element truss $eleTag $iNode $jNode $A $matTag

The corresponding Python version of the truss command

.. code-block:: python

   element('truss', eleTag, iNode, jNode, A, matTag)

A more pythonic Python version using a list


.. code-block:: python

   eleType = ['truss', eleTag, iNode, jNode]
   eleArgs = [A, matTag]
   element(*eleType, *eleArgs)
