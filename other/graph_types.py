import graphviz

g = graphviz.Graph('graph-path', format='svg')
g.attr(rankdir='LR')
for i in range(6):
	g.edge(f"p_{i}", f"p_{i+1}")
g.render()