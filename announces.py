#!/usr/bin/env python3


################################################################################
#                                                                              #
#  ExaBGP permit the user send routes using API, so one process will run on    #
#  core aplication, calling a process and in this case, we will use python to  #
#  announce our routes automatically, making unnecessary do it in a manual way #
#                                                                              #
#  Example:                                                                    #
#                                                                              #
#  process route-announce {                                                    #
#   run python3 /opt/exabgp/run/announces.py;                                  #
#   encoder json;                                                              #
#  }                                                                           #
#                                                                              #
#  neighbor x.x.x.x {                                                          #
#   local-address y.y.y.y;                                                     #
#   local-as yyyy;                                                             #
#   peer-as xxxx;                                                              #
#   api send {                                                                 #
#       processes [route-announce];                                            #
#   }                                                                          #
#                                                                              #
################################################################################

from sys import stdout
from time import sleep

announces = [
    'announce route 100.10.0.0/32 next-hop self',
    'announce route 200.20.0.0/32 next-hop self',
]

sleep(5)

#Iterate through announce routes, and send output to ExaBGP :D,
#The return is like: announce route 100.10.0.0/24 next-hop self
#By the way, when u use the announce command, automatically your
#packet prefix is build correctly
for announce in announces:
    stdout.write(announce + '\n')
    stdout.flush()
    #print(announce)
    sleep(1)

#Loop endlessly to allow ExaBGP to continue running, the process will be running
#so, we cand do something to update routes automatically!
while True:
    sleep(1)

#Next update should work with txt-file! 
#Next update should work with functions!
