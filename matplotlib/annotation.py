import matplotlib.pyplot as plt
import numpy as np


# You could use two calls to ax.annotate - one to add the text and one to draw an arrow with flat ends spanning the range you want to annotate:
xx = np.linspace(0,10)
yy = np.sin(xx)

fig, ax = plt.subplots(1,1, figsize=(12,5))
ax.plot(xx,yy)
ax.set_ylim([-2,2])

ax.annotate('', xy=(4, 1), xytext=(6, 1), xycoords='data', textcoords='data',
            arrowprops={'arrowstyle': '|-|'})
ax.annotate('important\npart', xy=(5, 1.5), ha='center', va='center')


# a arrow to point axvspan()
import matplotlib.pyplot as plt

plt.axvspan(76, 76, facecolor='g', alpha=1)
plt.annotate('This is awesome!',
             xy=(76, 0.75),
             xycoords='data',
             textcoords='offset points',
             arrowprops=dict(arrowstyle="->"))
plt.show()


import matplotlib.pyplot as plt

x_position = [1,6,2,7,4,5]
y_position = [8,4,7,7,2,4]

plt.plot(x_position, y_position, 'rx')

labels = ['text{}'.format(i) for i in range(len(x_position))]
for label, x, y in zip(labels, x_position, y_position):
    plt.annotate(label, xy=(x, y), xytext=(2, 2),
    arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()