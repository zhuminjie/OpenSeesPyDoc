remesh
======

.. py:currentmodule:: opensees

.. py:function:: remesh(type, alpha, numf, *frtags, numfi, *firtags[, *eleargs])

   remesh :doc:`node` s in :doc:`region` s to create new :doc:`element` s

   :param str type: remesh type, see :ref:`available types <remesh-types>`
   :param float alpha: the alpha parameter for `Alpha shape`_
   :param int numf: number of :doc:`region` s which contain freely moving nodes
   :param frtags: tags of above free :doc:`region` s
   :type frtags: list[int]
   :param int numfi: number of :doc:`region` s which contain fixed nodes
   :param firtags: tags of above fixed regions
   :type firtags: list[int]
   :param eleargs: element arguments, see :ref:`available triangular elements <tri-eleargs>`
   :type eleargs: list

.. _remesh-types:

Available remesh types

#. :ref:`Tri-ReMesh`

.. _Tri-ReMesh:

Triangular Remesh
-----------------

.. py:function:: remesh('tri', alpha, numf, *frtags, numfi, *firtags[, *eleargs])

   remesh :doc:`node` s in :doc:`region` s to create new :doc:`element` s

   :param eleargs: element arguments, see :ref:`available triangular elements <tri-eleargs>`
   :type eleargs: list

.. _Alpha shape: https://en.wikipedia.org/wiki/Alpha_shape
