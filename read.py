
f1='read1.py'
f2='read2.py'
f3='read3.py'
file_all='text.py'

def file_worker(f1):
    with open(f1,'r',encoding = 'utf - 8' ) as file:
             count  =0
             for line in file:
                 count+=1
             print(count)
file_worker(f1)


def file_worker(f2):
    with open(f2,'r',encoding = 'utf - 8' ) as file:
             count  =0
             for line in file:
                 count+=1
             print(count)
file_worker(f2)


def file_worker(f3):
    with open(f3,'r',encoding = 'utf - 8' ) as file:
             count  =0
             for line in file:
                 count+=1
             print(count)
file_worker(f3)


f = open('file_all', 'w',encoding = 'utf - 8')
f.write('read2.py\n'
        '1\n')
f.close()
f = open('file_all', 'a+',encoding = 'utf - 8')
fr =open('read2.py', 'r',encoding = 'utf - 8')
f.write(fr.read())
f.seek(0)
fr.seek(0)
print(f.read())
print(fr.read())
f.close()
fr.close()
f = open('file_all', 'a',encoding = 'utf - 8')
f.write('\nread1.py\n'
        '8\n')
f.close()
f = open('file_all', 'a+',encoding = 'utf - 8')
fs =open('read1.py', 'r',encoding = 'utf - 8')
f.write(fs.read())
f.seek(0)
fs.seek(0)
print(f.read())
print(fs.read())
f.close()
fr.close()
f = open('file_all', 'a',encoding = 'utf - 8')
f.write('\nread3.py\n'
        '9\n')
f.close()
f = open('file_all', 'a+',encoding = 'utf - 8')
fm =open('read3.py', 'r',encoding = 'utf - 8')
f.write(fm.read())
f.seek(0)
fm.seek(0)
print(f.read())
print(fm.read())
f.close()
fm.close()
