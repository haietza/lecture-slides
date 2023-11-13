import svgwrite
import draw_histo as dh
import random
import json

values = [dh.HistoValue(v) for v in random.sample(range(5, 30), k=10)]

filename = 'bubble.svg'
d = svgwrite.Drawing(filename, size=('410', '210'))
d.embed_stylesheet(content="""
.bar {
	fill: #ffb86c;
	stroke: white;
	stroke-width: 2;
}
.bar.locked {
	fill: #ff7f2a;
}
.bar.focus {
	fill: #ff6666;
}
""")

dh.make_histo(d, values, 5, 5, 400, 200)
d.save(pretty=True)

animation = [[]]
k = 0 # do we want to do all the values?
for i in range(1, len(values)-k):
	animation.append([{
			'element': '#bar{:02d}'.format(i-1),
			'modifier': 'class',
			'parameters': ["bar focus"],
			'duration': 500,
		},
		{
			'element': '#bar{:02d}'.format(i),
			'modifier': 'class',
			'parameters': ["bar focus"],
			'duration': 500,
		}])
	if (values[i].value < values[i-1].value):
		animation.append([{
				'element': '#bar{:02d}'.format(i-1),
				'modifier': 'attr',
				'parameters': [{'x': str(values[i].x)}],
				'duration': 1500,
			},
			{
				'element': '#bar{:02d}'.format(i),
				'modifier': 'attr',
				'parameters': [{'x': str(values[i-1].x)}],
				'duration': 1500,
			}])
		values[i].x, values[i-1].x = values[i-1].x, values[i].x
	animation.append([{
			'element': '#bar{:02d}'.format(i-1),
			'modifier': 'attr',
			'parameters': [{'class': "bar"}],
			'duration': 500,
		},
		{
			'element': '#bar{:02d}'.format(i),
			'modifier': 'attr',
			'parameters': [{'class': "bar"}],
			'duration': 500,
		}])
animation.append([{
		'element': '#bar{:02d}'.format(len(values)-k-1),
		'modifier': 'class',
		'parameters': "bar locked",
		'duration': 500,
	}])

meta = {'setup': [], 'animation': animation}
fragments = """<span class="fragment"></span>\n""" * (len(animation)-1)
with open("bubble.html", "w") as htm:
	print(f"""{fragments}
<div data-animate data-load="{filename}">
<!--
{json.dumps(meta, indent=4)}
-->
</div>""", file=htm)