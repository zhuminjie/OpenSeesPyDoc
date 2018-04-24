.. include:: sub.txt

===========================
 uniaxialMaterial commands
===========================

.. function:: uniaxialMaterial(matType, matTag, *matArgs)

   This command is used to construct a UniaxialMaterial object which represents uniaxial stress-strain (or force-deformation) relationships.

   ================================   ===========================================================================
   ``matType`` |str|                  material type
   ``matTag`` |int|                   material tag.
   ``matArgs`` |list|                 a list of material arguments, must be preceded with ``*``.
   ================================   ===========================================================================

For example,

.. code-block:: python

   matType = 'Steel01'
   matTag = 1
   matArgs = [Fy, E0, b]
   uniaxialMaterial(matType, matTag, *matArgs)



The following contain information about available ``matType``:

.. toctree::
   :maxdepth: 2
   :caption: Steel & Reinforcing-Steel Materials

   steel01
   steel02
   steel4
   Hysteretic
   ReinforcingSteel
   Dodd_Restrepo
   RambergOsgoodSteel
   SteelMPF


.. toctree::
   :maxdepth: 2
   :caption: Concrete Materials

   Concrete01
   Concrete02
   Concrete04
