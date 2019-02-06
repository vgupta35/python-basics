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

#Test Function
#Tests all points for IsIn function within number of frameparameter (2) spaces of shape formed by corners.

%matplotlib inline

import numpy as np
import itertools as it
import matplotlib.pyplot as plt

def testfunction(firstCorner=(0,0), secondCorner=(0,0),frameparameter=0): 
    """Checks all points within shape created by vertices +/- n spaces based on frame parameter.
    Returns a visual with blue and True and red as False. Used to validate isIn() function. """
    checks = min(len(firstCorner), len(secondCorner))
    listfirst, listsecond = list(firstCorner), list(secondCorner)
    leftcorner = [0]*checks
    rightcorner = [0]*checks
    for a in range(checks):
        leftcorner[a] = min(listfirst[a],listsecond[a]) - abs(frameparameter)
        rightcorner[a] = max(listfirst[a],listsecond[a]) + abs(frameparameter)
    checkfirst = tuple(leftcorner)
    checksecond = tuple(rightcorner)    
    coordinates = []
    for z in range(checks):
        coordinates.append(np.arange(checkfirst[z],checksecond[z]+1,1))
    matrix = list(it.product(*coordinates))
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


# testfunction((5,5),(3,3),2)
# testfunction((-1,-1),(10,10),1)
# testfunction((-1,10),(10,-1),2)

testfunction((10,3),(-1,7),2)


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

#Test Function

%matplotlib inline

import numpy as np
import itertools as it
import matplotlib.pyplot as plt

def testallfunction(firstCorner=(0,0), secondCorner=(0,0),boxframe=0, pointframe = 0): 
    """Checks whether a set of points is within shape created by vertices +/- n spaces based on box frame.
    Point set is a series of points +/- n spaces around a center point based on a point frame.
    Returns a visual with blue and True and red as False. Used to validate allIn() function. """
    checks = min(len(firstCorner), len(secondCorner))
    listfirst, listsecond = list(firstCorner), list(secondCorner)
    leftcorner = [0]*checks
    rightcorner = [0]*checks
    for a in range(checks):
        leftcorner[a] = min(listfirst[a],listsecond[a]) - abs(boxframe)
        rightcorner[a] = max(listfirst[a],listsecond[a]) + abs(boxframe)
    checkfirst = tuple(leftcorner)
    checksecond = tuple(rightcorner)    
    coordinates = []
    for z in range(checks):
        coordinates.append(np.arange(checkfirst[z],checksecond[z]+1,1))
    matrix = list(it.product(*coordinates))
    visual = []
    deviation = range(-pointframe, pointframe+1)
    for center in matrix:
        pointrange = []
        for d in range(checks):
            pointrange.append(np.arange(center[d] - abs(pointframe),center[d] + abs(pointframe)+1,1))
        pointset = list(it.product(*pointrange)) 
        entry = allIn(firstCorner,secondCorner,pointset)
        visual.append([center,pointset,entry])  
#     return visual
# Returning here shows raw data. 
# Plot going forward only works in 2 dimensions.
    visualarray = np.array(visual)
    for (v, c) in [(True, 'b'), (False, 'r')]:
        if visualarray[visualarray[:,2] == v].any():
            plt.scatter(*zip(*visualarray[visualarray[:,2] == v,0]),c = c)
    return plt.show()

# testfunction((5,5),(3,3),2)
# testfunction((-1,-1),(10,10),1)
# testfunction((-1,10),(10,-1),2)

# testallfunction((0,0,0),(10,10,10),3,1)

testallfunction((0,0),(10,10),3,1)
# testfunction((10,3),(-1,7),2)
