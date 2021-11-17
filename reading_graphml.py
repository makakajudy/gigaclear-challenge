from os import path
import pathlib
import networkx
import matplotlib.pyplot
from pathlib import Path
from networkx.classes.function import edges

cwd=Path(__file__).absolute().parent

network_data=networkx.read_graphml(cwd/'problem.graphml')
#C:\Users\makak\OneDrive\Desktop\Gigaclear challenge-solution\problem.graphml
networkx.draw(network_data)
#matplotlib.pyplot.show()# displays the network 

#variables to hold the number of the network items

#nodes
cabinet_counter=0 
pot_counter=0
chamber_counter=0

#edges
verge_length=0
road_length=0


for node in network_data.nodes(data=True):
    
    #accessing second element of the tuple and 
    #converting it into a dict
    network_nodes=dict(node[1])

    #looping thru the network and taking count of the nodes    
    for x,y in network_nodes.items():
        if network_nodes[x]=='Cabinet':
            cabinet_counter+=1
        if network_nodes[x]=="Pot":
            pot_counter+=1
        if network_nodes[x]=='Chamber':
            chamber_counter+=1




for edges in network_data.edges(data=True):
     
      network_edges=dict(edges[2])#accessing the third elelment of the tuple
      
      if network_edges['material']=='verge':
          verge_length+=network_edges['length']
      else:
          road_length+=network_edges['length']


