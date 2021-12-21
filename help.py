import os
import shutil
import time

time = time.time()
print(time)

path = input("enter your path")
print(path)

# path = '/Users/parent/Downloads/assets 3'

isExist = os.path.exists(path)
listOfFiles = (os.listdir(path))

for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        NAME = os.path.join(root, name)
        ctime = os.stat(os.path.join(root, name)).st_ctime
        #print(NAME,ctime)
        if ctime + 2592000 < time:
            os.remove(NAME)
    for name in dirs:
        FNAME = os.path.join(root, name)
        Fctime = os.stat(os.path.join(root, name)).st_ctime
        #print(FNAME, Fctime)
        if Fctime + 2592000 < time:
            shutil.rmtree(FNAME)





