background
==========

.. py:currentmodule:: opensees

.. py:function:: background(subcmd[,*opt])

   set up background mesh method

   :param str subcomd: see available :ref:`subcommands <bg-subcmds>`.
   :param opt: subcommand specific options
   :type opt: list


.. _bg-subcmds:

Categories of subcommands:

#. :ref:`bg-meshcmds`
#. :ref:`bg-particlecmds`
#. :ref:`bg-recordercmds`

      
.. _bg-meshcmds:

mesh commands:
--------------

These are subcommands to set up the background mesh domain and boundaries.

#. :ref:`bg-meshsize`
#. :ref:`bg-variableMesh`
#. :ref:`bg-fix`
#. :ref:`bg-structuralNodes`
#. :ref:`bg-notStructuralEleNodes`

.. _bg-meshsize:

meshsize
^^^^^^^^

.. py:function:: background('meshsize', size, *lower, *upper)
   
   set the basic mesh size and domain size for background mesh, must be called before other subcommands

   :param float size: mesh size
   :param lower: coordinates of lower point of the background mesh domain
   :type lower: list[float]
   :param upper: coordinates of  upper point of the background mesh domain
   :type upper: list[float]


.. _bg-variableMesh:

variableMesh
^^^^^^^^^^^^

.. py:function:: background('variableMesh', level, *lower, *upper)
   
   set up an area with variable mesh size

   :param int level: the highest level for coarser mesh sizes, :math:`h = \frac{h_0}{2^{level}}`.
   :param lower: coordinates of lower point of the variable mesh domain
   :type lower: list[float]
   :param upper: coordinates of  upper point of the variable mesh domain
   :type upper: list[float]

.. _bg-fix:

fix
^^^^^^^^^^^^

.. py:function:: background('fix', btype, *range, *args)
   
   set up the boundary condition for the background mesh

   :param str btype: the boundary type
      
      * ``'p'`` -- a point
      * ``'x'`` -- a line along x axis
      * ``'y'`` -- a line along y axis
      * ``'rect'`` -- a rectangular area
   :param range: the range of the boundary
      
      * ``'p'`` -- ``range = [*pcoords]``, ``pcoords`` is the coordinate of the point
      * ``'x'`` -- ``range = [x, y1, y2]``, ``x`` is the x coordinate of the line and ``y1, y2`` is the starting and end point the line
      * ``'y'`` -- ``range = [y, x1, x2]``, ``y`` is the y coordinate of the line and ``x1, x2`` is the starting and end point the line
      * ``'rect'`` -- ``range = [*lower, *upper]``, lower and upper coordinates of the rectangle
   :type range: list[float]
   :param args: the fixity for fixed boundary or values for velocity and pressure boundaries
      
      * fixed boundary -- ``args`` is a list of 1 and 0
      * velocity boundary -- ``args = ['-vel', *vals]``, ``vals`` is a list velocity values
      * pressure boundary -- ``args = ['-pressure', p]``, ``p`` is the pressure values
   :type upper: list


.. _bg-structuralNodes:

structuralNodes
^^^^^^^^^^^^^^^

.. py:function:: background('structuralNodes', *snds)
   
   add existing nodes as a group of structural nodes, FSI will perform
   between the structural nodes and background mesh.

   :param snds: tags of a group of structural nodes
   :type snds: list[int]


.. _bg-notStructuralEleNodes:

notStructuralEleNode
^^^^^^^^^^^^^^^^^^^^

.. py:function:: background('notStructuralElesNodes', *snds)
   
   indicate that some area between structural nodes do not really belong
   to the structure.

   :param snds: every three nodes form a triangular are that does not belong to the structure
   :type snds: list[int]

.. _bg-particlecmds:
      
particle commands:
------------------

These are the subcommnds to add or get particles.

#. :ref:`bg-particle`
#. :ref:`bg-auto`
#. :ref:`bg-addParticles`
#. :ref:`bg-getParticles`

.. _bg-particle:

particle
^^^^^^^^

.. py:function:: background('particle', areatype, *range, [*initial], *eleargs)
   
   add particles to the background mesh in an area, evey time this command called will create a new particle group

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
^^^^^

.. py:function:: background('auto', *lower, *upper, *vel, *num, *eleargs)
   
   set up the automatic particles generator, which will fill the area with particles in empty cells. The particle will be added to the last particle group before calling the command. If no particle group, then create a new one.

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


.. _bg-addParticles:

addParticles
^^^^^^^^^^^^

.. py:function:: background('addParticles', *coords)
   
   add multiple particles by their coordinates to the last particle group in the system, if no group, quit.

   :param coords: coordinates of particles to be added
   :type coords: list[float]


.. _bg-getParticles:

getParticles
^^^^^^^^^^^^

.. py:function:: background('getParticles', groupno)
   
   read coordinates of particles in a group and return

   :param int groupno: a group number, from ``0`` to ``numgroup-1``
   :return: coordinates of particles
   :rtype: list[float]


.. _bg-recordercmds:

      
recorder commands:
------------------

These are the subcommands to create recorders.

#. :ref:`bg-pvdRecorder`
#. :ref:`bg-nodeRecorder`
#. :ref:`bg-waveRecorder`


      

.. _bg-pvdRecorder:

pvdRecorder
^^^^^^^^^^^

.. py:function:: background('pvdRecorder', *args)

   create the pvd recorder for background mesh

   :param args: same as in :ref:`PVD-Recorder`
   :type args: list


.. _bg-nodeRecorder:

nodeRecorder
^^^^^^^^^^^^

.. py:function:: background('nodeRecorder', *args)

   create the node recorder for background mesh

   :param args: same as in :ref:`Node-Recorder`
   :type args: list


.. _bg-waveRecorder:

waveRecorder
^^^^^^^^^^^^

.. py:function:: background('waveRecorder', filename[, '-dT', dT[, *locs]])

   create the wave recorder for background mesh to record wave height and velocity, as well as the time steps and number iterations.
   
   :param str filename: the filename for wave recorder
   :param float dT: the minimum time step to record
   :param locs: the coordinats of locations to record wave height and velocity
   :type locs: list[float]
