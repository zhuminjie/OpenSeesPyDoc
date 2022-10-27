.. include:: sub.txt
   
.. _modalProperties:

modalProperties Command
***********************

|  This command is used to compute the modal properties of a model after an :doc:`eigen`.
|  This command computes the following modal properties:

   *  :math:`m_t` : A vector with the total mass of the structure for each DOF, considering both free and fixed DOFs.
   *  :math:`m_f` : The total mass of the structure, but considering only the masses at free DOFs.
   *  :math:`CoM` : The center of mass.
   *  :math:`gm` : The generalized mass matrix.
   *  :math:`MPF` : The modal participation factors.
   *  :math:`MPM` : The modal participation masses.
   *  :math:`MPMc` : The cumulative modal participation masses.
   *  :math:`MPM\left(\%\right)` : The modal participation masse ratios.
   *  :math:`MPMc\left(\%\right)` : The cumulative modal participation masse ratios.

.. function:: modalProperties(<'-print'>, <'-file', reportFileName>, <'-unorm'>, <'-return'>)

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40
   
   ``'-print'``, |str|, "Optional. If included, a report of the modal properties is printed to the console."
   ``'-file'``, |str|, "Optional. If included, a report of the modal properties is printed to the file ``reportFileName``."
   ``reportFileName``, |str|, "Optional, but mandatory if the -file option is included. Indicates the filename for the report. If the file does not exist, it will be created. If the file exists, it will be overwritten."
   ``'-unorm'``, |str|, "Optional. If included, the computation of the modal properties will be carried out using a displacement-normalized version of the eigenvectors."
   ``'-return'``, |str|, "Optional. If included, a report of the modal properties will be returned as a dict object to Python."

.. admonition:: Return value with ``'-return'``

   .. code:: python

      {
         # list of one int value
         "domainSize": [ndm], 

         # list of lambda values for all modes
         "eigenLambda": [lambdas], 

         # list of omega values for all modes
         "eigenOmega": [omega], 

         # list of frequency values for all modes
         "eigenFrequency": [frequency], 

         # list of period values for all modes
         "eigenPeriod": [period], 

         # list of total mass values, [MX] for 1D, [MX, MY, RMZ] for 2D,  
         # [MX, MY, MZ, MRX, RMY, RMZ] for 3D
         "totalMass": [mass], 

         # list of total mass values for free DOFs, [MX] for 1D, 
         # [MX, MY, RMZ] for 2D,  [MX, MY, MZ, MRX, RMY, RMZ] for 3D
         "totalFreeMass": [mass], 

         # coordinates of mass center, [X] for 1D, [X, Y] for 2D,  
         # [X, Y, Z] for 3D
         "centerOfMass": [center], 

         #
         # modal participation factors for all modes
         #
         
         # for MX direction for 1D, 2D and 3D
         "partiFactorMX": [factor], 

         # for MY direction for 2D and 3D
         "partiFactorMY": [factor], 

         # for MZ direction for 3D
         "partiFactorMZ": [factor], 

         # for RMX direction for 3D
         "partiFactorRMX": [factor], 

         # for RMY direction for 3D
         "partiFactorRMY": [factor], 

         # for RMZ direction for 2D and 3D
         "partiFactorRMX": [factor], 

         #
         # modal participation masses for all modes
         #

         # for MX direction for 1D, 2D and 3D
         "partiMassMX": [mass], 

         # for MY direction for 2D and 3D
         "partiMassMY": [mass], 

         # for MZ direction for 3D
         "partiMassMZ": [mass], 

         # for RMX direction for 3D
         "partiMassRMX": [mass], 

         # for RMY direction for 3D
         "partiMassRMY": [mass], 

         # for RMZ direction for 2D and 3D
         "partiMassRMX": [mass], 

         #
         # modal participation masses (cumulative) for all modes
         #

         # for MX direction for 1D, 2D and 3D
         "partiMassesCumuMX": [mass], 

         # for MY direction for 2D and 3D
         "partiMassesCumuMY": [mass], 

         # for MZ direction for 3D
         "partiMassesCumuMZ": [mass], 

         # for RMX direction for 3D
         "partiMassesCumuRMX": [mass], 

         # for RMY direction for 3D
         "partiMassesCumuRMY": [mass], 

         # for RMZ direction for 2D and 3D
         "partiMassesCumuRMZ": [mass], 

         #
         # modal participation mass ratios (%) for all modes
         #

         # for MX direction for 1D, 2D and 3D
         "partiMassRatiosMX": [mass], 

         # for MY direction for 2D and 3D
         "partiMassRatiosMY": [mass], 

         # for MZ direction for 3D
         "partiMassRatiosMZ": [mass], 

         # for RMX direction for 3D
         "partiMassRatiosRMX": [mass], 

         # for RMY direction for 3D
         "partiMassRatiosRMY": [mass], 

         # for RMZ direction for 2D and 3D
         "partiMassRatiosRMX": [mass], 

         #
         # modal participation mass ratios (%) (cumulative) for all modes
         #

         # for MX direction for 1D, 2D and 3D
         "partiMassRatiosCumuMX": [mass], 

         # for MY direction for 2D and 3D
         "partiMassRatiosCumuMY": [mass], 

         # for MZ direction for 3D
         "partiMassRatiosCumuMZ": [mass], 

         # for RMX direction for 3D
         "partiMassRatiosCumuRMX": [mass], 

         # for RMY direction for 3D
         "partiMassRatiosCumuRMY": [mass], 

         # for RMZ direction for 2D and 3D
         "partiMassRatiosCumuRMX": [mass], 
      }

