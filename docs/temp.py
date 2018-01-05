import glob
import os.path
import os



for f in glob.glob('**',recursive=True):
    root, ext = os.path.splitext(f)
    head,tail = os.path.split(f)

    if ext == '.rst':
        print(f)

        fd = open(f,'r')
        data = fd.read()
        fd.close()

        fd = open(f,'w')
        check = False
        found = False
        for line in data.split('\n'):
            if not found:
                if check:
                    i = line.find('--')
                    if i > 0:
                        line = line[:i]
                        found = True
                
                if all([ele == '=' for ele in line]):
                    check = True
                            
            fd.write(line+'\n')

        fd.close()

