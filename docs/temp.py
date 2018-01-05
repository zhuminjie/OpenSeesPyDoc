import glob
import os.path
import os

for f in glob.glob('**',recursive=True):
    root, ext = os.path.splitext(f)
    head,tail = os.path.split(f)

    if ext == '.rst':
        fd = open(f,'r')
        data = fd.read()
        fd.close()

        fd = open(f,'w')
        
        fd.close()
    break

for f in glob.glob('**',recursive=True):
    root, ext = os.path.splitext(f)
    head,tail = os.path.split(f)

    if ext == '.rst':
        fd = open(f,'r')
        data = fd.read()
        fd.close()

        fd = open(f,'w')
        check = False
        for line in data.split('\n'):
            if check:
                i = line.find('--')
                if i > 0:
                    line = line[:i]
                check = False
                
            if all([ele == '=' for ele in line]):
                check = True
            fd.write(line)

        fd.close()
