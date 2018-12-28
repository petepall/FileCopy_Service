# FileCopy_Service

Windows service for doing file copies

In this repository and windows service is setup using Python 3.7
Using pyinstaller an executable for the program can be build.

## _pyinstaller -F --hidden-import=win32timezone programName.py_

____________________________________________________
The service can be called using Python or if an .exe is built using the exe.

**Python:**


        python JIS53_Backup.py install

**Using .exe:**

       JIS53_Backup.exe install
___________________________________________________
* _To start the service after install use:_

      JIS53_Backup start

* _To stop the service use:_

      JIS53_Backup stop

* _To update an installed service use:_

      JIS53_Backup update

* _To remove an installed service use:_

      JIS53_Backup remove
