# FileCopy_Service
Windows service for doing file copies

In this repository and windows service is setup using Python 3.7
Using pyinstaller an executable for the program can be build.

pyinstaller -F --hidden-import=win32timezone WindowsService.py

The service can be called using Python or if an .exe is built using the exe.

Python:
  python WindowsService.py install
  
Using .exe:
  WindowsService.exe install
  
To start the service after install use:
  WindowsService start
  
To stop the service use:
  WindowsService stop
  
To update an installed service use:
  WindowsService update
  
To remove an installed service use:
  WindowsService remoce
