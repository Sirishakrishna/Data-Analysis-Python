#Plotting Different Types of Graphs

import networkx as nx
import matplotlib.pyplot as plt

options_1 = {
 'with_labels': False,
 'node_color': 'black',
 'node_size': 50,
 'width': 1,
}

options_2 = {
 'with_labels': False,
 'node_color': 'grey',
 'node_size': 10,
 'linewidths': 0,
 'width': 0.1,
}

options_3 = {
 'with_labels': False,
 'node_color': 'grey',
 'node_size': 10,
 'linewidths': 0,
 'width': 0.1,
 'alpha': 0.3
}
# Drawing Complete Graph
G=nx.complete_graph(6)
plt.figure()
nx.draw_circular(G)
plt.savefig("complete_graph.png")

# Cycle Graph
G=nx.cycle_graph(10)
plt.figure()
nx.draw_circular(G)
plt.savefig("cycle_graph.png")

# lollipop Graph
G = nx.lollipop_graph(5, 2)
plt.figure()
nx.draw_circular(G)
plt.savefig("lollipop.png")

# petersen_graph
G= nx.petersen_graph()
plt.figure()
nx.draw_circular(G)
plt.savefig("Peterson_graph.png")

# barabasi_albert_graph
G = nx.barabasi_albert_graph(100, 3)
nx.draw_circular(G, **options_2)
plt.savefig("barabasi.png")



G = nx.complete_bipartite_graph(25,26)
nx.draw_shell(G, nlist=[range(0,25), range(25,51)], **options_3)
plt.savefig("complete_bipartite.png")