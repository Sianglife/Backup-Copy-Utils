import time
import shutil
import os
f=open('config.txt','r',errors='ignore')
get=f.readlines()
f.close()
source=get[0][:len(get[0])-1]
target=get[1][:len(get[1])-1]
ext=get[2][:len(get[2])-1]
timeformat=get[3][:len(get[3])-1]
newfilename=target+timeformat+ext
timenow=time.strftime(timeformat, time.localtime())
shutil.copyfile(source,target+timenow+ext)
print("File "+source+" Backup Successful! "+timenow+ext+" in "+target)
os.system('pause')
