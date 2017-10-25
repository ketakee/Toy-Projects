#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  RockPaperScissor.py
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
import random


def generate_winner(a,b):
	user_dict= {a:"user1",b:"user2"}
	if a==b:
		return "It's a tie"
	elif a+b==2:
		return user_dict[2]
	else:
		return user_dict[min(a,b)]

print("Press 1 to play against the computer, 2 to play with a friend")
inpt=int(input())
print(inpt)
if inpt == 1:
    b=random.randrange(3)
    print("Computer it is!")
    print("Hello there! This is hp Pavillion - my model name's too long and you don't really care- i7")
    print("Let the games begin!")
    print("You go first Lord user1. Pick a number. \n 0: Rock\n 1: scissor \n 2 :A pair of Scissors")
    ans = int(input())
    print("Ahh nice choice! Lets see what the computer shall choose")
    print(str(b))
    print ("And the winner is!")
    print(generate_winner(ans,b))
else:
	print("You have chosen a fellow companion I see. Let the games begin")
	print("user1, choose a side.\n 0- Rock\n 1- scissor \n 2 - A pair of Scissors")
	a = int(input())
	print("Hmm interesting choice.")
	print("Roll your dices user2. \n 0- Rock\n 1- scissor \n 2 -A pair of Scissors")
	b = int(input())
	print("and the winner is.......")
	print(generate_winner(a,b))
