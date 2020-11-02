import os, glob, sys
import numpy as np
from itertools import permutations
from scipy.integrate import odeint
from classes.plotter import LorenzPlotter
from classes.lorenzSystem import LorenzSystem


def getRGBCodeFromRange(x, y, z, r=1):
    
    r = min(r, 255)
    factor = int(np.floor(255 / r))
    f = '{:02x}'
    rgbString = '#' \
            + f.format(x * factor) \
            + f.format(y * factor) \
            + f.format(z * factor) \
            + '40'

    return rgbString


def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size * j / count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()
    


def simpleRun():

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

    ps = odeint(ls.computeState, ls.initVector, time)

    points = [ps[:, 0], ps[:, 1], ps[:, 2]]


    print('plotting...')
    lp.plot(points)
    lp.save(imgFolder + 'out.png')

    print('done.')

def pertubingYRun():
    
    imgFolder = 'assets/images/'

    if not os.path.exists(imgFolder):
        os.makedirs(imgFolder)
    
    print('initialising...')

    start = 0
    stop = 100
    interval = 100
    vecLen = 3

    time = np.linspace(start, stop, num=(stop * interval))

    lp = LorenzPlotter()

    perms = list(permutations([0.1,0,0], (vecLen)))
    for perm in progressbar(perms, 'Solving: ', 60):

        ls = LorenzSystem()
        x = perm[0]
        y = perm[1]
        z = perm[2]
        ls.initVector = [x, y, z]

        # print('solving...')

        ps = odeint(ls.computeState, ls.initVector, time)
        points = [ps[:, 0], ps[:, 1], ps[:, 2]]

        lc = getRGBCodeFromRange(int(z*10), int(y*10), int(z*10), r=vecLen)

        lp.plot(points, lineColor=lc)

    lp.save()

    print('done')

def pertubingRhoRun():
    
    imgFolder = 'assets/images/'

    if not os.path.exists(imgFolder):
        os.makedirs(imgFolder)
    
    print('initialising...')

    start = 0
    stop = 100
    interval = 100
    rhoMax = 256 

    time = np.linspace(start, stop, num=(stop * interval))

    lp = LorenzPlotter()


    for i in progressbar(range(0, rhoMax, 16), 'Solving: ', 40):

        ls = LorenzSystem()
        ls.rho = i
        
        ps = odeint(ls.computeState, ls.initVector, time)
        points = [ps[:, 0], ps[:, 1], ps[:, 2]]

        lc = getRGBCodeFromRange(i, i, i, r=rhoMax)

        lp.plot(points, lineColor=lc)

    lp.save()

    print('done')

if __name__ == '__main__':

    pertubingYRun()
    pertubingRhoRun()
    
