from vpython import *
import random

jmax = 20
x, y = 0, 0
graph = graph(width=500, height=500, title='Random Walk', xtitle='x', ytitle='y')
pts = gcurve(color=color.yellow)

for i in range(jmax + 1):
    pts.plot(pos=(x, y))
    x += (random.random() - 0.5) * 2
    y += (random.random() - 0.5) * 2
    pts.plot(pos=(x, y))
    rate(1000)