.. note::
   *  This command can be used only if a previous call to :doc:`eigen` has been performed.
   *  This command has only optional arguments, and they can be given in any order. Note, however, that the only requirement is that the ``reportFileName`` must follow the ``'-file'`` option if used.
   *  The modal properties are computed and stored in the ``Domain`` object, so that they can be accessed later in the :doc:`responseSpectrumAnalysis`.
   *  This command directly accesses the mass matrix of the model, so it accounts for both nodal masses and element's (distributed) masses. And the element mass matrix can be either lumped or consistent.
   *  The global mass matrix is then stored into a temporary sparse matrix storage, so it can be used for both small and large models.
   *  This command can be used for both 2D problems (-ndm = 2, -ndf = 2 or 3) and 3D problems (-ndm = 3, -ndf = 3, 4 or 6). In both cases the algorithm computes rotational masses. If a node has rotational DOFs, the rotational masses account for both the direct rotational masses (i.e. those input by the user at rotational DOFs) and the effect of translational masses gyrating about the center of mass. If a node has no rotational DOF, only the latter is considered.
   *  Only the values in :math:`gm` and :math:`MPF` depend on the normalization of the eigenvectors. This normalization depends on the solver used in the :doc:`eigen`. The default ``'-genBandArpack'`` uses a mass-normalization, so that the :math:`gm` is the identity. On the contrary, the ``'-fullGenLapack'`` uses a displacement-normalization, so that the largest component of the eigenvector is 1. If you use the ``'-genBandArpack'``, but want a displacement-normalization of the eigenvectors, use the ``'-unorm'`` option.

Theory
^^^^^^
|  The eigenvalues :math:`\lambda` and the eigenvectors :math:`\Phi` can be obtained after solving the *generalized eigenvalue problem* for two symmetric matrices :math:`K` (stiffness) and :math:`M` (mass) given by:

.. math::
   \left (K - \lambda M \right ) \Phi = 0

|  The global mass matrix :math:`M` is given by the assembly of :math:`n` elemental and nodal mass matrices :math:`m_e`:

.. math::
   M = \bigwedge_{i=1}^{n}m_e

|  :math:`M` is not necessarily diagonal, because some elemental matrices :math:`m_e` may be consistent. However, the computation of :math:`CoM`, :math:`m_t` and :math:`m_f` requires a lumped version of :math:`M`. The global lumped mass matrix :math:`LM` can be computed by the assembly of a diagonalized version of the elemental mass matrices :math:`m_e`:

