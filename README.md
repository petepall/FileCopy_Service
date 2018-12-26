# FileCopy_Service

Windows service for doing file copies

In this repository and windows service is setup using Python 3.7
Using pyinstaller an executable for the program can be build.

## _pyinstaller -F --hidden-import=win32timezone programName.py_

____________________________________________________
The service can be called using Python or if an .exe is built using the exe.

**Python:**


        python WindowsService.py install

**Using .exe:**

       WindowsService.exe install
___________________________________________________
* _To start the service after install use:_

      WindowsService start

* _To stop the service use:_

      WindowsService stop

* _To update an installed service use:_

      WindowsService update

* _To remove an installed service use:_

      WindowsService remoce
