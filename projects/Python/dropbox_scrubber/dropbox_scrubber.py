#!/usr/bin/env
# adapted from www.thinkpython.com example
import os

count = 0
dup_files = {}

#for (dirname, dirs, files) in os.walk('.'):
 # for filename in files:
   # count += 1
    #thefile = os.path.join(dirname,filename)
    #file_int = 1
    #thesize = str(os.path.getsize(thefile)/1000) + 'k'
     #print thesize , thefile

#print 'Files: ', count

for dirname, dirs, files in os.walk(','):
  for filename in files:
    thefile = os.path.join(dirname, filename)
    file_int = 1
    if filename not in dup_files:
      dup_files[filename] = file_int
