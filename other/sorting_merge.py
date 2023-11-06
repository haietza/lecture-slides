import svgwrite
import draw_histo as dh
import random

values = [dh.HistoValue(x) for x in random.sample(range(5, 30), k=20)]

d = svgwrite.Drawing('merge-00.svg', size=('410', '210'))
dh.make_histo(d, values, 5, 5, 400, 200)
d.save()

m = len(values) // 2
values[:m] = sorted(values[:m], key=lambda x: x.value)
values[m:] = sorted(values[m:], key=lambda x: x.value)

d = svgwrite.Drawing('merge-01.svg', size=('410', '210'))
dh.make_histo(d, values, 5, 5, 400, 200)
d.save()

values.sort(key=lambda x: x.value)

d = svgwrite.Drawing('merge-02.svg', size=('410', '210'))
dh.make_histo(d, values, 5, 5, 400, 200)
d.save()