from random import randint as rand
i=0
y=0
community = ["264386:111","264386:222","264386:333"]

for i in range (255):
    for y in range (255):
        print("announce route 127.{}.40.{}/32 next-hop self extended-community {};".format(i,y,community[rand(0,2)]))
        print("announce route 127.{}.70.{}/32 next-hop self extended-community {};".format(i,y,community[rand(0,2)]))
        print("announce route 10.{}.45.{}/32 next-hop self extended-community {};".format(i,y,community[rand(0,2)]))
        print("announce route 10.22.{}.{}/32 next-hop self extended-community {};".format(i,y,community[rand(0,2)]))
        print("announce route 10.120.{}.{}/32 next-hop self extended-community {};".format(i,y,community[rand(0,2)]))
    i+=1
    y+=1
