#!/usr/bin/env
import os

dupfiles = {}

for dirname, dirs, files in os.walk(','):
  for filename in files:
    if filename in dup_files:
      dupfiles[filename] +=1
    else:
      dupfiles[filename] = 1

print dupfiles
