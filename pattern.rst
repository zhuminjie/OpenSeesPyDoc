.. include:: sub.txt

==================
 pattern commands
==================

Use the plain pattern as an example.

The Tcl plain pattern command can be found 
`here <http://opensees.berkeley.edu/wiki/index.php/Plain_Pattern>`_.

The Tcl version of the plain pattern command:

.. code-block:: tcl

   pattern Plain $patternTag $tsTag {
       load $nodeTag $Px $Py
       eleLoad -ele $eleTag1 $eleTag2 -type -beamUniform $Wy
       sp $nodeTag $dofTag $dofValue
   }

The corresponding Python version of the plain pattern command

.. code-block:: python

   pattern('Plain', patternTag, tsTag)
   eleLoad('-ele', eleTag1, eleTag2, '-type', '-beamUniform', Wy)
   load(nodeTag, Py, Py)
   sp(nodeTag, dofTag, dofValue)



As shown above, the Tcl pattern commands include the subcommands,
load, eleLoad, sp, as the last parameter. While this is not possible
in Python, in which subcommands issued after a pattern command are
considered as in that pattern.
