import dataclasses
import typing
import svgwrite
import draw_style as ds
import math

NODE_SIZE = 40
NODE_XPAD = 2
NODE_YPAD = 15

def draw_tree_edge(d, c1, c2):
	if c1 is None or c2 is None: return
	x1, y1, r1 = c1
	x2, y2, r2 = c2
	angle = math.atan2(y2-y1, x2-x1)
	x1 += math.cos(angle) * r1
	x2 -= math.cos(angle) * r2
	y1 += math.sin(angle) * r1
	y2 -= math.sin(angle) * r2
	d.add(d.line((x1, y1), (x2, y2), stroke=ds.normal_stroke,
        stroke_width=ds.stroke_width))
	
def draw_object(d, obj, x=0, y=0):
	if obj is None: return x, None
	return obj.draw(d, x, y)

@dataclasses.dataclass
class BinaryNode:
	contents: typing.Any
	annot: typing.Any = None
	left: 'Node' = None
	right: 'Node' = None

	# return x, anchor
	def draw(self, d, x, y):
		y2 = y + NODE_SIZE + NODE_YPAD
		yc = y + NODE_SIZE // 2

		x, c1 = draw_object(d, self.left, x, y2)
		xc = x + NODE_XPAD + NODE_SIZE // 2
		d.add(d.circle((xc, yc), NODE_SIZE // 2,
			stroke=ds.normal_stroke, fill=ds.normal_fill,
			stroke_width=ds.stroke_width))
		d.add(d.text(str(self.contents), insert=(xc, yc),
			font_size=16, font_family='sans-serif',
			text_anchor="middle", dominant_baseline="central"))
		
		x += 2 * NODE_XPAD + NODE_SIZE
		x, c2 = draw_object(d, self.right, x, y2)
		
		cr = (xc, yc, NODE_SIZE // 2)
		draw_tree_edge(d, cr, c1)
		draw_tree_edge(d, cr, c2)
		return x, cr

@dataclasses.dataclass
class Subtree:
	contents: typing.Any
	annot: typing.Any = None

	# return x, anchor
	def draw(self, d, x, y):
		r = NODE_SIZE // 2
		d.add(d.polygon([(x+r, y), (x, y+3*r), (x+2*r, y+3*r)], 
			stroke=ds.normal_stroke, fill=ds.normal_fill,
			stroke_width=ds.stroke_width))
		d.add(d.text(str(self.contents), insert=(x+r, y+2*r),
			font_size=16, font_family='sans-serif',
			text_anchor="middle", dominant_baseline="central"))
		return x+2*r, (x+r, y, 0)