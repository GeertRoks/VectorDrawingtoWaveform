import bezierCurves as bezier
import utilFunctions as util

import numpy as np
import math

# point up /\
point_up = [-1-1j, 0+1j, 1-1j]
point_down = [-1+1j, 0-1j, 1+1j]
triangle = [-1-1j, 0+1j, 1-1j, -1-1j]
square = [-1-1j, -1+1j, 1+1j, 1-1j, -1-1j]
star = [0+1j, 0.6-0.8j, -0.95+0.31j, 0.95+0.31j, -0.6-0.8j, 0+1j]

def multiLinearBezierOscillator(points, f, fs, duration, readDirection = "forward", plot = False):
    '''
        Input:
            points(array(complex)):     Array of complex numbers that denote the points of the bezier figure
            f(float):                   frequency of the oscillator
            fs(int):                    sampling rate of the oscillator
            duration(float):            duration of the synthesized sound in seconds
            readDirection(string):      The way how the oscillator reads the vector. Options: forward, backward and backforth
            plot(boolean):              Denotes if the result has to be plot or not

        Output:
            y_real(numpy.array):    synthesized sound from the horizontal movement over the vector image (x-axis, real)
            y_imag(numpy.array):    synthesized sound from the vertical movement over the vector image (y-axis, imaginary)

    '''

    # init parameters
    num_lines = np.size(points) - 1
    num_samples = int(math.ceil(fs * duration))
    step_size = f/fs # step size for one line: 1/(samples per period) * num_lines = 1/(fs/f) * numlines = f*num_lines/fs

    phase_offset = 0

    # generate phase ramp
    t = util.linearPhaseFunction(step_size, num_lines, readDirection, phase_offset)

    # get signal
    x = np.zeros(np.size(t), dtype = complex)
    for idx, ti in enumerate(t):
        # Write signal with correct points
        #   if first line, then math.floor(ti) == 0, thus points[0] and points[1]
        #   if second line, then math.floor(ti) == 1, thus points[1] and points[2]
        #   etc...
        x[idx] = bezier.linearBezierComplex(points[math.floor(ti)],points[math.ceil(ti)], ti-math.floor(ti))

    onePeriod = x

    # repeat the period for the amount needed to fill the duration
    x = np.resize(x, num_samples)

    # Scale amplitude of signals
    A = 0.8
    fullSample = A * x

    # Plot results
    if (plot):
        util.plotResults(onePeriod, fullSample, num_lines, fs, f, duration, readDirection, phase_offset)

    return fullSample

