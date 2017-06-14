
movies=["meaning of life",
        "life of brain",
        "holy grail"]

cast = ["Cleese", 'Palin', 'Jones', "Idle"]

print 'hello world!'

print movies[1]

print cast
print 'cast'
print len(cast)

print "cast.append(gilliam)"
cast.append('gilliam')
print cast

print "cast.pop()"
cast.pop()
print cast

print "cast.extend([gilliam,chapman])"
cast.extend(["gilliam","chapman"])
print cast

print "cast.remove(Jones)"
cast.remove("Jones")
print cast

print "cast.insert(0,Jones)"
cast.insert(0,"Jones")
print cast

print "movies.insert(1,1975)"
movies.insert(1,1975)
movies.insert(3,1979)
movies.insert(5,1983)
print movies

movies2=["meaning of life",1975,
        "life of brain",1979,
        "holy grail",1983]
print movies2

print "for loop"
for data in movies2:
    print data

print "while loop"
cnt = 0
while cnt < len(movies2):
    print movies2[cnt]
    cnt = cnt+1
