import os
import subprocess
import shutil
import CoreObjects
import time

class AdbWrapper(object):
    def __init__(self):
        self.LocalApkDirectory="ApkDirectory"
        self.cmdAdb = 'adb'
        self.adbArgShell = 'shell'
        self.adbArgPull = 'pull'
        self.adbArgPush = 'install'
        self.cmdCloseShell = 'exit'
        self.cmdListPackages = b'pm list packages -3'
        self.cmdGetPathOfApk = b'pm path '
        self.cmdDisableApkCheck = b'settings put global package_verifier_enable 0'
        self.adbFullPath=shutil.which(self.cmdAdb)
        if(self.adbFullPath==None):
            raise FileNotFoundError('['+self.cmdAdb+'] cannot be found: Ensure Android SDK is installed and in PATH')

    def CreateDirectoryIfNeeded(self, dir):
        if not os.path.exists(dir):
            os.makedirs(dir)

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
        inputcmd = self.cmdGetPathOfApk+packageName.encode('ascii')
        execResult=subprocess.run([self.adbFullPath, self.adbArgShell], input=inputcmd, capture_output=True, shell=True)
        outputBulk=execResult.stdout.decode('ascii')
        fileList = outputBulk.splitlines()
        firstApk = fileList[0]
        ret = firstApk.replace('package:', '').rstrip()
        return ret

    def Pull(self, package):
        self.CreateDirectoryIfNeeded(self.LocalApkDirectory)
        targetLocation= os.path.join(self.LocalApkDirectory,package.Name)+".apk"
        execResult=subprocess.run([self.adbFullPath, self.adbArgPull, package.Path,  targetLocation], capture_output=True, shell=True)
        outputTxt=execResult.stdout.decode('ascii')
        ret = False
        successToken="1 file pulled"
        if(successToken in outputTxt):
            ret = True;
        return ret

    def Push(self, fileName):        
        fileLocation= os.path.join(self.LocalApkDirectory,fileName)
        execResult=subprocess.run([self.adbFullPath, self.adbArgPush, fileLocation], capture_output=True, shell=True)
        outputTxt=execResult.stdout.decode('ascii')
        ret = False
        successToken="Success"
        if(successToken in outputTxt):
            ret = True;
        return ret

    def DisableApkCheck(self):
        inputcmd = self.cmdDisableApkCheck
        execResult=subprocess.run([self.adbFullPath, self.adbArgShell], input=inputcmd, capture_output=True, shell=True)
        outputBulk=execResult.stdout.decode('ascii')

    def EnumLocalPackages(self):
        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(self.LocalApkDirectory):
            for file in f:
                files.append(file)
        return files
