#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Timer.py
#  
#  Copyright 2016 Ketakee Nimavat <Ketakee Nimavat@KETAKEE>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from threading import Timer
import time

import winsound

def timeout():
    print("Break time!")
    winsound.Beep(500,1000)
#t1=5.0
#flag=True 
#i=0

flag=True
while(flag):
	print("starting 1500 sec")
	winsound.Beep(500,1000)
	t = Timer(25* 60, timeout)
	t.start()
	#i=0
	#while(i<2):
		#print(i+1)
		#winsound.Beep(750,2000)
		#time.sleep(750)
		#i+=1
	print("break")
	time.sleep(300)
	winsound.Beep(300,2000)
	print("break over")
	time.sleep(10)