.. math::
   LM = \bigwedge_{i=1}^{n}diag\left(m_e\right)

|  :math:`diag\left(m_e\right)` cannot be computed just by summing the summing the components of each row (in beams or solid with higher order interpolation, this would produces negative terms on the diagonal mass matrix that would be unphysical).
|  Instead we use the **HRZ** algorithm [HintonEtAl1976]_, named after the authors Hinton, Rock and Zienkiewicz: *“The procedure of lumping recommended in view of the infinite possibilities offered by condition (5) is to compute the diagonal terms of the consistent mass matrix and then scale these terms so as to preserve the total mass of the element”*.
|  The procedure is as follows:
   
   *  compute :math:`DM`, a vector containing the sum of each row of :math:`m_e`.
   *  compute :math:`SM`, a vector of size=ndf, obtained summing the components in :math:`DM` pertaining to the same DOF (i to ndf). This procedures allows to obtain the total elemental mass for each DOF.
   *  compute :math:`DC`, a vector containing only the diagonal terms in the consistent mass matrix :math:`m_e`.
   *  compute :math:`SC`, a vector of size=ndf, obtained summing the components in :math:`DC` pertaining to the same DOF (i to ndf).
   *  now we can obtain the scale factors for each dof :math:`i` as: :math:`SM_i/SC_i`.
   *  |  scale each diagonal term of the consistent mass matrix :math:`DC_j` using the scale factor of the respective DOF :math:`SM_i/SC_i`:
      |  :math:`diag\left(m_e\right)_j = DC_j \cdot SM_i/SC_i`.

|  The center of mass :math:`CoM` and the total masses :math:`m_t` and :math:`m_f` of the structure, for each node :math:`n` with position :math:`X_n` and each DOF :math:`i`, can now be easily computed from :math:`LM`:

.. math::
   m_{t_i} &= \sum_{n=1}^{Nnodes} LM_{ni}\\
   m_{f_i} &= \sum_{n=1}^{Nnodes} LM_{ni}\quad(\text{if}\:i = free)\\
   CoM_i &= \frac{\sum_{n=1}^{Nnodes} X_{ni} \cdot LM_{ni}}{m_{f_i}} \quad(\text{if}\:i = free)
   
|  The generalized mass matrix is

.. math::
   gm = \Phi^T M \Phi

|  If the default solver is used in the :doc:`eigen` (-genBandArpack), and the option **-unorm** is not used, the eigenvectors are mass-normalized and :math:`gm` will be an identity matrix, i.e. a diagonal matrix whose diagonal entries are = 1, and whose size is :math:`n_m \times n_m` (where :math:`n_m` is the number of requested eigenvalues).


|  The modal participation factor matrix :math:`MPF` is a :math:`n_m \times ndf` matrix (where ndf = 3 in 2D and 6 in 3D), where each row contains the modal participation factors for each DOF. The modal participation factor for a certain mode :math:`i` and DOF :math:`j` indicates how strongly the motion (or rotation) associated to that DOF is represented in the eigenvector :math:`i`

.. math::
   MPF_{ij} = \frac{\Phi_{i}^T M T_j}{gm_{ii}}
   
|  where :math:`T_j` defines the magnitude of the rigid body response to imposed rigid body motion (displacement or infinitesimal rotation) in the DOF :math:`j`. Each :math:`ndf \times 1` block :math:`T_{nj}` corresponds to the node :math:`n` and it is defined as (for the 3D/6DOFs case):

.. math::
   T_{nj} = 
   \begin{pmatrix}
   1 & 0 & 0 & 0 & d_z & -d_z \\
   0 & 1 & 0 & -d_z & 0 & d_x \\
   0 & 0 & 1 & d_y & -d_x & 0 \\
   0 & 0 & 0 & 1 & 0 & 0 \\
   0 & 0 & 0 & 0 & 1 & 0 \\
   0 & 0 & 0 & 0 & 0 & 1
   \end{pmatrix}
   \begin{Bmatrix} 
   e_1 \\
   e_2 \\
   e_3 \\
   e_4 \\
   e_5 \\
   e_6 \\
   \end{Bmatrix}

