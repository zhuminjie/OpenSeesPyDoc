region
======

.. py:function:: region(regTag, *opts)

   create a region with optional arguments

   :param int regTag: tag of the new region
   :param opts: optional list of optional arguments, see below
   :type opts: list

   Optional argument list can have any combinations of following arguments:
	       
   * with a list of element tags::

       opts = ['-ele', *eles]

     where ``eles`` is a list of element tags.

   * with a range of element tags::

       opts = ['-eleRange', start, end]

     where  a list of element tags
     is defined by ``range(start,end+1)``.

   * with a list of node tags::

       opts = ['-node', *nds]

     where ``nds`` is a list of node tags.


   * with a range of node tags::

       opts = ['-nodeRange', start, end]

     where  a list of node tags
     is defined by ``range(start,end+1)``.


   * with :doc:`rayleigh`   damping::

       opts = ['-rayleigh', alphaM, betaK, betaK0, betaKc]

     
   Following are arguments for output, which can not be used
   with above arguments:

   * get nodes::

       opts = ['getNodeTags']

   return a list of node tags (``list[int]``) in the region.

   * get elements::

       opts = ['getEleTags']

   return a list of element tags (``list[int]``) in the region.

   * get connected elements::

       opts = ['getConnectedEleTags']

   return a list of element tags (``list[int]``), any of which nodes
   are in the region.
