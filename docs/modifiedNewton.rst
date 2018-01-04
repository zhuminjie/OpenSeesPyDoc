.. include:: sub.txt

modifiedNewton -- Modified Newton Algorithm
================================================

.. class:: modifiedNewton(secant=False,initial=False)

   Create a ModifiedNewton algorithm. The difference to :class:`newton` is that the tangent at the initial guess is used in the iterations, instead of the current tangent. A subclass of :class:`algorithm`.
		 
   See :class:`newton` for parameters.

