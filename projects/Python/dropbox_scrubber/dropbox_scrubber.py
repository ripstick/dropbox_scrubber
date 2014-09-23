#!/usr/bin/env
import os

filelist= {}

for dirname, dirs, files in os.walk('.'):
  for filename in files:
      if filelist.has_key(filename):
          filelist[filename] +=1
      else:
           filelist[filename] = 1

# print OrderedDict(sorted(filelist.items(), key=lambda t: t[0]))
for w in sorted(filelist, key=filelist.get, reverse=True):
    print w, filelist[w]
