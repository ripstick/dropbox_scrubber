#!/usr/bin/env
import os

dup_files = {}

for dirname, dirs, files in os.walk(','):
  for filename in files:
    dup_files[filename] = dup_files.get(filename, 0) + 1

print dup_files
