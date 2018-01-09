.. include:: sub.txt

==========
 recorder
==========

.. class:: recorder()

   The :class:`recorder` object is to monitor what is happening during the
   analysis and generate output for the user.
   A subclass of :class:`tagged` and
   a base class for Recorders.
   Use subclasses to create recorderes.

   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`recorder.automatic`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`
     #. :meth:`recorder.record`


Following are beamIntegration subclasses available in the OpenSees:

.. toctree::
   :maxdepth: 2

   noderecorder
   pvd

.. attribute:: recorder.automatic

   An object attribute (get) |bool|.
   If it's ``True``, the recorder will be called in each time step to
   record outputs. Otherwise, the user should invoke the call.

   ::
   
      if not re.automatic:
          re.record()

	   
     
.. method:: recorder.record()

   Record the outputs. This method will be called automatically
   after the analysis if :attr:`recorder.automatric` is ``True``.

   ::

      re.record()

