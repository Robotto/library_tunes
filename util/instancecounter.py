#!/usr/bin/env python

import sys
from time import strftime, strptime, mktime, struct_time, time, ctime, localtime
import ntplib
from random import random


if len(sys.argv) == 1:
	print "No parameters supplied.. "
	print "Usage: %s <filename>" %sys.argv[0]
	sys.exit(1)

input_file = sys.argv[1]

AYearInSeconds = 31536000


def parseLine(line):
  transaction = line.split('\t')[0]
  library = line.split('\t')[2]

  timestring = line.split('\t')[1]
  time_struct=strptime(timestring,'%Y%m%dT%H%M%S')
  epoch = mktime(time_struct)

  epoch = epoch+AYearInSeconds #offset data one year, so it can be synced to the current NTP time.

  #epoch+=random() #add random amount of 1/100s of 1 second, to spread out the soundscape

  #print "TimeCode: %s" %epoch
  #print "Library: %s" %library
  #print "Transaction: %s" %transaction
  return (epoch,library,transaction)

try:

    print
    print "Opening data file: %s" %input_file
    loadtstart = time()
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f]
    loadtime = time()-loadtstart
    print "file loaded.."
    print "Loadtime: %s seconds" %loadtime

    print "parsing.."
    parsestart = time()
    try:
    	transactions = [parseLine(dataset) for dataset in lines]
    except Exception as e:
    	print "can't parse lines because:" +str(e)
    parsetime= time()-parsestart
    print "Parsetime: %s seconds" %parsetime


    simul=1
    maxsimul=0
    index=0
    max_entry=0


    while index<len(transactions)-1:
		if transactions[index+1][0]==transactions[index][0]:
			simul+=1
		else:
			if simul>=maxsimul:
				print "new maximum: %s"%simul
				print "ending at line #: %s"%(index+1)
				max_entry=(index+1)
				maxsimul=simul
			simul=1
		index+=1




    print
    print "maximum simultaneous entries: %s"%maxsimul
    print "Ending at line #%s"%max_entry
    print "parsed: %s entries"%len(transactions)
    print "first: %s"%transactions[0][0]
    print "last: %s"%transactions[len(transactions)-1][0]






except Exception as e:
    print "error... " + str(e)


