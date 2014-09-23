#!/usr/bin/env
# adapted from www.thinkpython.com example
import os

count = 0
for (dirname, dirs, files) in os.walk('.'):
  for filename in files:
    count += 1
    thefile = os.path.join(dirname,filename)
    thesize = str(os.path.getsize(thefile)/1000) + 'k'
    print thesize , thefile

print 'Files: ', count
