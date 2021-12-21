import MyLogger
import CoreObjects
import AdbWrapper

myLogger = MyLogger.MyLogger()
myLogger.SetupLogger()
_log = myLogger.GetLogger()
_log.debug('##############################');
_log.debug('##  Starting Xackage        ##');
_log.debug('##  Thierry Bremard         ##');
_log.debug('##  t.bremard@gmail.com     ##');
_log.debug('Download all ThirdParty packages from Android device.');
_log.debug('Needs Android SDK to be installed and adb.exe in PATH');
adbWrapper = AdbWrapper.AdbWrapper()
packages = adbWrapper.EnumThirdPartyPackages()
_log.debug('Identified '+ str(len(packages))+ ' packages')
for package in packages:
    package.Path = adbWrapper.GetPath(package.Name)
    print(package.Name + ':' + package.Path )