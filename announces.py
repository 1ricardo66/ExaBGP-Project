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

import os
import sys
import time
routes = open ('ips.txt','r')

for route in routes:
    sys.stdout.write(route)
    sys.stdout.flush()
    time.sleep(0.60)


try:
    now = time.time()
    while os.getppid() != 1 and time.time() < now + 5:
        line = sys.stdin.readline().strip()
        print (line)
        if not line or 'shutdown' in line:
            break
        time.sleep(1)
except IOError:
    pass
