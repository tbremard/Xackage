import os
import re
import logging
from time import strftime
from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler


class MyLogger:
    def CreateDirectoryIfNeeded(self, dir):
        if not os.path.exists(dir):
            os.makedirs(dir)

    def SetupLogger(self):
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s',)
        _log = logging.getLogger('Fatals_logger')
        _log.setLevel(logging.DEBUG)
        logDirectory = "myLog"
        self.CreateDirectoryIfNeeded(logDirectory )
        handler = RotatingFileHandler(logDirectory +"/Fatals_logs.log", maxBytes=10000000, backupCount=10)
        formatter = logging.Formatter('%(asctime)s [%(levelname)s]  %(message)s')
        handler.setFormatter(formatter)
        _log.addHandler(handler)


    def GetLogger(self):
        _log = logging.getLogger('Fatals_logger')
        return _log


