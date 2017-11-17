.. include:: sub.txt

Integrator Object
=======================

.. class:: integrator()

   A python :class:`integrator` object
   is a wrapper to the OpenSees ``Integrator`` object.

   .. note::
   
      One cannot create an :class:`integrator` object
      directly, but only through the :ref:`integrator-class-methods`.

      There is only one global :class:`integrator` object.
      Creating another :class:`integrator` object
      will automatically invalid the previous :class:`integrator` objects.

.. _integrator-class-methods:

Class methods
--------------

Static Integrators

#. :meth:`integrator.LoadControl`
#. :meth:`integrator.DisplacementControl`
#. :meth:`integrator.MinUnbalDispNorm`
#. :meth:`integrator.ArcLength`

Transient Integrators

#. :meth:`integrator.CentralDifference`
#. :meth:`integrator.Newmark`
#. :meth:`integrator.HHT`
#. :meth:`integrator.GeneralizedAlpha`
#. :meth:`integrator.TRBDF2`
#. :meth:`integrator.Explicitdifference`
#. :meth:`integrator.PFEM`
	       
.. classmethod:: integrator.LoadControl(incr,numIter=1,minIncr=incr,maxIncr=incr)

   Create a LoadControl :class:`integrator`.

   ========================   =============================================================
   ``incr`` |float|           Load factor increment :math:`\lambda`.
   ``numIter`` |int|          Number of iterations the user would
		              like to occur in the solution algorithm. (optional)
   ``minIncr`` |float|        Min stepsize the user will allow :math:`\lambda_{min}`.
		              (optional)
   ``maxIncr`` |float|        Max stepsize the user will allow :math:`\lambda_{max}`.
		              (optional)
   ========================   =============================================================

   #. The change in applied loads that this causes depends on the active load :class:`pattern` (those load :class:`pattern` not set constant) and the :class:`load` in the load :class:`pattern`. If the only active :class:`load` acting on the ``Domain`` are in load :class:`pattern` with a Linear :class:`timeSeries` with a factor of 1.0, this :class:`integrator` is the same as the classical load control method.
   #. The optional arguments are supplied to speed up the step size in cases where convergence is too fast and slow down the step size in cases where convergence is too slow.

.. classmethod:: integrator.DisplacementControl(nd,dof,incr,numIter=1,dUmin=incr,dUmax=incr)

   Create a DisplacementControl :class:`integrator`.  In an analysis step with Displacement Control we seek to determine the time step that will result in a displacement increment for a particular degree-of-freedom at a node to be a prescribed value.

   ========================   =============================================================
   ``nd`` |node|              :class:`node` whose response controls solution
   ``dof`` |int|              Degree of freedom at the :class:`node`,
		              1 through :attr:`node.ndf`.
   ``incr`` |float|           First displacement increment :math:`\Delta U_{dof}`.
   ``numIter`` |int|          Number of iterations the user would
		              like to occur in the solution algorithm. (optional)
   ``minIncr`` |float|        Min stepsize the user will allow :math:`\Delta U_{min}`.
		              (optional)
   ``maxIncr`` |float|        Max stepsize the user will allow :math:`\Delta U_{max}`.
		              (optional)
   ========================   =============================================================

.. classmethod:: integrator.MinUnbalDispNorm(dlambda1,Jd=1,minLambda=dlambda1,maxLambda=dlambda1,det=False)

   Create a MinUnbalDispNorm :class:`integrator`. 

   ========================   ================================================================
   ``dlambda1`` |float|       First load increment (pseudo-time step) at the first
		              iteration in the next invocation of the analysis command.
   ``Jd`` |int|               Factor relating first load increment at subsequent
		              time steps. (optional)
   ``minLambda`` |float|      Min load increment. (optional)
   ``maxLambda`` |float|      Max load increment. (optional)
   ========================   ================================================================


.. classmethod:: integrator.ArcLength(s,alpha)

   Create a ArcLength :class:`integrator`. In an analysis step with ArcLength we seek to determine the time step that will result in our constraint equation being satisfied.

   ========================   ================================================================
   ``s`` |float|              The arcLength.
   ``alpha`` |float|          :math:`\alpha` a scaling factor on the reference loads.
   ========================   ================================================================


.. classmethod:: integrator.CentralDifference()

   Create a LoadControl :class:`integrator`.

   #. The calculation of :math:`U_t + \Delta t`, is based on using the equilibrium equation at time t. For this reason the method is called an explicit integration method.
   #. If there is no rayleigh damping and the C matrix is 0, for a diagonal mass matrix a diagonal solver may and should be used.
   #. For stability, :math:`\frac{\Delta t}{T_n} < \frac{1}{\pi}`


.. classmethod:: integrator.Newmark(gamma,beta,formD=True)

   Create a Newmark :class:`integrator`.

   ========================   =============================================================
   ``gamma`` |float|          :math:`\gamma` factor.
   ``beta`` |float|           :math:`\beta` factor.
   ``formD`` |bool|           Flag to indicate if use displacement as primary variable.
		              If not, use acceleration. (optional)
   ========================   =============================================================

   #. If the accelerations are chosen as the unknowns and :math:`\beta` is chosen as 0, the formulation results in the fast but conditionally stable explicit Central Difference method. Otherwise the method is implicit and requires an iterative solution process.
   #. Two common sets of choices are
   
      #. Average Acceleration Method (:math:`\gamma=\tfrac{1}{2}, \beta = \tfrac{1}{4}`)
      #. Linear Acceleration Method (:math:`\gamma=\tfrac{1}{2}, \beta = \tfrac{1}{6}`)
      
   #. :math:`\gamma > \tfrac{1}{2}` results in numerical damping proportional to :math:`\gamma - \tfrac{1}{2}`
   #. The method is second order accurate if and only if :math:`\gamma=\tfrac{1}{2}`
   #. The method is unconditionally stable for  :math:`\beta >= \frac{\gamma}{2} >= \tfrac{1}{4}`

