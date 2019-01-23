.. include:: sub.txt

=============================
 OpenSeesPy in `DesignSafe`_
=============================

Follow steps below to run OpenSeesPy in `DesignSafe`_.

.. tip::

   * Go To `DesignSafe`_ website and click register

   .. image:: /_static/designsafe.png

.. tip::
   * Register an account for free and log in

   .. image:: /_static/register.png

.. tip::
   * Land on your own portal and go to workspace

   .. image:: /_static/portal.png

.. tip::
   * In your workspace, select ``Jupyter``, launch it, and start my server

   .. image:: /_static/startjupyter.png

.. tip::
   * Now you should be in the ``Jupyter`` Notebook
   * Go to ``mydata`` and alwasy save your data under this folder

   .. image:: /_static/jupyterhome.png


.. tip::
   * In ``mydata`` folder, select ``New`` and then ``Terminal``

   .. image:: /_static/terminal.png


.. tip::
   * The version on DesignSafe is not the latest.
   * To update to the latest:

     * Type ``pip install --user --upgrade openseespy`` in the terminal
     * Check the installation by running ``ipython`` and ``import openseespy.opensees as ops``
     * Everytime you start a new session, you have to update openseespy (this is
       not ideal, but it works for now.
   * Now you may close the terminal by closing the brower tab.

   .. image:: /_static/upgrade.png


.. tip::
   * Back to ``mydata`` folder, select ``New`` and then ``Python 3``

   .. image:: /_static/notebook.png


.. tip::
   * Now you can write OpenSeesPy script in ``Jupyter`` Notebook,
     run the script, and show results
   * To show figure in the Notebook, you should include
     ``%matplotlib inline`` at the beginning

   .. image:: /_static/openseespy.png
      
