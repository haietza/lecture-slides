import dataclasses
import typing
import svgwrite
import draw_style as ds
import math

NODE_SIZE = 40

@dataclasses.dataclass
class HistoValue:
	value: int
	highlight: bool = False
	style: dict = dataclasses.field(default_factory=dict)

def make_histo(d, values, x, y, w, h):
	def make_hv(v):
		if isinstance(v, HistoValue): return v
		return HistoValue(v)
	
	values = [make_hv(x) for x in values]
	mx = max(x.value for x in values)

	for i,v in enumerate(values):
		barh = v.value * h / mx
		x1 = i * w / len(values)
		x2 = (i + 1) * w / len(values)
		style = {
			'stroke': ds.normal_stroke,
			'fill': ds.highlight_fill if v.highlight else ds.normal_fill,
			'stroke_width': ds.stroke_width,
		}
		style.update(v.style)
		d.add(d.rect(insert=(x+x1, y+h - barh), size=(x2-x1, barh), **style))