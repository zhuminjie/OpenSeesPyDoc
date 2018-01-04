.. include:: sub.txt

=================================
 tagged -- OpenSeesPy Base Class
=================================


.. class:: tagged()

   The base class to be inherited by other classes.
   No object can be created.


   * attributes

   #. :attr:`tagged.tag`

   * methods

   #. :meth:`tagged.__str__`
   #. :meth:`tagged.remove`



.. attribute:: tagged.tag
      
   An object attribute (get) |int|.
   The tag of a tagged object.

.. method:: tagged.__str__

   The string reprsentation of the object. Usually
   used in the |print| function.

.. method:: tagged.remove()

   Remove the corresponding OpenSees  object.

   .. note::
      
      By calling :meth:`tagged.remove`, 
      the python object is not removed, but
      any operation on the python object will fail.
      However, when you |del| a python object or set it to |None|,
      the python object is removed, but
      the OpenSees object is not.
