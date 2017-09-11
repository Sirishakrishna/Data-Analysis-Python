import networkx as ny
import matplotlib.pyplot as plt


# Creating an empty graph

g=ny.Graph()

# If we want to create a digraph

g=ny.DiGraph()

# Creating nodes

g.add_node(0)
g.add_node(4)
g.add_node(5)
g.add_node(5)

# Adding edges

g.add_edge(0,4)
g.add_edge(6,7)
g.add_edges_from([(2,3),(6,7)])

# Graph info

print ny.info(g)

# Plotting

ny.draw(g)

plt.show()

