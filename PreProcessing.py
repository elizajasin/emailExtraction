__author__ = 'elizajasin'

import os

def readData(path):
    data = []
    directory = os.path.normpath(path)
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                f=open(os.path.join(subdir, file),'r')
                a = f.read()
                data.append(a)
                f.close()
    return data

