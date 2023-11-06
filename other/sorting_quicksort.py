import svgwrite
import draw_histo as dh
import draw_style as ds
import random

values = [dh.HistoValue(x) for x in random.sample(range(5, 40), k=30)]

d = svgwrite.Drawing('quick-00.svg')
dh.make_histo(d, values, 5, 5, 400, 200)
d.save()

pivot = sorted(values, key=lambda x: x.value)[10]
below = [x for x in values if x.value < pivot.value]
above = [x for x in values if x.value > pivot.value]
random.shuffle(below)
random.shuffle(above)
pivot.highlight = True
values = below + [pivot] + above

d = svgwrite.Drawing('quick-01.svg', size=('410', '210'))
dh.make_histo(d, values, 5, 5, 400, 200)
mx = max(x.value for x in values)
y = 5 + 200 - 200 * pivot.value // mx
print(y)
d.add(d.line(start=(0, y), end=(405, y), stroke=ds.highlight_stroke, stroke_width=ds.stroke_width, stroke_dasharray="5 3"))
d.save()

values.sort(key=lambda x: x.value)
for v in values:
    v.highlight = True

d = svgwrite.Drawing('quick-02.svg', size=('410', '210'))
dh.make_histo(d, values, 5, 5, 400, 200)
d.save()