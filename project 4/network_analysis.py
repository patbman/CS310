# -*- coding: utf-8 -*-
"""
Written by: Patrick Bowden
"""

# Importing modules
from states import states
import pandas as pd
import networkx as nx
import community
import operator

# Importing file and data manipulation
infile = pd.read_excel('data/State_to_State_Migrations_Table_2015.xls',header=0,index_col=0,skiprows=6,skip_footer=8,na_values='N/A3')
infile = infile[infile.index.isin(states.values())]
stable = infile.loc[:, states.values()]
stable.fillna(0, inplace = True)

# Organizing the data for the graph
med = stable.median(axis = 1)
allMed = med.median()
stable = stable >= allMed
stable = stable.unstack()
stable = stable[stable == True]
stable = stable.index.tolist()
stable = tuple(stable)

# Making the graph
netG = nx.Graph()
netG.add_edges_from(stable)
netG.remove_edges_from(netG.selfloop_edges())

bCent = nx.betweenness_centrality(netG)
bCent = ', '.join(sorted(bCent, key = bCent.get)[:5])
print('The 5 states that have the highest betweenness centrality are: ' + bCent)

cClose = nx.closeness_centrality(netG)
cClose = ', '.join(sorted(cClose, key = cClose.get)[:5])
print('The 5 states that have the highest closeness centrality are: ' + cClose)

conn = sorted(nx.connected_components(netG), key = len, reverse = True)
print('The graph has '+ str(len(conn)) + ' connected component(s)')

comdict = community.best_partition(netG)
comm = list(set([i for i in comdict.values()]))
mod = community.modularity(comdict, netG)
print('There are ' + str(len(comm)) + ' communities, with a modularity of: ' + str(mod))

comsort = sorted(comdict.items(), key = operator.itemgetter(1)) # Shows which states belong to which community, a bit messy but functional.
print('\nList of states with their community numbers: ' + str(comsort))

nx.draw(netG)
nx.write_graphml(netG, open('data/netG.graphml', 'wb'))