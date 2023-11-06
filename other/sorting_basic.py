import svgwrite
import draw_histo as dh
import random

d = svgwrite.Drawing('histo-unsorted.svg', size=('410', '210'))
values = random.sample(range(5, 30), k=20)
dh.make_histo(d, values, 5, 5, 400, 200)
d.save(pretty=True)

d = svgwrite.Drawing('histo-sorted.svg', size=('410', '210'))
values.sort()
values = [dh.HistoValue(v, highlight=True) for v in values]
dh.make_histo(d, values, 5, 5, 400, 200)
d.save(pretty=True)