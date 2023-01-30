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