|  where :math:`e_j` is 1, and all other :math:`e_p\:(\text{with}\:p \neq j)` are 0. :math:`d_x`, :math:`d_y` and :math:`d_z` are the distances of the node :math:`n` coordinates :math:`X_n=\left(x, y, z\right)` from the center of mass :math:`CoM=\left(x_0, y_0, z_0\right)`. Therefore, the modal participation factors accounts for the masses directly input at translational and rotational DOFs, and also the rotational masses given by the translational masses gyrating about the center of mass. Note, in fact, that even if the user does not input any rotational mass, or even if the user uses 3D solid elements with no rotational DOF, the modal participation factors associated to the rotational DOFs may be :math:`\neq 0`.
|  
|  The modal participation mass matrix :math:`MPM` is a :math:`n_m \times ndf` matrix (where ndf = 3 in 2D and 6 in 3D), where each row contains the modal participation masses for each DOF. The modal participation mass for a certain mode :math:`i` and DOF :math:`j` is defined as

.. math::
   MPM_{ij} = \frac{\left(\Phi_{i}^T M T_j\right)^2}{gm_{ii}}
   
|  If the modal participation masses for each mode in a particular DOF are summed, it should give the total mass of the structure for that DOF, exlcluding the masses at fixed DOFs.

.. [HintonEtAl1976] Hinton, E., Rock, T. & Zienkiewicz, O. (1976). “A note on mass lumping and related processes in the Finite element method.” Earthquake Engineering and Structural Dynamics, 13, 9, p. A112.

.. admonition:: Example
   
   The following example shows how to:
   
   *  Use the modalProperties command
   *  Print the results on the console (``'-print'``)
   *  Generate a report file in the current directory (``'-file', 'ModalReport.txt'``)
   *  Use a displacement-normalization for the eigenvectors

   .. code:: python

      modalProperties('-print', '-file', 'ModalReport.txt', '-unorm')
   
   For a complete example that runs an **eigenvalue analysis**, extracts the **modal properties** and runs a **response spectrum analysis**, see the documentation of the :doc:`responseSpectrumAnalysis`

