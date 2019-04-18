import CephFS

class FileObject:
    
    def __init__(self, cephFS = None, file = '', mode = ''):
        self._cephFS = cephFS.getFileSystem()
        self._path = file
        self._mode = mode
        self._fd = -1

        if self._cephFS.state != 'mounted':
            raise Exception('CephFS is not mounted!')
        
        try:
            self._fd = self._cephFS.open(self._path, self._mode)

        except Exception as ex:
            print(repr(ex))
        

    def close(self):
        self._cephFS.close(self._fd)
        self._fd = -1
    
    def flush(self):
        self._cephFS.sync_fs()
    
    def fileno(self):
        return self._fd

    # To Do, always return false at this stage
    def isatty(self):
        return False

    
    

    

    



