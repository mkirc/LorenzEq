import os, glob
import numpy as np
from scipy.integrate import odeint
from classes.plotter import LorenzPlotter
from classes.lorenzSystem import LorenzSystem





imgFolder = 'assets/images/'

if not os.path.exists(imgFolder):
    os.makedirs(imgFolder)


start = 0
stop = 100
interval = 100

print('initialising...')
time = np.linspace(start, stop, num=(stop * interval))

ls = LorenzSystem()
lp = LorenzPlotter()

print('solving...')
ps = ls.solveForTime(time)

ps = odeint(ls.computeState, ls.initVector, time)

points = [ps[:, 0], ps[:, 1], ps[:, 2]]


print('plotting...')
lp.plt(points, imgFolder + 'out.png')

print('done.')
