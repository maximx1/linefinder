import os
import sys
import glob

path = os.getcwd()
searchpattern = "*"

if len(sys.argv) > 1:
    searchpattern = sys.argv[1]
if len(sys.argv) > 2:
    path = sys.argv[2]

searchterm = os.path.join(path, searchpattern)

addresses = []

for filename in glob.glob(searchterm):
    with open(filename, "r") as f:
        line = f.readline()
        while line:
            line = line.strip()
            if(line.startswith("From: ")):
                addresses.append(line[6:])
            if(line.startswith("Delivered-To: ")):
                addresses.append(line[14:])
            if(line.startswith("To: ")):
                addresses.append(line[4:])
            if(line.startswith("Return-Path: ")):
                addresses.append(line[13:])
            line = f.readline()

for address in set(addresses):
    print(address)
