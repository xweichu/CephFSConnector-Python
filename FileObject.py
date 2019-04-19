import CephFS

class FileObject:
    
    def __init__(self, cephFS = None, file = '', mode = ''):
        self._cephFS = cephFS.getFileSystem()
        self._path = file
        self._mode = mode
        self._fd = -1
        self._seek = 0

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

    def next(self):
        raise Exception('next() not implmented!')
    
    def read(self, size = -1):
        if size == -1:
            result = self._cephFS.read(self._fd, int(self._seek), int(self._cephFS.fstat(self._fd).st_size))
            self._seek = self._cephFS.fstat(self._fd).st_size
            return result

        result = self._cephFS.read(self._fd, int(self._seek), size)
        self._setSeek('r',size)
        return result
        
    
    def seek(self, offset, whence = 0):
        ret = self._cephFS.lseek(self._fd, offset, whence)
        self._seek = ret
        return ret
    
    def tell(self):
        return self._seek
    
    def _setSeek(self, mode, size):
        fileLen = self._cephFS.fstat(self._fd).st_size
        if mode == 'r':
            if (size + self._seek) / fileLen < 1:
                self._seek = size + self._seek
            else:
                self._seek = fileLen

    def write(self):
        raise Exception('next() not implmented!')

            

    

    

    



