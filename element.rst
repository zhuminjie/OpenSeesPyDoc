.. include:: sub.txt

=================
 element command
=================

.. function:: element(eleType, eleTag, *eleNodes, *eleArgs)

   Create a OpenSees element.

   ================================   ===========================================================================
   ``eleType`` |str|                  element type
   ``eleTag`` |int|                   element tag.
   ``eleNodes`` |listi|               a list of element nodes, must be preceded with ``*``.
   ``eleArgs`` |list|                 a list of element arguments, must be preceded with ``*``.
   ================================   ===========================================================================

For example, 

.. code-block:: python

   eleType = 'truss'
   eleTag = 1
   eleNodes = [iNode, jNode]
   eleArgs = [A, matTag]
   element(eleType, eleTag, *eleNodes, *eleArgs)



The following contain information about available ``eleType``:

.. toctree::
   :maxdepth: 2
   :caption: Beam-Column Elements

   ForceBeamColumn
   dispBeamColumn
