'''
    Windows service to copy a file from one location to another
    at a certain interval.
'''
import sys
import time
from distutils.dir_util import copy_tree

import servicemanager
import win32serviceutil

import win32service
from HelperModules.CheckFileExistance import check_folder_exists, create_folder
from HelperModules.ReadConfig import (check_config_file_exists,
                                      create_config_file, read_config_file)
from ServiceBaseClass.SMWinService import SMWinservice

sys.path += ['filecopy_service/ServiceBaseClass',
             'filecopy_service/HelperModules']


class Jis53Backup(SMWinservice):
    _svc_name_ = "Jis53Backup"
    _svc_display_name_ = "JIS53 backup copy"
    _svc_description_ = "Service to copy files from server to local drive"

    def start(self):
        self.conf = read_config_file()
        if not check_folder_exists(self.conf['dest']):
            create_folder(self.conf['dest'])

        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        while self.isrunning:
            # Copy the files from the server to a local folder
            # TODO: build function to trigger only when a file is changed.
            copy_tree(self.conf['origin'], self.conf['dest'], update=1)
            time.sleep(30)


if __name__ == '__main__':
    if sys.argv[1] == 'install':
        if not check_config_file_exists():
            create_config_file()

    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(Jis53Backup)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(Jis53Backup)
