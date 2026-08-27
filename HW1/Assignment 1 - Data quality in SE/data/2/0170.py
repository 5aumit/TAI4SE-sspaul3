# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 20:06:32 2020

@author: Supriyo
"""

import networkx as nx
import matplotlib.pyplot as plt 

g=nx.Graph()


#l=[1,2,3]

# g.add_node(1)
# g.add_node(2)
# g.add_node(3)
    # g.add_nodes_from(l)
    
    # g.add_edge(1,2)
    # g.add_edge(2,3)
    # g.add_edge(3,1)

# print(g.nodes())
# print(g.edges())

g=nx.complete_graph(10)

h=nx.gnp_random_graph(10,0.5)#0.55 is the probability
nx.draw(g)
nx.draw(h)
plt.show()

nx.write_gexf(g,"test.gexf")