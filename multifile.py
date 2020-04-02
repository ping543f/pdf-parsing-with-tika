# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 21:19:20 2020

@author: mdsae
"""


import tika
tika.initVM()
from tika import parser
import os

path = 'pdfs/'
files = []
# r = root, d = directories, f = files
for r,d, f in os.walk(path):
    for file in f:
        if '.pdf' in file:
            files.append(file)

for f in files:
    print(f)

def process_file(filename):
    
    file_name = filename
    file_path = path
    print("Currently converting: ", filename )
    parsed = parser.from_file(file_path+file_name)
    f = open("converted_files/" + file_name + ".txt","w+", encoding = "utf-8")
    f.write(parsed["content"])
    print("Conversion done .........")
    f.close()

for singlefile in files:
    process_file(singlefile)
