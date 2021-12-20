import MyLogger
import os
import subprocess
import shutil

myLogger = MyLogger.MyLogger()
myLogger.SetupLogger()
_log = myLogger.GetLogger()
_log.debug('##############################');
_log.debug('##  Starting Xackage        ##');
_log.debug('##  Thierry Bremard         ##');
_log.debug('##  t.bremard@gmail.com     ##');
_log.debug('Download all ThirdParty packages from Android device.');
_log.debug('Needs Android SDK to be installed and adb.exe in PATH');
cmdAdb = 'adb'
cmdOpenShell = 'adb shell'
cmdCloseShell = 'exit'
cmdListPackages = b'pm list packages -3'
cmdGetPathOfApk = 'pm path com.skype.raider'
myPath=shutil.which(cmdAdb)
execResult=subprocess.run([myPath, 'shell'], input=cmdListPackages, capture_output=True, shell=True)
_log.debug('##############################');
packageBulk=execResult.stdout.decode('ascii')
packageList = packageBulk.splitlines()
validPackages=[]
for package in packageList:
    packageName=package.replace('package:', '')
    validPackages.append(packageName)
_log.debug('Identified '+ str(len(validPackages))+ ' packages')