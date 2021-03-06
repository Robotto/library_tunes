#!/usr/bin/env python

import sys
import time
from time import strftime, strptime, mktime, struct_time, time, ctime, localtime
import ntplib
import pygame
from random import random

if len(sys.argv) == 1:
    print "No parameters supplied.. "
    print "Usage: %s <filename>" %sys.argv[0]
    sys.exit(1)

input_file = sys.argv[1]

pygame.mixer.init()

#time_offset=-774448

#load sounds:
print "loading sounds.."

aaby_u = pygame.mixer.Sound('sounds/aby_u.wav')
aaby_a = pygame.mixer.Sound('sounds/aby_a.wav')
aaby = {'u':aaby_u,'a':aaby_a} #dictionary

beder_u = pygame.mixer.Sound('sounds/bed_u.wav')
beder_a = pygame.mixer.Sound('sounds/bed_a.wav')
beder = {'u':beder_u,'a':beder_a} #dictionary

egaa_u = pygame.mixer.Sound('sounds/ega_u.wav')
egaa_a = pygame.mixer.Sound('sounds/ega_a.wav')
egaa = {'u':egaa_u,'a':egaa_a} #dictionary

gellerup_u = pygame.mixer.Sound('sounds/gel_u.wav')
gellerup_a = pygame.mixer.Sound('sounds/gel_a.wav')
gellerup = {'u':gellerup_u,'a':gellerup_a} #dictionary

hasselager_u = pygame.mixer.Sound('sounds/har_u.wav')
hasselager_a = pygame.mixer.Sound('sounds/har_a.wav')
hasselager = {'u':hasselager_u,'a':hasselager_a} #dictionary

hasle_u = pygame.mixer.Sound('sounds/has_u.wav')
hasle_a = pygame.mixer.Sound('sounds/has_a.wav')
hasle = {'u':hasle_u,'a':hasle_a} #dictionary

harlev_u = pygame.mixer.Sound('sounds/har_u.wav')
harlev_a = pygame.mixer.Sound('sounds/har_a.wav')
harlev = {'u':harlev_u,'a':harlev_a} #dictionary

hb_u = pygame.mixer.Sound('sounds/hb_u.wav')
hb_a = pygame.mixer.Sound('sounds/hb_a.wav')
hb = {'u':hb_u,'a':hb_a} #dictionary

hjortshoj_u = pygame.mixer.Sound('sounds/hjo_u.wav')
hjortshoj_a = pygame.mixer.Sound('sounds/hjo_a.wav')
hjortshoj = {'u':hjortshoj_u,'a':hjortshoj_a} #dictionary

hojbjerg_u = pygame.mixer.Sound('sounds/hoj_u.wav')
hojbjerg_a = pygame.mixer.Sound('sounds/hoj_a.wav')
hojbjerg = {'u':hojbjerg_u,'a':hojbjerg_a} #dictionary

lystrup_u = pygame.mixer.Sound('sounds/lys_u.wav')
lystrup_a = pygame.mixer.Sound('sounds/lys_a.wav')
lystrup = {'u':lystrup_u,'a':lystrup_a} #dictionary

risskov_u = pygame.mixer.Sound('sounds/ris_u.wav')
risskov_a = pygame.mixer.Sound('sounds/ris_a.wav')
risskov = {'u':risskov_u,'a':risskov_a} #dictionary

sabro_u = pygame.mixer.Sound('sounds/sab_u.wav')
sabro_a = pygame.mixer.Sound('sounds/sab_a.wav')
sabro = {'u':sabro_u,'a':sabro_a} #dictionary

skodstrup_u = pygame.mixer.Sound('sounds/sko_u.wav')
skodstrup_a = pygame.mixer.Sound('sounds/sko_a.wav')
skodstrup = {'u':skodstrup_u,'a':skodstrup_a} #dictionary

solbjerg_u = pygame.mixer.Sound('sounds/sol_u.wav')
solbjerg_a = pygame.mixer.Sound('sounds/sol_a.wav')
solbjerg = {'u':solbjerg_u,'a':solbjerg_a} #dictionary

tranbjerg_u = pygame.mixer.Sound('sounds/tra_u.wav')
tranbjerg_a = pygame.mixer.Sound('sounds/tra_a.wav')
tranbjerg = {'u':tranbjerg_u,'a':tranbjerg_a} #dictionary

trige_u = pygame.mixer.Sound('sounds/tri_u.wav')
trige_a = pygame.mixer.Sound('sounds/tri_a.wav')
trige = {'u':trige_u,'a':trige_a} #dictionary

tilst_u = pygame.mixer.Sound('sounds/til_u.wav')
tilst_a = pygame.mixer.Sound('sounds/til_a.wav')
tilst = {'u':tilst_u,'a':tilst_a} #dictionary

viby_u = pygame.mixer.Sound('sounds/vib_u.wav')
viby_a = pygame.mixer.Sound('sounds/vib_a.wav')
viby = {'u':viby_u,'a':viby_a} #dictionary

