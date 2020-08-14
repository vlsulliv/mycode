#!/usr/bin/env python3

# open file in read mode
# dnsfile = open("dnsservers.txt", "r")
with open("dnsservers.txt", "r") as dnsfile:
	# ident to keep dnsfile open
	# loop accross the lines in the file
	for svr in dnsfile:
	    #print and end without a newline
	    print(svr, end="")

# dnt worry abt closing file, done auto
# dnsfile.close()





