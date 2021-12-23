import MyLogger
import CoreObjects
import AdbWrapper
import Xackage
import sys

myLogger = MyLogger.MyLogger()
myLogger.SetupLogger()
_log = myLogger.GetLogger()
_log.debug('##############################');
_log.debug('##  Xackage                 ##');
_log.debug('##  Thierry Bremard         ##');
_log.debug('##  t.bremard@gmail.com     ##');
_log.debug('Download all ThirdParty packages from Android device.');
_log.debug('Needs Android SDK to be installed and adb.exe in PATH');

if(len(sys.argv)==1):
    _log.error(sys.argv[0] + " <push|pull> [<apkDir>]")
    exit(-1)
function = sys.argv[1]
targetDir = None
if(len(sys.argv)>2):
    targetDir = sys.argv[2]  
try:
    adbWrapper = AdbWrapper.AdbWrapper()
except FileNotFoundError as ex:
    _log.error(ex.args)
    exit(-1)
if(targetDir != None):
    adbWrapper.LocalApkDirectory=targetDir
_log.debug('LocalApkDirectory: ' +adbWrapper.LocalApkDirectory)
xackage = Xackage.Xackage(adbWrapper)
if("pull" in function):
    xackage.PullPackages()
elif ("push" in function):
    xackage.PushPackages()
else:
    _log.error("Unknown function: "+function)