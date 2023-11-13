import svgwrite
import draw_graph as dg
import networkx as nx

def base_drawing(filename, size=(200,200)):
	d = svgwrite.Drawing(filename, size=size)
	d.embed_stylesheet(content="""
	.node {
		fill: #ffb86c;
		stroke: black;
		stroke-width: 2;
	}
	.edge {
		stroke: black;
		stroke-width: 2;
	}
	.edge.highlight {
		stroke: #ff7f2a;
		stroke-width: 10;
	}
	""")
	return d

G = nx.Graph()
G.add_edge(1,2,weight=7)
G.add_edge(2,3,weight=19)
G.add_edge(3,4,weight=8)
G.add_edge(5,6,weight=4)
G.add_edge(6,7,weight=16)
G.add_edge(7,8,weight=3)
G.add_edge(1,6,weight=15)
G.add_edge(2,6,weight=9)
G.add_edge(2,7,weight=11)
G.add_edge(2,8,weight=10)
G.add_edge(3,7,weight=12)
G.add_edge(3,8,weight=2)
G.add_edge(4,8,weight=14)

layout = nx.drawing.spring_layout(G, weight=None)
graph = dg.nx_to_graph(G, layout)
print(graph.size())

d = base_drawing('graph-minspantree.svg', size=graph.size())
graph.draw(d, 0, 0)
d.save(pretty=True)

T = nx.minimum_spanning_tree(G)
for a,b in T.edges:
	for e in graph.edges:
		if {e.src.content, e.dst.content} == {a, b}:
			print('found', a, b)
			e.classes.add('highlight')

d = base_drawing('graph-minspantree2.svg', size=graph.size())
graph.draw(d, 0, 0)
d.save(pretty=True)