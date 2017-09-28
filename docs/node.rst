node
====

.. py:currentmodule:: opensees


.. py:function:: node(nodeTag, *coords, *opts)

   create a node object

   :param int nodeTag: tag of the new node
   :param coords: nodal coordinates, same dimensions defined in :doc:`model`
   :type coords: list[float]
   :param opts: list of optional options,

      * ``'-disp', *disp(list[float])`` -- initial displacements, the number of dofs is either same as the system in :doc:`model` or set by ``'-ndf'``.
      * ``'-vel', *vel(list[float])`` -- initial velocities, the number of dofs is either same as the system in :doc:`model` or set by ``'-ndf'``.
      * ``'-mass', *mass(list[float])`` -- nodal mass, the number of dofs is either same as the system in :doc:`model` or set by ``'-ndf'``.
      * ``'-ndf', ndf(int)`` -- the number of dofs for this node
   :type opts: list
