from sys import argv
import tika
tika.initVM()
from tika import parser
import time
from datetime import datetime

oext = str(datetime.now())
oext = oext.replace(" ","")
oext = oext.replace(":","-")
f = open(argv[1], 'r')
flags = int(argv[2])

print("File name :", argv[1])
print("File is being converted..........\n")

parsed = parser.from_file(argv[1])

w = open("converted_at"+oext+".txt","w+", encoding = "utf-8")
w.write(parsed["content"])   
if flags ==1:
    contents = parsed["content"]
    chunks = contents.split('\n')
    for lines in chunks:
        print(lines)
        time.sleep(.01)
        
print("\nYour file has been converted successfully")

f.close()
w.close()