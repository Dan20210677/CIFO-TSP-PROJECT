import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

def openFile (fileName):
    infile = open(fileName, 'r')
    header = True
    node = True #matrix or node?
    temp = []
    info = {}
    while header:
        for line in infile.readline().strip().split(':'):
            temp.append(line)
            if 'NODE_COORD_SECTION' in line:
                header = False

            elif 'EDGE_WEIGHT_SECTION' in line:
                header = False
                node = False

    for i in range(0, len(temp)-1, 2):
        info[temp[i]] = temp[i+1]

    # Read node list
    if node:
        nodelist = []
        N = int(info['DIMENSION'])
        for i in range(0, N):
            x, y = infile.readline().strip().split()[1:]
            nodelist.append([float(x), float(y)])
    else:
        nodelist = []
        N = int(info['DIMENSION'])
        for i in range(0, N):
            array_str = infile.readline().strip().split()
            array_float = []
            for j in array_str:
                array_float.append(float(j))
            nodelist.append(array_float)

    # Close input file
    infile.close()

    return info, nodelist


def compute_euclidean_distance_matrix(locations):
    #Creates callback to return distance between points.
    distances = []
    for from_node in locations:
        distances_row = []
        for to_node in locations:
            # Euclidean distance
            distances_row.append(
            math.hypot((from_node[0] - to_node[0]),
                (from_node[1] - to_node[1])))
        distances.append(distances_row)
    return distances

files = ['ulysses16.tsp', 'br17.atsp', 'ftv70.atsp', 'eil76.tsp'] #list of availavle files

NOME = 'ftv70.atsp' #write the file you want to study

def data(nome):
    info, nodelist = openFile(nome)
    if nome.split('.')[1] == 'atsp':
        distance_matrix = nodelist
    else:
        distance_matrix = compute_euclidean_distance_matrix(nodelist)
    return distance_matrix
distance_matrix = data(NOME)


