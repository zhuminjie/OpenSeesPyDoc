region
======

.. py:currentmodule:: opensees

.. py:function:: region(regTag, *opts)

   create a region with optional arguments

   :param int regTag: tag of the new region
   :param opts: optional list of optional arguments, see :ref:`multiple arguments <region-multi-args>` and :ref:`single arguments <region-single-args>`
   :type opts: list

.. _region-multi-args:

Multiple arguments:

Optional argument list can have any combinations of following arguments:
	       
   * with a list of :doc:`element` tags::

       opts = ['-ele', *eles]

     where ``eles`` is a list of :doc:`element` tags.

   * with a range of :doc:`element` tags::

       opts = ['-eleRange', start, end]

     where  a list of :doc:`element` tags
     is defined by ``range(start,end+1)``.

   * with a list of :doc:`node` tags::

       opts = ['-node', *nds]

     where ``nds`` is a list of :doc:`node` tags.


   * with a range of :doc:`node` tags::

       opts = ['-nodeRange', start, end]

     where  a list of :doc:`node` tags
     is defined by ``range(start,end+1)``.


   * with :doc:`rayleigh`   damping::

       opts = ['-rayleigh', alphaM, betaK, betaK0, betaKc]

.. _region-single-args:

Singular arguments:

Following are arguments for output, which can not be used
with above arguments:

   * get :doc:`node` s::

       opts = ['getNodeTags']

   return a list of :doc:`node` tags (``list[int]``) in the region.

   * get :doc:`element` s::

       opts = ['getEleTags']

   return a list of :doc:`element` tags (``list[int]``) in the region.

   * get connected :doc:`element` s::

       opts = ['getExtraEleTags']

   return a list of extra :doc:`element` tags (``list[int]``) in the region.
