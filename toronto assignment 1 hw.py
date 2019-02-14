######################Assignment 1 - Intro to Python################################################


'''Question 1: Count number of times letters appear in DNA sequence
'''

def distrubution(s):
	letters = []
	for i in s: 
		if i.isalpha() == True and i not in letters:
			count = 0
			for a in s: 
				if a == i: 
					count += 1
			print('Number of ' + i + '\'s: ' + str(count))
			letters.append(i)
			
distrubution('ATGCTTCAGAAAGGTCTTACG.')
			
''' Question 2: Output all Capitals that contain their State Names in dictionary
'''

capitals = {

	'Alabama'        :'Montgomery',
	'Alaska'         :'Juneau',
	'Arizona'        :'Phoenix',
	'Arkansas'       :'Little Rock',
	'California'     :'Sacramento',
	'Colorado'       :'Denver',
	'Connecticut'    :'Hartford',
	'Delaware'       :'Dover',
	'Florida'        :'Tallahassee',
	'Georgia'        :'Atlanta',
	'Hawaii'         :'Honolulu',
	'Idaho'          :'Boise',
	'Illinois'       :'Springfield',
	'Indiana'        :'Indianapolis',
	'Iowa'           :'Des Moines',
	'Kansas'         :'Topeka',
	'Kentucky'       :'Frankfort',
	'Louisiana'      :'Baton Rouge',
	'Maine'          :'Augusta',
	'Maryland'       :'Annapolis',
	'Massachusetts'  :'Boston',
	'Michigan'       :'Lansing',
	'Minnesota'      :'St. Paul',
	'Mississippi'    :'Jackson',
	'Missouri'       :'Jefferson City',
	'Montana'        :'Helena',
	'Nebraska'       :'Lincoln',
	'Nevada'         :'Carson City',
	'New Hampshire'  :'Concord',
	'New Jersey'     :'Trenton',
	'New Mexico'     :'Santa Fe',
	'New York'       :'Albany',
	'North Carolina' :'Raleigh',
	'North Dakota'   :'Bismarck',
	'Ohio'           :'Columbus',
	'Oklahoma'       :'Oklahoma City',
	'Oregon'         :'Salem',
	'Pennsylvania'   :'Harrisburg',
	'Rhode Island'   :'Providence',
	'South Carolina' :'Columbia',
	'South Dakota'   :'Pierre',
	'Tennessee'      :'Nashville',
	'Texas'          :'Austin',
	'Utah'           :'Salt Lake City',
	'Vermont'        :'Montpelier',
	'Virginia'       :'Richmond',
	'Washington'     :'Olympia',
	'West Virginia'  :'Charleston',
	'Wisconsin'      :'Madison',
	'Wyoming'        :'Cheyenne'

		
	}

for x,y in statecapitals.items(): 
	if x.upper() in y.upper():
		print(y)
		
'''Question 3: Check if single coordinate is in rectangle defined from left diagonal to right. 
'''

def isIn(firstCorner=(0,0), secondCorner=(0,0), point=(0,0)):
    """Checks if point is inside shape produced by specified corners. Note: works in multiple dimensions"""
    indices = min([len(firstCorner), len(secondCorner), len(point)])
    NotIn = 0
    for a in range(indices):       
        if firstCorner[a] < secondCorner[a]: 
            if not (firstCorner[a] <= point[a] <= secondCorner[a]): 
                NotIn += 1
                break
        else: 
            if not (secondCorner[a] <= point[a] <= firstCorner[a]):
                NotIn += 1
                break           
    if NotIn > 0: 
        return False
    else: 
        return True

# print(isIn((1,2), (3,4), (1.5, 3.2))) #True
# print(isIn((4,3.5), (2,1), (3, 2))) #True
# print(isIn((-1,0), (5,5), (6,0))) #False
# print(isIn((4,1), (2,4), (2.5,4.5))) #False
# print(isIn((-4,-1), (2,4), (2.5,4.5))) #False
# print(isIn((1,1,1),(3,3,3),(2,2,2)))#True
# print(isIn((1,1,1),(3,1,3),(2,2,2)))#False
# print(isIn((5,5,5,5),(0,-1,0,1),(2,2,2,2)))#True
# print(isIn((5,5,5,5),(0,-1,0,1),(2,2,2,0)))#False


