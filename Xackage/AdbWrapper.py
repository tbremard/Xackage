import os
import subprocess
import shutil
import CoreObjects

class AdbWrapper(object):
    def __init__(self):
        self.cmdAdb = 'adb'
        self.adbArgShell = 'shell'
        self.cmdCloseShell = 'exit'
        self.cmdListPackages = b'pm list packages -3'
        self.cmdGetPathOfApk = 'pm path com.skype.raider'
        self.adbFullPath=shutil.which(self.cmdAdb)

    def EnumThirdPartyPackages(self):
        execResult=subprocess.run([self.adbFullPath, self.adbArgShell], input=self.cmdListPackages, capture_output=True, shell=True)
        packageBulk=execResult.stdout.decode('ascii')
        packageList = packageBulk.splitlines()
        validPackages=[]
        for package in packageList:
            packageName=package.replace('package:', '')
            apk = CoreObjects.Apk(packageName)
            validPackages.append(apk)
        return validPackages

    def GetPath(self, packageName):
        ret = 'xxxxxxx'
        return ret

