
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  TicTacToe.py
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
#  issues: 1.  doesnt work if the if else is switched
#  remaining: 1. whos the winner. sum of rows and cols
#  

def print1():
	for i in range(3):
		for j in range(3):
			if s[i][j]==0:
				print("["+ str(i) + str(j) + "]",end=' ' )
			else:
				print(s[i][j],end=' ')
		print()
		
	
def getinp(i):
	print("enter your symbol player and location. For eg: x 1 2")
	z=input("enter \n").split(" ")
	print(int(z[1]),int(z[2]))
	if s[int(z[1])][int(z[2])]=="o" or s[int(z[1])][int(z[2])]=="x":
		print(" Choose another position please")
		getinp(i)
		
	else:
		s[int(z[1])][int(z[2])]=z[0]
		i+=1
		
	print1()
	return i
	
	
	
s=[[0,0,0],[0,0,0],[0,0,0]]
print1()
#print("[0,0] [0,1] [0,2]")
#print("[1,0] [1,1] [1,2]")
#print("[2,0] [2,1] [2,2]")
print("Player 1 is x, player 2 is o")
i=0
while(i<9):
      print("-------------------------")
      if i%2==0:
          print("player 1")
          i=getinp(i)
      else:
          print("player 2")
          i=getinp(i)
    

print1()

	
