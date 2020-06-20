import glob
import re
import json
import os
import sys

result_file="resultdata.txt"
b = {}
#print(b)
if len(sys.argv)==2:
    dir = sys.argv[1]
else:
    print("python logParser.py dirToWalkForLogFile")
    exit()
if os.path.exists(result_file):
    f = open(result_file,'r')
    if f is not None:
        for line in f:
            words=line.rstrip('\n').split(',,,')
            b[words[0]]={'header' : words[1],
        'body' : words[2]
        }
else:
    print("data file does not exist! creating the file.")


print(b)

files = glob.glob(dir+"/**/application*.log",recursive=True)
print(files)
a = {}
for data_file in files:
    f = open(data_file,'r')
    for line in f:
        #print(line.rstrip())
        if "url=" in line:
            url = re.search(r'url=(.*?) headers->', line).group(1)
            if url in b.keys() or url in a.keys():
                pass
            else:
                header = re.search(r'headers-> (.*?) Body->', line).group(1)
                body = re.search(r'Body-> (.*?)$', line).group(1)
                a[url]={'header':header,'body':body}
    
f = open(result_file,'a+')
for key,value in a.items():
    data = "{},,,{},,,{}\n".format(key,a[key]['header'],a[key]['body'])
    f.write(data)

f.close()
