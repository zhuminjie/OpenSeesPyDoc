.. include:: sub.txt

==========================
 uniaxialMaterial command
==========================

Use the Steel01 material as an example.

The Tcl uniaxialMaterial command can be found 
`here <http://opensees.berkeley.edu/wiki/index.php/Steel01_Material>`_.

The Tcl version of the uniaxialMaterial command:

.. code-block:: tcl

   uniaxialMaterial Steel01 $matTag $Fy $E0 $b 


The corresponding Python version of the uniaxialMaterial command

.. code-block:: python

   uniaxialMaterial('Steel01', matTag, Fy, E0, b)

A more pythonic Python version using a list

.. code-block:: python

   args = [Fy, E0, b]
   uniaxialMaterial('Steel01', matTag, *args)

