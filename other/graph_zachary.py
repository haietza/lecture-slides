import svgwrite
import draw_graph as dg
import networkx as nx

def base_drawing(filename, size=(200,200)):
	d = svgwrite.Drawing(filename, size=size)
	d.embed_stylesheet(content="""
	.node {
		fill: #ffb86c;
		stroke: white;
		stroke-width: 2;
	}
	.edge {
		stroke: white;
		stroke-width: 2;
	}
	""")
	return d

G = nx.karate_club_graph()
layout = nx.drawing.spring_layout(G)

graph = dg.nx_to_graph(G, layout)
print(graph.size())
d = base_drawing('graph-zachary.svg', size=graph.size())
graph.draw(d, 0, 0)
d.save(pretty=True)