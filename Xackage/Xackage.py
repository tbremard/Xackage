import MyLogger

class Xackage(object):
    def __init__(self, adbWrapper):
        self._adbWrapper = adbWrapper
        myLogger = MyLogger.MyLogger()
        self._log = myLogger.GetLogger()

    def PullPackages(self):
        packages = self._adbWrapper.EnumThirdPartyPackages()
        self._log.debug('Identified '+ str(len(packages))+ ' packages to be pulled from device')
        for package in packages:
            package.Path = self._adbWrapper.GetPath(package.Name)
            isPulled = self._adbWrapper.Pull(package)
            self._log.debug(package.Name + ':' + str(isPulled)  )

    def PushPackages(self):
        packages = self._adbWrapper.EnumLocalPackages()
        self._log.debug('Identified '+ str(len(packages))+ ' packages to be pushed to device')




