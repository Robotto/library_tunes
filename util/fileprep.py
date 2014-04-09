#!/usr/bin/env python

import sys
import time
from time import strftime, strptime, mktime, struct_time, time, ctime, localtime
from random import random


if len(sys.argv) == 2:
    print "No parameters supplied.. "
    print "Usage: %s <input filename> <output filename>" %sys.argv[0]
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

AYearInSeconds = 31536000


def parseLine(line):
  transaction = line.split('\t')[0]
  library = line.split('\t')[2]

  timestring = line.split('\t')[1]
  time_struct=strptime(timestring,'%Y%m%dT%H%M%S')
  epoch = mktime(time_struct)

  epoch = epoch+AYearInSeconds #offset data one year, so it can be synced to the current NTP time.

  epoch+=random() #add random amount of 1/1000s of 1 second, to spread out the soundscape

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

    print "parsed: %s entries"%len(transactions)
    print "first: %s"%transactions[0][0]
    print "last: %s"%transactions[len(transactions)-1][0]

    print "Sorting entries after adding random time.."
    sortstart = time()
    sorted_by_fractions=sorted(transactions, key=lambda transaction: transactions[0])   # sort by timestamp
    sorttime= time()-sortstart
    print "sorted in %s seconds" %sorttime
    #print sorted_transactions

    print "entry 1:"
    print lines[0]


    writestart = time()
    print "writing new file: %s"%output_file
    with open(output_file, 'w') as f:
         for line in sorted_by_fractions:
         	f.write(str(line[0])+' '+str(line[1])+' '+str(line[2])+'\n')
    writetime = time()-writestart
    print "Writetime: %s"%writetime

    print
    print "Done."

except Exception as e:
    print "error... " + str(e)



