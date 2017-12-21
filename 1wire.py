#!/usr/bin/env python
#coding: utf8

# Import modules
import sys
import os


# Find 1-Wire sensor 
file = open('/sys/devices/w1_bus_master1/w1_master_slaves')
w1_slave = file.read(15)
file.close()

# Read temp of sensor
file = open('/sys/devices/w1_bus_master1/' + str(w1_slave)+ '/w1_slave')
filecontent = file.read()
file.close()

# Format temp
stringvalue = filecontent.split("\n")[1].split(" ")[9]
temp = float(stringvalue[2:]) / 1000

print(str('%3.1f' % temp)+" °C")


exit()
