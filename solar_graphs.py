import matplotlib.pyplot as plt
import pylab
import numpy as np


def graphs():
    """
    Showing statistics of the system
    """
    with open("stats.txt", "r") as f:
        data = list(map(lambda x: x.rstrip().split(), f.readlines()))
    velocity = []
    distance = []
    time = []
    for s in data:
        velocity.append(float(s[1]))
        distance.append(float(s[0]))
        time.append(float(s[2]))

    velocity = np.array(velocity)
    distance = np.array(distance)
    time = np.array(time)

    pylab.subplot(3, 1, 1)
    pylab.plot(time, distance, color='black')
    pylab.title(r'distance from time')

    pylab.subplot(3, 1, 2)
    pylab.plot(time, velocity, color='black')
    pylab.title(r'velocity from time')

    pylab.subplot(3, 1, 3)
    pylab.plot(distance, velocity, color='black')
    pylab.title(r'velocity from distance')

    plt.show()