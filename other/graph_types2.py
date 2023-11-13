import svgwrite
import draw_graph as dg
import math
import random

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

### PATH
nodes = [
	dg.GraphNode((100*4, 50)),
	dg.GraphNode((100*3, 50)),
	dg.GraphNode((100*2, 50)),
	dg.GraphNode((100, 125)),
	dg.GraphNode((100*2, 200)),
	dg.GraphNode((100*3, 200)),
	dg.GraphNode((100*4, 200)),
]

graph = dg.Graph()
for n in nodes:
	graph.nodes.add(n)

for i in range(1, len(nodes)):
	graph.edges.add(dg.GraphEdge(nodes[i-1], nodes[i]))

d = base_drawing('graph-path.svg', size=graph.size())
graph.draw(d, 0, 0)
d.save(pretty=True)

### CYCLE
nodes.append(dg.GraphNode((100*5, 125)))

graph = dg.Graph()
for n in nodes:
	graph.nodes.add(n)

for i in range(len(nodes)):
	graph.edges.add(dg.GraphEdge(nodes[i-1], nodes[i]))

d = base_drawing('graph-cycle.svg', size=graph.size())
graph.draw(d, 0, 0)
d.save(pretty=True)

### BIPARTITE
g1 = [dg.GraphNode((50, 50+100*i)) for i in range(5)]
g2 = [dg.GraphNode((350, 50+100*i)) for i in range(5)]

graph = dg.Graph()
for n in g1 + g2:
	graph.nodes.add(n)

for n in g1: graph.edges.add(dg.GraphEdge(n, random.choice(g2)))
for n in g2: graph.edges.add(dg.GraphEdge(random.choice(g1), n))
while len(graph.edges) < 10:
	graph.edges.add(dg.GraphEdge(random.choice(g1), random.choice(g2)))

d = base_drawing('graph-bipartite.svg', size=graph.size())
graph.draw(d, 0, 0)
d.save(pretty=True)

### COMPLETE
K, radius = 7, 200
nodes = []
for i in range(K):
	nodes.append(dg.GraphNode((radius*math.cos(2*i*math.pi/K), radius*math.sin(2*i*math.pi/K))))

graph = dg.Graph()
for n in nodes:
	graph.nodes.add(n)

for a in nodes:
	for b in nodes:
		graph.edges.add(dg.GraphEdge(a, b))

d = base_drawing('graph-complete.svg', size=graph.size())
graph.draw(d, 0, 0)
d.save(pretty=True)

### PLANAR
ROWS = 4
prev = None
x, y = 0, 0
graph = dg.Graph()
for r in range(ROWS, 0, -1):
	curr = []
	for i in range(r):
		curr.append(dg.GraphNode((x+150*i, y)))
	for n in curr:
		graph.nodes.add(n)
	for i in range(1, len(curr)):
		graph.edges.add(dg.GraphEdge(curr[i-1], curr[i]))

	if prev is not None:
		for i,n in enumerate(curr):
			graph.edges.add(dg.GraphEdge(n, prev[i]))
			graph.edges.add(dg.GraphEdge(n, prev[i+1]))
	prev = curr
	x += 75
	y -= 100

d = base_drawing('graph-planar.svg', size=graph.size())
graph.draw(d, 0, 0)
d.save(pretty=True)

### TREES