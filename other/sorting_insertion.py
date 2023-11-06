import svgwrite
import draw_histo as dh
import draw_style as ds
import random
import math

values = [dh.HistoValue(v) for v in random.sample(range(5, 30), k=10)]

d = svgwrite.Drawing('insertion-00.svg')
dh.make_histo(d, values, 5, 5, 400, 200)
d.save()

frame = 1
for i in range(len(values)):
	while i > 0 and values[i-1].value > values[i].value:
		d = svgwrite.Drawing('insertion-%02d.svg' % frame, size=('410', '210'))
		values[i  ].style = {'fill': "#FF6666"}
		dh.make_histo(d, values, 5, 5, 400, 200)
		d.save()
		frame += 1
		
		values[i  ].style = {}
		values[i-1].style = {}
		values[i], values[i-1] = values[i-1], values[i]
		i -= 1
	values[i].highlight = True

	d = svgwrite.Drawing('insertion-%02d.svg' % frame, size=('410', '210'))
	dh.make_histo(d, values, 5, 5, 400, 200)
	d.save()
	frame += 1