.. classmethod:: integrator.HHT(alpha,gamma=1.5-alpha,beta=(2-alpha)^2/4)

   Create a Hilber-Hughes-Taylor (HHT) :class:`integrator`. This is an implicit method that allows for energy dissipation and second order accuracy (which is not possible with the regular :meth:`integrator.Newmark` method). Depending on choices of input parameters, the method can be unconditionally stable.

   ========================   =============================================================
   ``alpha`` |float|          :math:`\alpha` factor.
   ``gamma`` |float|          :math:`\gamma` factor. (optional)
   ``beta`` |float|           :math:`\beta` factor. (optional)
   ========================   =============================================================

   #. Like :meth:`integrator.Newmark` and all the implicit schemes, the unconditional stability of this method applies to linear problems. There are no results showing stability of this method over the wide range of nonlinear problems that potentially exist. Experience indicates that the time step for implicit schemes in nonlinear situations can be much greater than those for explicit schemes.
   #. :math:`\alpha` = 1.0 corresponds to the :meth:`integrator.Newmark` method.
   #. :math:`\alpha` should be between 0.67 and 1.0. The smaller the :math:`\alpha` the greater the numerical damping.
   #. :math:`\gamma` and :math:`\beta` are optional. The default values ensure the method is second order accurate and unconditionally stable when :math:`\alpha` is :math:`\tfrac{2}{3} <= \alpha <= 1.0`. The defaults are:
   
      :math:`\beta = \frac{(2 - \alpha)^2}{4}`
	 
      and
	    
      :math:`\gamma = \frac{3}{2} - \alpha`

.. classmethod:: integrator.GeneralizedAlpha(alphaM,alphaF,gamma=0.5+alphaM-alphaF,beta=(1+alphaM-alphaF)^2/4)

   Create a GeneralizedAlpha :class:`integrator`. This is an implicit method that like the :meth:`integrator.HHT` method allows for high frequency energy dissipation and second order accuracy, i.e. :math:`\Delta t^2`. Depending on choices of input parameters, the method can be unconditionally stable.

   ========================   =============================================================
   ``alphaM`` |float|         :math:`\alpha_M` factor.
   ``alphaF`` |float|         :math:`\alpha_F` factor.
   ``gamma`` |float|          :math:`\gamma` factor. (optional)
   ``beta`` |float|           :math:`\beta` factor. (optional)
   ========================   =============================================================

   #. Like :meth:`integrator.Newmark` and all the implicit schemes, the unconditional stability of this method applies to linear problems. There are no results showing stability of this method over the wide range of nonlinear problems that potentially exist. Experience indicates that the time step for implicit schemes in nonlinear situations can be much greater than those for explicit schemes.
   #. :math:`\alpha_M` = 1.0, :math:`\alpha_F` = 1.0 produces the :meth:`integrator.Newmark` Method.
   #. :math:`\alpha_M` = 1.0 corresponds to the :meth:`integrator.HHT` method.
   #. The method is second-order accurate provided :math:`\gamma = \tfrac{1}{2} + \alpha_M - \alpha_F`
   #. The method is unconditionally stable provided :math:`\alpha_M >= \alpha_F >= \tfrac{1}{2}, \beta>=\tfrac{1}{4} +\tfrac{1}{2}(\gamma_M - \gamma_F)`
   #. :math:`\gamma` and :math:`\beta` are optional. The default values ensure the method is unconditionally stable, second order accurate and high frequency dissipation is maximized.

      The defaults are:
   
      :math:`\gamma = \tfrac{1}{2} + \alpha_M - \alpha_F`
	 
      and
	    
      :math:`\beta = \tfrac{1}{4}(1 + \alpha_M - \alpha_F)^2`

.. classmethod:: integrator.TRBDF2()

   Create a TRBDF2 :class:`integrator`. The TRBDF2 integrator is a composite scheme that alternates between the Trapezoidal scheme and a 3 point backward Euler scheme. It does this in an attempt to conserve energy and momentum, something :meth:`integrator.Newmark` does not always do.

   As opposed to dividing the time-step in 2 as outlined in the `Bathe2007`_, we just switch alternate between the 2 integration strategies,i.e. the time step in our implementation is double that described in the `Bathe2007`_.

.. classmethod:: integrator.Explicitdifference()

   Create a Explicitdifference :class:`integrator`.

   #. When using Rayleigh damping, the damping ratio of high vibration modes is overrated, and the critical time step size will be much smaller. Hence Modal damping is more suitable for this method.
   #. There should be no zero element on the diagonal of the mass matrix when using this method.
   #. Diagonal solver should be used when lumped mass matrix is used because the equations are uncoupled.
   #. For stability, :math:`\Delta t \leq \left(\sqrt{\zeta^2+1}-\zeta\right)\frac{2}{\omega}`


.. classmethod:: integrator.PFEM()

   Create a PFEM :class:`integrator`, which is for Fluid-Structure Interaction
   using PFEM.

	 
Examples
----------

::

   integrator.LoadControl(incr=1.0/Nsteps)

   integrator.DisplacementControl(nd, dof=2, inc=0.1)

   integrator.ArcLenght(s=1.0, alpha=0.1)

   integrator.Newmark(gamma=0.5, beta=0.25)

   integrator.HHT(alpha=0.9)

   integrator.GeneralizedAlpha(alphaM=1.0, alphaF=0.8)

