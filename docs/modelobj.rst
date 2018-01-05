.. include:: sub.txt

===============================
 model -- Finite-Element Model
===============================

.. class:: model(ndm=2, ndf=3)

   Create a basic OpenSees model. A subclass of :class:`tagged`.

   ========================   ===========================================================================
   ``ndm`` |int|              Number of dimentions. (optional)
   ``ndf`` |int|              Number of dofs per node. (optional)
   ========================   ===========================================================================

   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`model.ndm`
     #. :attr:`model.ndf`
     #. :attr:`model.rayleigh`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`
     #. :meth:`model.wipe`
     #. :meth:`model.reactions`

   .. note::

      After creating a :class:`model`, you must assign it
      to a variable in order to keep it from being destructed.

      If more than one :class:`model` are created, the last created
      one is used.

   ::

      m = model(ndm=2, ndf=2)
      m = model(ndm=3, ndf=6)
     


.. attribute:: model.ndm
      
   An object attribute (get) |int|.
   The number of dimentions of the model.

   ::
   
      print(m.ndm)

.. attribute:: model.ndf

   An object attribute (get/set) |int|.
   The default number of degrees of freedoms per :class:`node`.
	       
   ::
   
      m.ndf = 6
   
.. attribute:: model.rayleigh

   An object attribute (set) |listf|.
   Assign damping to all existing :class:`element` and :class:`node` objects.
   The Rayleigh damping factors are ``[alphaM,betaK,betaKinit,betaKcomm]``, where

   ========================   ====================================================================
   ``alphaM`` |float|         Factor applied to elements or nodes mass matrix.
   ``betaK`` |float|          Factor applied to elements current stiffness matrix.
   ``betaKinit`` |float|      Factor applied to elements initial stiffness matrix.
   ``betaKcomm`` |float|      Factor applied to elements committed stiffness matrix.
   ========================   ====================================================================

   ::

      m.rayleigh = [0.01, 0.02, 0.0, 0.0]

.. method:: model.wipe()

   Wipe all objects in this model including analysis objects. 

   ::

      m.wipe()


.. method:: model.reactions(dynamic=0,rayliegh=0)

   Calculate reactions for all :class:`node` objects in the :class:`model`.

   ========================   =========================================================================
   ``dynamic`` |int|          Include dynamic effects in reactions. (optional)
   ``rayleigh`` |int|         Include rayleigh damping in reactions. (optional)
   ========================   =========================================================================


   ::

      m.reactions(dynamic=1)


