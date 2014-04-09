#!/usr/bin/env python

import sys
from time import strftime, strptime, mktime, struct_time, time, ctime, localtime
import ntplib
from random import random
import operator


if len(sys.argv) == 1:
    print "No parameters supplied.. "
    print "Usage: %s <filename>" %sys.argv[0]
    sys.exit(1)

input_file = sys.argv[1]

AYearInSeconds = 31536000


def parseLine(line):
  #transaction = line.split('\t')[0]
  library = line.split('\t')[2]

  #timestring = line.split('\t')[1]
  #time_struct=strptime(timestring,'%Y%m%dT%H%M%S')
  #epoch = mktime(time_struct)

  #epoch = epoch+AYearInSeconds #offset data one year, so it can be synced to the current NTP time.

  #epoch+=random() #add random amount of 1/100s of 1 second, to spread out the soundscape

  #print "TimeCode: %s" %epoch
  #print "Library: %s" %library
  #print "Transaction: %s" %transaction
  return (library)

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
        libraries = [parseLine(dataset) for dataset in lines]
    except Exception as e:
        print "can't parse lines because:" +str(e)
    parsetime= time()-parsestart
    print "Parsetime: %s seconds" %parsetime



 										#(1398163052.4438782, 'ris', 'u')


    aaby = libraries.count('aby')
    beder = libraries.count('bed')
    egaa = libraries.count('ega')
    gellerup = libraries.count('gel')
    hasselager = libraries.count('hag')
    hasle = libraries.count('hal')
    harlev = libraries.count('har')
    hb = libraries.count('hb' )
    hjortshoj = libraries.count('hjo')
    hojbjerg = libraries.count('hoj')
    lystrup = libraries.count('lys')
    risskov = libraries.count('ris')
    sabro = libraries.count('sab')
    skodstrup = libraries.count('sko')
    solbjerg = libraries.count('sol')
    tranbjerg = libraries.count('tra')
    trige = libraries.count('tri')
    tilst = libraries.count('tst')
    vib = libraries.count('vib')

    counts ={
    'Aaby': aaby,
    'beder' : beder,
    'egaa' : egaa,
    'gellerup':gellerup,
    'hasselager':hasselager,
    'hasle':hasle,
    'harlev':harlev,
    'hb':hb,
    'hjortshoj':hjortshoj,
    'hojbjerg':hojbjerg,
    'lystrup':lystrup,
    'risskov':risskov,
    'sabro':sabro,
    'skodstrup':skodstrup,
    'solbjerg':solbjerg,
    'tranbjerg':tranbjerg,
    'trige':trige,
    'tilst':tilst,
    'vib':vib
    }


    #sorted_counts=sorted(counts, key=lambda counts: counts)   # sort by library
    sorted_counts=sorted(counts.iteritems(), reverse=True, key=operator.itemgetter(1))



    print sorted_counts



except Exception as e:
    print "error... " + str(e)


