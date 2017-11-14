.. _node-obj:

Node Object
===========

.. index:: object: node

.. class:: node(tag,crds=[],disp=[],vel=[],accel=[],mass=[],ndf=0)

   Create a python node object, which
   is a wrapper to the OpenSees node object.
	   
   When only ``tag`` is given, it creates a wrapper to
   the existing Opensees node with ``tag``.

   If ``ndf`` is given,
   it will override the system ndf set by :func:`model`.
	   
   When ``crds`` is given, number of items in which 
   should be equal to ``ndm`` set by :func:`model`,
   it creates a new OpenSees node object.
	   
   The number of items of ``disp``, ``vel``, ``accel``, ``mass``
   should be equal to ``ndf``.
   


   .. attribute:: tag
      
      An object attribute (get).
      The unique tag of the node object, which is
      same in python and in OpenSees.

   .. attribute:: crds

      An object attribute (get/set).
      A list of nodal coordinates.

   .. attribute:: disp

      An object attribute (get/set).
      A list of nodal displacements

   .. attribute:: vel

      An object attribute (get/set).
      A list of nodal velocities

   .. attribute:: accel

      An object attribute (get/set).
      A list of nodal accelerations

   .. attribute:: mass

      An object attribute (get/set).
      A list of nodal mass.

   .. attribute:: ndf

      An object attribute (get).
      The number of degrees of freedoms of the node.

   .. method:: remove()

      Remove the corresponding OpenSees ``Node`` object.
	       
      .. note::
      
	 The python :class:`node` object is not removed, but
	 any operation on the python :class:`node` object will fail.
	 When you ``del`` a :class:`node` or set it to ``None``,
	 the python :class:`node` object is removed, but
	 the OpenSees ``Node`` is not.

   .. method:: __str__()

      The string reprsentation of the node. Usually
      used in the `print`_ function.

   Examples::

     node(1, crds=[0.0, 0.0], disp=[1.0, 0.0])

     nds = [node(1, crds=[0.0, 0.0],disp=[0.0,0.0]),
            node(2, [72.0, 0.0], vel = [0.0,0.0]),
            node(3, [168.0, 0.0], mass = [0.0, 0.0]),
            node(4, [48.0, 144.0], ndf = 2)]

     for nd in nds:
         nd.disp = [-1.0, -2.0]
	 nd.vel = [50.0, -20.0]
	 nd.accel = [1.9, 2.8]
	 nd.mass = [3.19, 0.12]
	 print(nd.ndf, nd.tag, nd.mass, nd.crds, nd.disp, nd.vel, nd.accel)
	 print(nd)
         nd.remove()

     del nds
   
     nds = {}
     nds[1] = node(1)
     nds[2] = node(2)
     nds[3] = node(3)
     nds[4] = node(4)

     for tag, nd in nds.items():
         print(nd)

.. _print: https://docs.python.org/3/library/functions.html#print
