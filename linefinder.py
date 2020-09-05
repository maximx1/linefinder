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

for filename in glob.glob(searchterm):
    with open(filename, "r") as f:
        line = f.readline()
        while line:
            line = line.strip()
            if(line.startswith("From: ")):
                print(line[6:])
            line = f.readline()