'''
Question 4: Same as Question 3 but iterating through a list of points and returning false if: 
working with an empty set of points or atleast one point doesn't fit in
'''

def allIn(firstCorner=(0,0), secondCorner=(0,0), pointList=[]):
    """Checks if all points in a set are inside a shape produced by specified corners. 
    Note: works in multiple dimensions"""
    NotIn = 0
    if pointList == []: 
        return False
    else:
        for point in pointList:
                indices = min([len(firstCorner), len(secondCorner), len(point)])
                for a in range(indices):       
                    if firstCorner[a] < secondCorner[a]: 
                        if not (firstCorner[a] <= point[a] <= secondCorner[a]): 
                            NotIn += 1
                            break
                    else: 
                        if not (secondCorner[a] <= point[a] <= firstCorner[a]):
                            NotIn += 1
                            break           
    if NotIn > 0: 
        return False
    else: 
        return True

# print(allIn((0,0), (5,5), [(1,1), (0,0), (5,5)])) #True
# print(allIn((0,0), (5,5), [(1,1), (0,0), (5,6)])) #False            
# print(allIn((0,0), (5,5), [])) #False     
# print(allIn((0,0), (-5,-5), [(-1,-1), (0,0), (3,-3)])) #False
# print(allIn((0,0), (-5,-5), [(-1,-1), (0,0), (-3,-3)])) #True

#Test Functions for Questions 3 and 4

%matplotlib inline

import numpy as np
import itertools as it
import matplotlib.pyplot as plt

def framemaker(pointa = (0,0), pointb = (0,0), frame = 0): 
    """Lists all tuples inside a fixed size frame around a box 
	created by two points."""
	dimension = min(len(pointa), len(pointb))
    lista, listb = list(pointa), list(pointb)
    leftlist, rightlist = [0]*dimension, [0]*dimension
    inputs = []
    for a in range(dimension):
        leftlist[a] = min(lista[a],listb[a]) - abs(frame)
        rightlist[a] = max(lista[a],listb[a]) + abs(frame)
        inputs.append(np.arange(leftlist[a], rightlist[a]+1,1))
    return list(it.product(*inputs))


def testfunction(firstCorner=(0,0), secondCorner=(0,0),boxframe=0): 
    """Individually checks all points within a a certain range of a box
	for function made by Question 3 and illustates with a visual. """
    matrix = framemaker(firstCorner, secondCorner, boxframe)
    visual = []
    for m in matrix:
        entry = isIn(firstCorner,secondCorner,m)
        visual.append([m,entry])  
#     return visual
## Returning here shows raw data. 
## Plot going forward only works in 2 dimensions.
    visualarray = np.array(visual)
    for (v, c) in [(True, 'b'), (False, 'r')]:
        if visualarray[visualarray[:,1] == v].any():
            plt.scatter(*zip(*visualarray[visualarray[:,1] == v,0]),c = c)
    return plt.show()


def testallfunction(firstCorner=(0,0), secondCorner=(0,0),boxframe=0, pointframe = 0): 
    """Individually checks all point sets within a a certain range of a box
	for function made by Question 4 and illustates with a visual. Point sets 
	made by generating all tuples within a certain distance of a point (similar to 
	the box."""
	matrix = framemaker(firstCorner, secondCorner, boxframe)
    visual = []
    for center in matrix:
        pointset = framemaker(center, center, pointframe)
        entry = allIn(firstCorner,secondCorner,pointset)
        visual.append([center,pointset,entry])  
#     return visual
# Returning here shows raw data. 
# Plot generating colored scatter plot only works in 2 dimensions.
    visualarray = np.array(visual)
    for (v, c) in [(True, 'b'), (False, 'r')]:
        if visualarray[visualarray[:,2] == v].any():
            plt.scatter(*zip(*visualarray[visualarray[:,2] == v,0]),c = c)
    return plt.show()



# framemaker((1,1),(5,5),2)
testallfunction((1,1),(5,5),3,1)

# testfunction((5,5),(3,3),2)
# testfunction((-1,-1),(10,10),1)
# testfunction((-1,10),(10,-1),2)

testfunction((10,3),(-1,7),2)
	
# testallfunction((0,0,0),(10,10,10),3,1)
# testallfunction((0,0),(10,10),3,1)
# framemaker((1,1),(5,5),2)
# testallfunction((1,1),(5,5),3,1)
