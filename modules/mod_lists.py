import print_lol

movies=["meaning of life",1975,
        "life of brain",1979,
        "holy grail",1983,
        ['graham chapman',["Michael Palin", "John Cleese",
        "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
print(movies)

print('\nlists')
print_lol.print_lol(movies,1)
print('\nlists')
print_lol.print_lol(movies)
print('\nlists')
print_lol.print_lol(movies,2)
print('\nlists')
print_lol.print_lol(movies,-9)

print('\nlists print_lol2')
print_lol.print_lol2(movies,True,1)
print('\nlists print_lol2')
print_lol.print_lol2(movies)
print('\nlists print_lol2')
print_lol.print_lol2(movies,True)
print('\nlists print_lol2')
print_lol.print_lol2(movies,True,-9)
