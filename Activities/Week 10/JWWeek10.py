# Joyce Woznica
# Week 10: Social Network Analysis
# 10.2

import networkx as nx
g = nx.Graph()

g.add_edge(1,2)
g.add_node("spam")
g.nodes()
g.edges()
g.add_edge(1,"spam")
g.edges()

g.add_nodes_from([3,4])
g.add_edges_from([(1,3),(3,4)])
g.nodes()
g.edges()

# add some color
g.add_node(5, color='blue')
g.node[1]['color'] = 'red'
g.nodes(data=True)

# now update the weights of the lines between
g.add_edge(2,5, weight=4.7)
#g.edge[1][2]['weight'] = 1.2 
#g.edge[1][2] is dictionary of edge from 1 to 2
g.edges(data=True)

g.neighbors(1)

# the matrix
adj_matrix = nx.adjacency_matrix(g)
type(adj_matrix)
amatrix = adj_matrix.todense()
type(amatrix)
amatrix

# degrees
deg = nx.degree(g)
type(deg)
deg
# doesn't work
min(deg.values())
max(deg.values())

# doesn't work
sorteddeg = sorted(deg.items(), key = lambda x: x[1])
for node in sorteddeg:
    print(node)
    
dg = nx.DiGraph()
dg.add_weighted_edges_from([(1,2,.5),(3,1,.75)])
dg.nodes()
dg.edges(data=True)
dg.out_degree(1)
dg.out_degree(1, weight='weight')

nx.connected_components(g)
comp_list = list(nx.connected_components(g))
comp_list
g.add_node(6)
comp_list = list(nx.connected_components(g))
comp_list

import matplotlib.pyplot as plt
nx.draw(g)
plt.show()

def trim_degrees(g, degree=1):
    g2 = g.copy()
    d = nx.degree(g2)
    for n in g2.nodes():
        if d[n]<=degree: 
            g2.remove_node(n)
    return g2

core = trim_degrees(g)
len(core)
core.nodes()
core.edges()

import os
api_key=os.environ['APIKEY']

# 10.3
import geopy
from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("Hinds Hall, Syracuse, NY")
print(location.address)
location = geolocator.reverse("43.0382155,-76.1333455471294")
print(location.address)

# Find the following addresses
#1. lat = 42.773760, long = -78.786973
location = geolocator.reverse("42.773760,-78.786973")
print(location.address)

#2. lat = 44.854865, long = -93.242215
location = geolocator.reverse("44.854865,-93.242215")
print(location.address)

#3. lat = 42.999775, long = -78.787046
location = geolocator.reverse("42.999775,-78.787046")
print(location.address)

#4. lat = 43.183994, long = -76.236695
location = geolocator.reverse("43.183994,-76.236695")
print(location.address)

#5. lat = 40.689249, long = -74.044500
location = geolocator.reverse("40.689249,-74.044500")
print(location.address)









