#!/usr/bin/env python
#coding: utf8

import os
import sys


base_dir = '/sys/devices/w1_bus_master1/'

# Find 1-Wire sensor 
dir = open(base_dir+'w1_master_slaves')
device_folder = dir.readline(15)
dir.close()

# Read temp of sensor
file = open(base_dir + device_folder + '/w1_slave')
filecontent = file.read()
file.close()

# Format temp
stringvalue = filecontent.split("\n")[1].split(" ")[9]
temp = float(stringvalue[2:]) / 1000

print(str('%3.1f' % temp)+" °C")

exit()
