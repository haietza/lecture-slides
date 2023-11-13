import dataclasses
import typing
import svgwrite
import draw_style as ds
import math

NODE_SIZE = 40

@dataclasses.dataclass
class HistoValue:
	value: int
	classes: set[str] = dataclasses.field(default_factory=set)
	x: int = None

def make_histo(d, values, x, y, w, h):
	def make_hv(v):
		if isinstance(v, HistoValue): return v
		return HistoValue(v)
	
	values = [make_hv(x) for x in values]
	mx = max(x.value for x in values)

	bars = []
	for i,v in enumerate(values):
		barh = v.value * h / mx
		x1 = i * w / len(values)
		x2 = (i + 1) * w / len(values)
		v.x = x+x1
		rect = d.rect(insert=(x+x1, y+h - barh), size=(x2-x1, barh), id='bar%02d' % i)
		rect.attribs['class'] = ' '.join(['bar'] + list(v.classes))
		bars.append((rect, v.value))

	bars.sort(key=lambda x: x[1])
	for rect,v in bars:
		d.add(rect)