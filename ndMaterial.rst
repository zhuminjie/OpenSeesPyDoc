.. include:: sub.txt

=====================
 nDMaterial commands
=====================

Use the ElasticIsotropic material as an example.

The Tcl nDMaterial command can be found 
`here <http://opensees.berkeley.edu/wiki/index.php/Elastic_Isotropic_Material>`_.

The Tcl version of the nDMaterial command:

.. code-block:: tcl

   nDMaterial ElasticIsotropic $matTag $E $v 

The corresponding Python version of the nDMaterial command

.. code-block:: python

   nDMaterial('ElasticIsotropic', matTag, E, v)

A more pythonic Python version using a list

.. code-block:: python

   args = [E, v]
   nDMaterial('ElasticIsotropic', matTag, *args)