.. admonition:: ReportFile
   
   The generated report file looks like this:
   
   .. code:: text
      
      # MODAL ANALYSIS REPORT
      
      * 1. DOMAIN SIZE:
      # This is the size of the problem: 2 for 2D problems, 3 for 3D problems.
      3
      
      
      * 2. EIGENVALUE ANALYSIS:
      #          MODE        LAMBDA         OMEGA     FREQUENCY        PERIOD
      # ------------- ------------- ------------- ------------- -------------
                    1        7578.8       87.0563       13.8554     0.0721738
                    2       8484.47       92.1112       14.6599     0.0682131
                    3       10518.5        102.56       16.3229     0.0612636
                    4         85779       292.881       46.6134     0.0214531
                    5       89260.1       298.764       47.5498     0.0210306
                    6        101089       317.945       50.6025     0.0197619
                    7   1.71885e+06       1311.05        208.66    0.00479249
      
      
      * 3. TOTAL MASS OF THE STRUCTURE:
      # The total masses (translational and rotational) of the structure
      # including the masses at fixed DOFs (if any).
      #            MX            MY            MZ           RMX           RMY           RMZ
      # ------------- ------------- ------------- ------------- ------------- -------------
                 1600          1600          1600          7200         10000         10000
      
      
      * 4. TOTAL FREE MASS OF THE STRUCTURE:
      # The total masses (translational and rotational) of the structure
      # including only the masses at free DOFs.
      #            MX            MY            MZ           RMX           RMY           RMZ
      # ------------- ------------- ------------- ------------- ------------- -------------
                 1600          1600          1600          7200         10000         10000
      
      
      * 5. CENTER OF MASS:
      # The center of mass of the structure, calculated from free masses.
      #             X             Y             Z
      # ------------- ------------- -------------
                    2           1.5           4.5
      
      
      * 6. MODAL PARTICIPATION FACTORS:
      # The participation factor for a certain mode 'a' in a certain direction 'i'
      # indicates how strongly displacement along (or rotation about)
      # the global axes is represented in the eigenvector of that mode.
      #          MODE            MX            MY            MZ           RMX           RMY           RMZ
      # ------------- ------------- ------------- ------------- ------------- ------------- -------------
                    1       1.20368             0             0             0      0.661418             0
                    2             0      -1.20172             0      0.637456             0             0
                    3             0             0             0             0             0      -2.39705
                    4      0.430981             0             0             0       -1.8352             0
                    5             0      -0.41375             0      -1.83591             0             0
                    6             0             0             0             0             0      0.780575
                    7             0             0      -1.17082             0             0             0
      
      
      * 7. MODAL PARTICIPATION MASSES:
      # The modal participation masses for each mode.
      #          MODE            MX            MY            MZ           RMX           RMY           RMZ
      # ------------- ------------- ------------- ------------- ------------- ------------- -------------
                    1       1418.18             0             0             0        428.21             0
                    2             0       1430.41             0        402.49             0             0
                    3             0             0             0             0             0       9041.23
                    4        181.82             0             0             0       3296.78             0
                    5             0        169.58             0       3338.87             0             0
                    6             0             0             0             0             0       958.755
                    7             0             0       1515.54             0             0             0
      
      
      * 8. MODAL PARTICIPATION MASSES (cumulative):
      # The cumulative modal participation masses for each mode.
      #          MODE            MX            MY            MZ           RMX           RMY           RMZ
      # ------------- ------------- ------------- ------------- ------------- ------------- -------------
                    1       1418.18             0             0             0        428.21             0
                    2       1418.18       1430.41             0        402.49        428.21             0
                    3       1418.18       1430.41             0        402.49        428.21       9041.23
                    4          1600       1430.41             0        402.49       3724.99       9041.23
                    5          1600       1599.99             0       3741.36       3724.99       9041.23
                    6          1600       1599.99             0       3741.36       3724.99       9999.99
                    7          1600       1599.99       1515.54       3741.36       3724.99       9999.99
      
      
      * 9. MODAL PARTICIPATION MASS RATIOS (%):
      # The modal participation mass ratios (%) for each mode.
      #          MODE            MX            MY            MZ           RMX           RMY           RMZ
      # ------------- ------------- ------------- ------------- ------------- ------------- -------------
                    1        88.636             0             0             0        4.2821             0
                    2             0       89.4005             0       5.59014             0             0
                    3             0             0             0             0             0       90.4123
                    4       11.3638             0             0             0       32.9678             0
                    5             0       10.5988             0       46.3732             0             0
                    6             0             0             0             0             0       9.58755
                    7             0             0       94.7214             0             0             0
      
      
      * 10. MODAL PARTICIPATION MASS RATIOS (%) (cumulative):
      # The cumulative modal participation mass ratios (%) for each mode.
      #          MODE            MX            MY            MZ           RMX           RMY           RMZ
      # ------------- ------------- ------------- ------------- ------------- ------------- -------------
                    1        88.636             0             0             0        4.2821             0
                    2        88.636       89.4005             0       5.59014        4.2821             0
                    3        88.636       89.4005             0       5.59014        4.2821       90.4123
                    4       99.9997       89.4005             0       5.59014       37.2499       90.4123
                    5       99.9997       99.9993             0       51.9633       37.2499       90.4123
                    6       99.9997       99.9993             0       51.9633       37.2499       99.9999
                    7       99.9997       99.9993       94.7214       51.9633       37.2499       99.9999

Code Developed by: **Massimo Petracca** at ASDEA Software, Italy
