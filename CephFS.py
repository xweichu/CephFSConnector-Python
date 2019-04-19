import cephfs

# Configure CephFS and mount the CephFS.
# Only implemented simple CephFS management functions
# More implementations later
class CephFS:

    def __init__(self, confFilePath = None, clientPermission = '0'):
        self._fileSys = cephfs.LibCephFS()
        self._fileSys.conf_read_file()
        self._fileSys.conf_set('client_permissions', clientPermission)
        self._mounted = False
        
        if self._fileSys.state != 'mounted':
            try:
                self._fileSys.mount()
                self._mounted = True
            except Exception as ex:
                print(repr(ex))
    
    def getFileSystem(self):
        return self._fileSys
    
    def mount(self):
        self._fileSys.mount()
        self._mounted = True
    
    def unmount(self):
        self._fileSys.unmount()
        self._mounted = False

    def isMounted(self):
        return self._mounted

    