#x_a_1 = pygame.mixer.Sound('sounds/x_a_1.wav')
#x_a_2 = pygame.mixer.Sound('sounds/x_a_2.wav')
#x_a_3 = pygame.mixer.Sound('sounds/x_a_3.wav')
print "Done."

dictionaries={
'aby': aaby,
'bed' : beder,
'ega' : egaa,
'gel': gellerup,
'hag': hasselager,
'hal': hasle,
'har': harlev,
'hb': hb,
'hjo': hjortshoj,
'hoj': hojbjerg,
'lys': lystrup,
'ris': risskov,
'sab': sabro,
'sko': skodstrup,
'sol': solbjerg,
'tra': tranbjerg,
'tri': trige,
'tst': tilst,
'vib': viby }

#print "dictionaries:"
#print
#print dictionaries


AYearInSeconds = 31536000

def transaction_to_sound(line):
  timestring = line.split(' ')[0]
  library = line.split(' ')[1]
  transaction = line.split(' ')[2]

  sound = dictionaries[library][transaction]

  epoch = float(timestring)

  #epoch = epoch+AYearInSeconds #offset data one year, so it can be synced to the current NTP time.

  #epoch+=random() #add random amount of 1/1000s of 1 second, to spread out the soundscape

  if transaction=='u':
  	trstring='Udlaan fra %s'%library
  else: trstring='Aflevering til %s'%library
  #print "TimeCode: %s" %epoch
  #print "Library: %s" %library
  #print "Transaction: %s" %transaction
  return (epoch,sound,library,trstring)



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
        #transactions = [parseLine(dataset) for dataset in lines]
        sounds = [transaction_to_sound(dataset) for dataset in lines]
    except Exception as e:
        print "can't parse lines because:" +str(e)
    parsetime= time()-parsestart
    print "Parsetime: %s seconds" %parsetime

    print "parsed: %s entries"%len(sounds)
    print "first: %s"%sounds[0][0]
    print "last: %s"%sounds[len(sounds)-1][0]


    print "Sorting entries after adding random time.."
    sortstart = time()
    sorted_by_fractions=sorted(sounds, key=lambda transaction: sounds[0])   # sort by timestamp
    sorttime= time()-sortstart
    print "sorted in %s seconds" %sorttime
    #print sorted_transactions

    try:
        ntpClock = ntplib.NTPClient()

        ntpResponse = ntpClock.request('dk.pool.ntp.org', version=3)
        ntpTime = ntpResponse.tx_time
        print "ntp time: %s"%ntpTime
        print "hwclock time %s"%time()
        print "ntp-hw: %s"%(ntpTime-time())
    except:
    	print "NTP unresponsive!!!"
    	ntpTime=time()

    ntpLastSync = int(time()) #localtime is only used relatively

    timeto = sorted_by_fractions[195][0]-ntpTime

    print "Entry #195 occurs %s seconds in the future"%timeto

    if len(sys.argv) == 2:
      if raw_input("Would you like to offset it to now?")=='y':
        offset=-timeto
    else: offset=86400
    #offset=86400 #offset 1 day to match day of week. 2013 -> 2014

    timestore = time()
    echotime  = timestore
    index=0

    while (sorted_by_fractions[index][0]+offset)<ntpTime: #forward the index pointer to a current time
   	        index+=1

    print "index=%s"%index

    time_to_next_echo = (sorted_by_fractions[index][0]+offset)-time()
    print "Time to next echo: %s"%time_to_next_echo
    echotime=timestore


    while 1:
        if int(time())>ntpLastSync+1800: #30 minutes
            try:
                ntpResponse = ntpClock.request('dk.pool.ntp.org', version=3)
                ntpTime = ntpResponse.tx_time
                ntpLastSync = int(time())
                print "NTP update: %s"%ntpTime
            except: print "NTP unresponsive!!!"

    #timekeeper - delay until next 1/100 second

    	while time()<timestore+0.1:
        	pass


    	ntpTime+=time()-timestore



    	if index==len(sorted_by_fractions):
    		print "End of data. Done."
    		sys.exit(0)


		#(1398163052.4438782, 'ris', 'u')
		#(1398163052.4438782, <Sound object at 0x7f08b62a2850>,'aby', 'Udlaan fra')

    	if sorted_by_fractions[index][0]+offset<=ntpTime:

    		timestring=strftime('%Y-%m-%d %H:%M:%S', localtime(sorted_by_fractions[index][0]))
    		print "%s: %s"%(timestring,sorted_by_fractions[index][3])

    		sorted_by_fractions[index][1].play()


    		index+=1

        #print ntpTime

        if echotime+5<timestore:
        	if (sorted_by_fractions[index][0]+offset-5)>time():
        		time_to_next_echo = sorted_by_fractions[index][0]+offset-time()
        		print "Time to next echo: %s"%time_to_next_echo
        		echotime=timestore







    	timestore=time()








except Exception as e:
    print "error... " + str(e)



