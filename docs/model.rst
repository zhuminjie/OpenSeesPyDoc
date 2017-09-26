model
===================

.. py:function:: model(type, opt1, ndm[, opt2, ndf])

   :param str type: Currently there is only one 'basic'
   :param str opt1: must be '-ndm'
   :param int ndm: number of dimensions of the model
   :param str opt2: must be '-ndf'
   :param int ndf: number of degrees of freedoms, defaults to 1, 3 or 6
   :raises SystemError: if ndm is not 1, 2, or 3
