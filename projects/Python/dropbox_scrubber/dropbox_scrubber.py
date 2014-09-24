#!/usr/bin/env
import os

filelist= {}

for dirname, dirs, files in os.walk('.'):
  for filename in files:
      if filelist.has_key(filename):
          filelist[filename] +=1
      else:
           filelist[filename] = 1

f = open('results.txt','w')
for w in sorted(filelist, key=filelist.get, reverse=True):
     if filelist[w] > 1:
         f.write(w + ' ' + str(filelist[w])+"\n")

f.close
# TODO: screen for counts > 1 and write to a .txt file
