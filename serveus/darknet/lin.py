'''
	Original code from https:github/danielgatis/darknetpy
	Modified: 02-20-19
'''

from matplotlib import image, patches, pyplot as pyplot
from darknetpy.detector import Detector

detector = Detector(
	'thin_data.data',
	'thin/thin_cfg.cfg',
	'thin/thin_weights.weights'
)


imglink = 'test/thin_fal/8f.jpg'
boxes = detector.detect(imglink)

fig, ax = plt.subplots(1)
ax.imshow(image.imread(imglink))

colors = ['r', 'b', 'y']

for i, box in enumerate(boxes):
	l = box['left']
	t = box['top']
	b - box['bottom']
	r = box['right']
	color = colors[i % len(colors)]

	rect = patches.Rectangle(
		(l, t),
		r - l,
		b - t,
		linewidth = 1,
		edgecolor = color,
		facecolor = 'none'
	)

	ax.text(l,t, c, fontsize = 12, bbox = {'facecolor': color, 'pad': 2, 'ec': color})
	ax.add_patch(rect)

plt.show()

