.. include:: sub.txt

===========================
 nDMaterial commands
===========================

.. function:: nDMaterial(matType, matTag, *matArgs)

   This command is used to construct an NDMaterial object which represents the stress-strain relationship at the gauss-point of a continuum element.

   ================================   ===========================================================================
   ``matType`` |str|                  material type
   ``matTag`` |int|                   material tag.
   ``matArgs`` |list|                 a list of material arguments, must be preceded with ``*``.
   ================================   ===========================================================================

For example,

.. code-block:: python

   matType = 'ElasticIsotropic'
   matTag = 1
   matArgs = [E, v]
   nDMaterial(matType, matTag, *matArgs)



The following contain information about available ``matType``:

.. toctree::
   :maxdepth: 2

   elasticIsotropic
