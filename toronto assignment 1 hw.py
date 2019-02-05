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

#Test Function

import numpy as np

def testfunction(firstCorner=(0,0), secondCorner=(0,0)): 
    frameparameter = 2
    checks = min(len(firstCorner), len(secondCorner))
    listfirst = list(firstCorner)
    listsecond = list(secondCorner)
    for a in range(checks):
        if firstCorner[a] < secondCorner[a]: 
            leftcorner = listfirst
            rightcorner = listsecond
        else: 
            leftcorner = listsecond
            rightcorner = listfirst
        leftcorner[a] = leftcorner[a] - frameparameter
        rightcorner[a] = rightcorner[a] + frameparameter
    checkfirst = tuple(leftcorner)
    checksecond = tuple(rightcorner)
    checkdimensions = []
	coordinates = []
	for z in range(checks):
		coordinates[z] = np.arange(checkfirst[z],checksecond[z]+1,1)
	def matrix(n): 
		while n >= 0: 
			row_op = []
			for a in coordinates[n]: 
				matrix(n-1)
			row_op.append(a)
		return row_op
	points = matrix(checks)
	return points
	for p in points:
		
	
	
	a_int = np.arange(checkfirst[0],checksecond[0]+1,1)
    b_int = np.arange(checkfirst[1],checksecond[1]+1,1)
    matrix = []
    for i in a_int: 
        row_op = []
        for j in b_int:
            row_op.append((i,j))
        matrix.append(row_op)
    results = []
    for m in matrix:
        for a in m:
            entry = isIn(firstCorner,secondCorner,a)
            results.append([a,entry])
    return results

#testfunction((1,1),(5,5))
testfunction((5,5),(3,3))



'''
Question 4: Same as Question 3 but iterating through a list of points and returning false if: 
working with an empty set of points or atleast one point doesn't fit in
'''

def allIn(firstCorner=(0,0), secondCorner=(0,0), pointList=[]):
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



