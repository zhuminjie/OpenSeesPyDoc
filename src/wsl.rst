.. include:: sub.txt

=============================
 Windows Sybsystem for Linux
=============================

This is a real Linux sybsystem for you
to run OpenSeesPy Linux version on Windows.


Install the Windows Sybsystem for Linux
---------------------------------------

Follow the instruction on `here <https://docs.microsoft.com/en-us/windows/wsl/install-win10>`_
to install Windows Subsystem for Linux on Windows 10.
There are a couple of Linux distributions available and Ubuntu is recommended.
Once the Linux is installed, it will show as an application in the start menu.

.. image:: /_static/start.png


Run OpenSeesPy with Windows Sybsystem for Linux
-----------------------------------------------

- Run the subsystem from start menu and a terminal window will show.

.. image:: /_static/wslterminal.png

- Download Anaconda Linux version

::

   wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh

- Install Anconda Linux version

::

   >> bash Anaconda3-2019.10-Linux-x86_64.sh

   >> Please answer 'yes' or 'no':
   >> yes

   >> Anaconda3 will not be installed into this location:

   [/home/username/anaconda3] >>> (enter)

- Run Anaconda with follwing command,
  where `username` is your username of your computer. Please use
  the `username` shown in last step

::

   ~$ /home/username/anaconda3/bin/python3.7

.. image:: /_static/wslanaconda.png

- 
