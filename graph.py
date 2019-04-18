"""
Homework 3 
CIS4930
Summer 17
Ryan Winter
rw15e
"""
from __future__ import print_function
vertexList = []
edgeList = []

class Graph:
    #def __init__(self):
	#vertexList = []

    def add_vertex(self, name):
        # create/add vertex identified by "name"
	# if vertex already exists, print error message
	if name in vertexList:
	    print("A vertex with name", name, "already exists.")
	else:
	    vertexList.append(name)

    def add_edge(self, start, end):
	if end not in vertexList:
	    vertexList.append(end) 
	if start not in vertexList:
	    vertexList.append(start)
	if start in vertexList:
	    if end in vertexList:
		edgeList.append(start)
		edgeList.append(end)
	
	  #  else:
	#	vertexList.append(end)
	#else:
	 #   vertexList.append(start)

    def remove_vertex(self, name):
	if name in vertexList:
	    vertexList.remove(name)
	pass

    def remove_edge(self, start, end):
	#indexVal = 0
	edgeList.remove(start)
	edgeList.remove(end)
	#for i in range(len(edgeList)/2):
	#    if start == edgeList[indexVal]:
	#	if end == edgeList[indexVal+1]:
	#	    #print("DELETING EDGE")
	#	    del edgeList[indexVal], edgeList[indexVal+1]
	    #print (edgeList[indexVal], "->", end = " ")
	#    indexVal = indexVal + 1
	    

    def vertices(self):
	return vertexList

    def print_edges(self):
	#print(*edgeList, sep = '\n')
	indexVal = -1
	for i in range(len(edgeList)/2):
	    print (edgeList[indexVal], "->", end = " ")
	    indexVal = indexVal + 2
	    print (edgeList[indexVal])

    def is_connected(self, start, end):
	#if start and end in edgeList:
	for i in range(len(edgeList)):
	    if edgeList[i] == start:
		if edgeList[i+1] == end:
		    return True
	return False

    def print_paths(self, start, end):
	for j in range(len(vertexList)):
	    if vertexList[j] == start:
		try:
		    if vertexList[j+1] == end:
		        print(vertexList[j], "->", vertexList[j+1])
		    if vertexList[j+2] == end:
		        print(vertexList[j], "->", vertexList[j+1], "->", vertexList[j+2])
		    if vertexList[j+3] == end:
		        print(vertexList[j], "->", vertexList[j+1], "->", vertexList[j+2], "->", vertexList[j+3])
		    if vertexList[j+4] == end:
		        print(vertexList[j], "->", vertexList[j+1], "->", vertexList[j+2], "->", vertexList[j+3], "->", vertexList[j+4])
		    if vertexList[j+5] == end:
		        print(vertexList[j], "->", vertexList[j+1], "->", vertexList[j+2], "->", vertexList[j+3], "->", vertexList[j+4], "->", vertexList[j+5])
		except IndexError:
		    pass
	pass

class UndirectedGraph(Graph):
    def __init__(self):
	vertexList[:] = []	# clear list
        edgeList[:] = []	# clear list

    def add_edge(self, start, end):
	if end not in vertexList:
	    vertexList.append(end) 
	if start not in vertexList:
	    vertexList.append(start)
	if start in vertexList:
	    if end in vertexList:
		edgeList.append(start)
		edgeList.append(end)
    pass

    def remove_edge(self, start, end):
	edgeList.remove(start)
	edgeList.remove(end)

    def print_edges(self):
	#print(*edgeList, sep = '\n')
	indexVal = -1
	for i in range(len(edgeList)/2):
	    print (edgeList[indexVal], "<->", end = " ")
	    indexVal = indexVal + 2
	    print (edgeList[indexVal])

    def print_paths(self, start, end):
	for j in range(len(vertexList)):
	    if vertexList[j] == start:
		try:
		    if vertexList[j+1] == end:
		        print(vertexList[j], "<->", vertexList[j+1])
		    if vertexList[j+2] == end:
		        print(vertexList[j], "<->", vertexList[j+1], "<->", vertexList[j+2])
		    if vertexList[j+3] == end:
		        print(vertexList[j], "<->", vertexList[j+1], "<->", vertexList[j+2], "<->", vertexList[j+3])
		    if vertexList[j+4] == end:
		        print(vertexList[j], "<->", vertexList[j+1], "<->", vertexList[j+2], "<->", vertexList[j+3], "<->", vertexList[j+4])
		    if vertexList[j+5] == end:
		        print(vertexList[j], "<->", vertexList[j+1], "<->", vertexList[j+2], "<->", vertexList[j+3], "<->", vertexList[j+4], "<->", vertexList[j+5])
		except IndexError:
		    pass
	pass

