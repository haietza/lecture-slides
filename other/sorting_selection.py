import svgwrite
import draw_histo as dh
import draw_style as ds
import random
import math

values = [dh.HistoValue(v) for v in random.sample(range(5, 30), k=10)]

d = svgwrite.Drawing('selection-00.svg', size=('410', '210'))
dh.make_histo(d, values, 5, 5, 400, 200)
d.save()

frame = 1
for i in range(len(values)):
	minval, minndx = math.inf, -1
	for j in range(i, len(values)):
		if values[j].value < minval:
			minval, minndx = values[j].value, j
	j = minndx

	d = svgwrite.Drawing('selection-%02d.svg' % frame, size=('410', '210'))
	values[j].style = {'fill': "#FF6666"}
	dh.make_histo(d, values, 5, 5, 400, 200)
	d.save()
	frame += 1
	values[j].style = {}
	
	d = svgwrite.Drawing('selection-%02d.svg' % frame, size=('410', '210'))
	values[i], values[j] = values[j], values[i]
	values[i].highlight = True
	dh.make_histo(d, values, 5, 5, 400, 200)
	d.save()
	frame += 1