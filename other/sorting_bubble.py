import svgwrite
import draw_histo as dh
import random

values = [dh.HistoValue(v) for v in random.sample(range(5, 30), k=10)]

d = svgwrite.Drawing('bubble-00.svg', size=('410', '210'))
dh.make_histo(d, values, 5, 5, 400, 200)
d.save()

frame = 1
for i in range(len(values)-1):
	d = svgwrite.Drawing('bubble-%02d.svg' % frame, size=('410', '210'))
	values[i].highlight = True
	values[i+1].highlight = True
	dh.make_histo(d, values, 5, 5, 400, 200)
	d.save()
	frame += 1
	
	d = svgwrite.Drawing('bubble-%02d.svg' % frame, size=('410', '210'))
	values[i].highlight = False
	values[i+1].highlight = False
	if values[i].value > values[i+1].value:
		values[i], values[i+1] = values[i+1], values[i]
	dh.make_histo(d, values, 5, 5, 400, 200)
	d.save()
	frame += 1