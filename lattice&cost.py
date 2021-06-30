# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 13:54:17 2021

@author: dingzeyu
"""

from anytree import Node, RenderTree
import re
import math


input_sentence = "hakaniiku"
start = Node("start", parent = None, cost = 0, POS = "START")   # start of the lattice tree
# end = Node("end", parent = None, cost = 0, POS = "END")
parent_node = start

final_cost = math.inf   # total cost of certain path
# final_node = None


Word_Dictionary = {
    "aka": ['N'],
    "ani":['N'],
    "ha":['N','P'],
    "haka":['N'],
    "i":['V'],
    "kani":['N'],
    "ku":['N','X'],
    "ni":['P'],
    "nii":['N']    
    }

Connection_Table = [
    [0,1,1,0,0],    # START
    [1,1,1,1,0],    # N
    [0,0,1,0,1],    # V
    [1,1,1,1,0],    # P
    [1,1,1,0,0]     # X
    ]

POS_cost_table = [40, 10, 30, 10, 0, 0]     # N V P X

POS_pair_cost_table = [
    [0, 10, 50, 0,  0   ],  # START
    [30,20, 50, 10, 0   ],  # N
    [0, 0,  60, 0,  10  ],  # V
    [20,20, 20, 40, 0   ],  # P
    [10,10, 20, 0,  0   ]   # X
    ]
  # END N   V   P   X


def lattice(input_sentence):  
    global parent_node
    global final_cost
    # global final_node
    
    for i in range(len(input_sentence)):
        for j in range(i+1, len(input_sentence)+1):
            substr = input_sentence[i:j]
            exist = 0
            for k in Word_Dictionary:
                if re.search("^"+substr,k):
                    exist = 1
                    if k == substr:
                        
                        for s in Word_Dictionary[k]:
                            temp_parent_node = parent_node
                            right = s
                            left = parent_node.POS
                           
                            
                            if lattice_check(left, right) :

                                cost_of_node = parent_node.cost + POS_cost(right) + POS_pair_cost(left,right)
                                
                                new_node = Node(substr, parent = parent_node, cost = cost_of_node, POS = s)
                                parent_node = new_node
                                sub_sentence = input_sentence[j:]

                                if sub_sentence == "" :
                                    cost_of_node = parent_node.cost +  POS_pair_cost(parent_node.POS,"END")
                                    
                                    end_node = Node("end", parent = parent_node, cost = cost_of_node, POS = "END")
                                    left = end_node.parent.POS
                                    right = end_node.POS
                              
                                    parent_node = parent_node.parent.parent
                                    
                                    if end_node.cost < final_cost:
                                        final_cost = end_node.cost
                                        # final_node = end_node

                                lattice(sub_sentence)
                                parent_node = temp_parent_node

            if exist == 0:  # if ^substr does not exist
                parent_node = parent_node.parent
                return
    
    return final_cost

def lattice_check(left, right):
    check_table = {
        "START":0,
        "END":0,
        "N":1,
        "V":2,
        "P":3,
        "X":4
        }

    for i in check_table:
        if left == i:
            left = check_table[i]
    for i in check_table:
        if right == i:
            right = check_table[i]
    # print(left,right)
    check = Connection_Table[left][right]
    return check

def POS_pair_cost(left, right):
    check_table = {
        "START":0,
        "END":0,
        "N":1,
        "V":2,
        "P":3,
        "X":4
        }
    for i in check_table:
        if left == i:
            left = check_table[i]
    for i in check_table:
        if right == i:
            right = check_table[i]
    cost = POS_pair_cost_table[left][right]
    return cost

def POS_cost(POS):
    check_table = {
        "START":4,
        "END":5,
        "N":0,
        "V":2,
        "P":1,
        "X":3
        }
    for i in check_table:
        if POS == i:
            POS = check_table[i]

    cost = POS_cost_table[POS]
    return cost

lattice(input_sentence)
for pre, fill, node in RenderTree((start)):
    print("%s%s (%d)" % (pre, node.name, node.cost))
    
print("The minimum cost is",final_cost)