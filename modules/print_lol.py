
''' This is the nester.py module, and it provides one function called
print_lol() which prints lists that may or may not include nested lists.'''

''' level is optional argument '''
def print_lol(mlist,level=0):
    '''This function takes a positional argument called the_list, which is any
    Python list (of, possibly, nested lists). Each data item in the provided list
    is (recursively) printed to the screen on its own line. A second argument called
    level to provide the indentation as per the level value.'''

    for name in mlist:
        if isinstance(name,list):
            print_lol(name,level+1)
        else:
            for tab_stop in range(level):
                #for python 2.x only comma will do & in 3.x end=''
                print("\t",)
            print(name)

''' indent level are optional argument
turning indentation on/off without changing the APIs'''
def print_lol2(mlist,indent=False,level=0):
    '''This function takes a positional argument called the_list, which is any
    Python list (of, possibly, nested lists). Each data item in the provided list
    is (recursively) printed to the screen on its own line. A second argument called
    level to provide the indentation as per the level value.'''

    for name in mlist:
        if isinstance(name,list):
            print_lol2(name,indent,level+1)
        else:
            if indent:
                for tab_stop in range(level):
                #for python 2.x only comma will do & in 3.x end=''
                    print("\t",)
            print(name)
