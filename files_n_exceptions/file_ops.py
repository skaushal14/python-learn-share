import os

def read_fl():
    fo = open('file.txt')
    print(fo.readline(),)

    fo.seek(0)

    for eline in fo:
        print(eline,)

    fo.close()


def process_fl():
    fo = open('file.txt')

    for eline in fo:
        # this split has issue when splits line to more than 2 pieces
        #(person,saidln) = eline.split(':')
        (person,saidln) = eline.split(':',1)
        print(person,)
        print(' said: ',)
        print(saidln)

    fo.close()

def process_fl2():
    fo = open('file.txt')

    for eline in fo:
        if eline.find(':') > 0:
            #print('find=%s %d' % (eline, eline.find(':')))
            (person,saidln) = eline.split(':',1)
            print(person,)
            print(' said: ',)
            print(saidln)

    fo.close()

def process_fl_try():
    if os.path.exists('file.txt'):
        fo = open('file.txt')

        for eline in fo:
            try:
                (person,saidln) = eline.split(':',1)
                print(person,)
                print(' said: ',)
                print(saidln)
            except:
                pass
                #print('pass')

        fo.close()
    else:
        print('Error: file.txt does not exists!!')

''' Be specific in exception handling. You might supress pontential bugs.'''
def process_fl_try2():
    try:
        fo = open('file.txt')

        for eline in fo:
            try:
                (person,saidln) = eline.split(':',1)
                print(person,)
                print(' said: ', end='')
                print(saidln)
            except ValueError:
                pass
                #print('pass')

        fo.close()
    except IOError:
        print('Error: file.txt does not exists!!')

#read_fl()
#process_fl()
#process_fl2()
#process_fl_try()
process_fl_try2()
