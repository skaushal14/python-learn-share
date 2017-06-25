#import nester

movies=["meaning of life",1975,
        "life of brain",1979,
        "holy grail",1983,
        ['graham chapman',["Michael Palin", "John Cleese",
        "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
print(movies)

for name in movies:
    print(name)

#check a list of list
for name in movies:
    if isinstance(name,list):
        print('yes list')
        for iname in name:
            if isinstance(iname,list):
                print('yes list')
                for i2name in iname:
                    print(i2name)
    else:
        print(name)

print('\n\trecursive function\n')
def print_list(mlist):
    for name in mlist:
        if isinstance(name,list):
            print('yes list')
            print_list(name)
        else:
            print(name)

print_list(movies)

print('\nimported function\n')
#nester.print_lol(movies)
