import cephfs

fileSys = cephfs.LibCephFS()

# Load the ceph.conf from the default location. Pass in the path of ceph.conf if it's in a different location.
fileSys.conf_read_file()
fileSys.conf_set("client_permissions", "0")
# Mount the filesystem to the default location "/"
fileSys.mount()

# Make a dir, change the dir, and get the current working dir.
fileSys.mkdir('testDir', 777)
fileSys.chdir('testDir')
fileSys.getcwd()

# Create and write a file
fd = fileSys.open('/testDir/my.txt','w')
fileSys.write(fd,b'Hello World!',-1)
fileSys.close(fd)

# Read and print the content of the file
fileSys.open('/testDir/my.txt', 'r')
content = fileSys.read(fd,-1,10)
print(content)

# Check the metadata of the file
stat = fileSys.fstat(fd)
print(stat)

# Close the file
fileSys.close(fd)

# Remove the file and dir
fileSys.unlink('my.txt')
fileSys.chdir('/')
fileSys.rmdir('testDir')

# Unmount the filesystem
fileSys.unmount()







