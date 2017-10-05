Background subcommands for particles
====================================

.. py:currentmodule:: opensees

These are the subcommnds to add or get particles.

#. :ref:`bg-particle`
#. :ref:`bg-auto`

.. _bg-particle:

particle
--------

.. py:function:: background('particle', gid, areatype, *range, [*initial[, *eleargs]])
   :noindex:
   
   add particles to the background mesh in an area, evey time this command called will create a new particle group

   :param int gid: an id for the particle group to  be created

   :param str areatype: the type of the area where particles are created
      
      * ``'quad'`` -- a quad area
      * ``'tri'`` -- a triangular area
      * ``'line'`` -- a line area
      * ``'point'`` -- a point
      
   :param range: the range of the area
      
      * ``'quad'`` -- ``range = [*p1,*p2,*p3,*p3]``, coordinates of four corner points of the quad
      * ``'tri'`` -- ``range = [*p1, *p2, *p3]``, coordinates of three corner points of the triangle
      * ``'line'`` -- ``range = [*p1, *p2]``, coordinates of two end points of the line
      * ``'point'`` -- ``range = [*p1]``, coordinates of the point
   :type range: list[float]
      
   :param initial: optional initial velocity or pressure

      * initial vel -- ``initial = ['-vel', *vel]``, ``vel`` is a list of velocity values
      * initial pressure -- ``initial = ['-pressure', p]``, ``p`` is a pressure value
   :type initial: list
   :param eleargs: element arguments, see :ref:`available elements <tri-eleargs>`
   :type eleargs: list


.. _bg-auto:

auto
----

.. py:function:: background('auto', gid, *lower, *upper, *vel, *num, *eleargs)
   :noindex:
   
   set up the automatic particles generator, which will fill the area with particles in empty cells. The particle will be added to the last particle group before calling the command. If no particle group, then create a new one.

   :param int gid: an id for an existing particle group
   :param lower: coordinates of lower point of the background mesh domain
   :type lower: list[float]
   :param upper: coordinates of  upper point of the background mesh domain
   :type upper: list[float]
   :param vel: velocity of the new particles
   :type vel: list[float]
   :param num: number of particles in a cell, e.g. [2,2] means 2 by 2 particles in each cell
   :type num: list[float]
   :param eleargs: element arguments, see :ref:`available elements <tri-eleargs>`
   :type eleargs: list
