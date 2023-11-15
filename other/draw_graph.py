import dataclasses
import typing
import svgwrite
import math

NODE_SIZE = 20

@dataclasses.dataclass
class GraphNode:
	pos: tuple
	content: typing.Any = None
	size: int = NODE_SIZE
	classes: set = dataclasses.field(default_factory=set)

	def __hash__(self):
		return hash(id(self))

@dataclasses.dataclass
class GraphEdge:
	src: GraphNode
	dst: GraphNode
	directed: bool = False
	cost: typing.Any = None
	classes: set = dataclasses.field(default_factory=set)

	def __eq__(self, other):
		if self.directed != other.directed:
			return False
		if self.directed:
			return self.src == other.src and self.dst == other.dst
		else:
			return (self.src == other.src and self.dst == other.dst) or (self.src == other.dst and self.dst == other.src)
		
	def __hash__(self):
		if self.directed:
			return hash((self.directed, self.src, self.dst))
		else:
			return hash((self.directed, hash(self.src) ^ hash(self.dst)))
		
@dataclasses.dataclass
class Graph:
	nodes: set = dataclasses.field(default_factory=set)
	edges: set = dataclasses.field(default_factory=set)

	def size(self):
		return (
			max(n.pos[0] + n.size for n in self.nodes) - min(n.pos[0] - n.size for n in self.nodes)+10,
			max(n.pos[1] + n.size for n in self.nodes) - min(n.pos[1] - n.size for n in self.nodes)+10,
		)

	def draw(self, d, x, y):
		arrow = d.marker(size=(4,3), markerUnits='strokeWidth')
		arrow.viewbox(0, 0, 10, 10)
		arrow.add(d.path(d="M 0 0 L 10 5 L 0 10 z", fill='white'))
		d.defs.add(arrow)

		dx = min(n.pos[0] - n.size for n in self.nodes) - (x+5)
		dy = min(n.pos[1] - n.size for n in self.nodes) - (y+5)
		def adj(pt):
			x, y = pt
			return (x-dx, y-dy)
		
		for e in self.edges:
			edge = d.line(adj(e.src.pos), adj(e.dst.pos))
			edge.attribs['class'] = ' '.join(['edge'] + list(e.classes))
			if e.directed:
				edge.set_markers((None, None, arrow))
			d.add(edge)

			if e.cost is not None:
				pass

		for n in self.nodes:
			node = d.circle(adj(n.pos), n.size)
			node.attribs['class'] = ' '.join(['node'] + list(e.classes))
			d.add(node)

			if n.content is not None:
				d.add(d.text(str(n.content), insert=adj(n.pos),
					font_size=24, font_family='sans-serif',
					text_anchor="middle", dominant_baseline="central"))
				
def nx_to_graph(G, layout=None):
	if layout is None:
		import networkx as nx
		layout = nx.drawing.spring_layout(G)
	mindist = math.inf
	for k1,v1 in layout.items():
		for k2,v2 in layout.items():
			if k1 == k2: continue
			dist = (v1[0]-v2[0])**2 + (v1[1]-v2[1])**2
			if dist < mindist: mindist = dist
	mindist = math.sqrt(mindist)
	scale = 100/mindist

	nodedict = dict()
	graph = Graph()
	for n in G.nodes:
		pos = layout[n]
		node = GraphNode((pos[0]*scale, pos[1]*scale), n)
		graph.nodes.add(node)
		nodedict[n] = node

	for a,b in G.edges:
		graph.edges.add(GraphEdge(nodedict[a], nodedict[b]))
	return graph