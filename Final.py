# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 14:05:48 2022

@author: datkh
"""


class DecisionTree:
    #initialisation constructor
    def __init__(self, input):
        self.input = input

    # Function for best split 

    def _findBestSplit(self):
        #sorting in ascending order
        sortl = sorted(self.input, key=lambda s: [s[0], s[0]])
        l1 = set()
        # initialise empty list
        l2 = []

        # appending input to the list
        #remove duplicates
        for a, b in sortl:
            #if element not in list
            if not a in l1:
                l1.add(a)
                l2.append((a, b))

        # initialise empty list
        l3 = []
        for i in range(len(l2)):
            num = (l2[i][0])
            l3.append(num)
        l3.sort()

        # initialise empty list
        midL = []
        for i in range(len(l3) - 1):
            num1 = l3[i]
            num2 = l3[i + 1]
            #calculation of mid point
            mid = num1 + (num2 - num1) / 2
            midL.append(mid)
            
        #initialising left and right
        left = {}
        right = {}
        #traversing through loop
        for i in range(0, len(midL)):
            left[str(i)] = []
            right[str(i)] = []
            for a, b in l2:
                if a <= midL[i]:
                    # appending the tuples to left
                    left[str(i)].append((a, b))
                # appending tuples to right
                else:
                    right[str(i)].append((a, b))

        # initialise lists
        right1 = {}
        right2 = {}
        left1 = {}
        left2 = {}
        
        # initialise the loop
        for n in range(0, len(midL)):
            left1[str(n)] = []
            left2[str(n)] = []
            # checking for for loop condition to 
            #categorize according to 0 and 1 in list
            for a, b in left[str(n)]:
                if b == 0:
                    left1[str(n)].append((a, b))
                else:
                    left2[str(n)].append((a, b))
        #initialising the lists for 0 and 1 
        #of right as empty
        for n in range(0, len(midL)):
            right1[str(n)] = []
            right2[str(n)] = []

            for a, b in right[str(n)]:
                #append to elements with zero
                if b == 0:
                    right1[str(n)].append((a, b))
                #append to elements with one
                else:
                    right2[str(n)].append((a, b))

      
        #list for storing gin index values
        ginL = []

        # Calculating ginLi for right sets
        for x in range(0, len(midL)):
            #according to the mid list
            #calculating according to the
            #gini index of partitions
            d = float(len(sortl))
            d1 = (len(left[str(x)]))
            d1i = ((len(left1[str(x)]) / (len(left[str(x)]))) ** 2)
            d1j = ((len(left2[str(x)]) / (len(left[str(x)]))) ** 2)
            d2i = ((len(right1[str(x)]) / (len(right[str(x)]))) ** 2)
            
            d2_1 = ((len(right2[str(x)]) / (len(right[str(x)]))) ** 2)
            d2 = (len(right[str(x)]))
            
            temp = (d1 / d) * (1 - d1i - d1j) + (d2 / d) * (1 - d2i - d2_1)
            #rounding to 4 decimal points
            temp1 = round(temp, 4)
            ginL.append(temp1)
        #final tress for left and right
        LeftTree = []
        RightTree = []

        #if unable to calculate gini index
        #return false
        if ginL == []:
            return False
        #if able to calculate
        else:
            #store the minimum gini index
            index_ginL = ginL.index(min(ginL))
            
            for a, b in sortl:
                if midL[index_ginL] >= a in l1:
                    LeftTree.append([a, b])
                else:
                    RightTree.append([a, b])
            
            return min(ginL), midL[index_ginL], LeftTree, RightTree

