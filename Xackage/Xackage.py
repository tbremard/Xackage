import MyLogger
import os
import subprocess
import shutil

myLogger = MyLogger.MyLogger()
myLogger.SetupLogger()
_log = myLogger.GetLogger()
_log.debug('##############################');
_log.debug('##          Starting        ##');

cmdAdb = 'adb'
cmdOpenShell = 'adb shell'
cmdCloseShell = 'exit'
cmdListPackages = 'pm list packages -3'
cmdGetPathOfApk = 'pm path com.skype.raider'

#output=subprocess.run([shutil.which(cmdOpenShell), cmdListPackages, cmdCloseShell], capture_output=True, shell=True)
myPath=shutil.which(cmdAdb)
output=subprocess.run(myPath, capture_output=True, shell=True)
#output=subprocess.run(['dir'], capture_output=True, shell=True)
_log.debug('##############################');
print(output)