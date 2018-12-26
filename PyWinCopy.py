'''
    Windows service to copy a file from one location to another
    at a certain interval.
'''
import os
import sys
import time

import servicemanager
import win32serviceutil

import win32service
from ServiceBaseClass.SMWinService import SMWinservice

sys.path += ['filecopy_service/ServiceBaseClass']


class PyWinCopy(SMWinservice):
    _svc_name_ = "PyWinCopy"
    _svc_display_name_ = "Python file copy service"
    _svc_description_ = "Service to copy files from server to local drive"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        while self.isrunning:
            # Copy the files from the server to a local folder
            os.system('robocopy \\tamun020\\reports '
                      'c:\\JIS53_backup /MIR')
            time.sleep(60)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(PyWinCopy)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(PyWinCopy)
