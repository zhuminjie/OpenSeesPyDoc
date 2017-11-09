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
		  
      The unique tag of the node object, which is
      same in python and in OpenSees.


   .. method:: crds()

      Return a list of nodal coordinates


   .. method:: disp()
	       
      Return a list of nodal displacements

   .. method:: vel()
	       
      Return a list of nodal velocities

   .. method:: accel()
	       
      Return a list of nodal accelerations

   .. method:: mass()
	       
      Return a list of nodal mass

   .. method:: ndf()
	       
      Return the number of degrees of freedoms of the node

   .. method:: remove()

      Remove the corresponding OpenSees node object.
	       
      .. note::
      
	 The python node object is not removed, but
	 any operation on the python node object will fail.

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
         print(nd,nd.tag, nd.crds(), nd.disp(), nd.vel(), nd.accel(), nd.mass(), nd.ndf())
         nd.remove()



.. _print: https://docs.python.org/3/library/functions.html#print
