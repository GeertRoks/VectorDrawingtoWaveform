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

    #offset = 0.5 # TODO: add scalable offset

    # setup the step waveform t through the bezier curve for one period: choice for forward, backward or back-and-forth
    if (readDirection == "forward" or readDirection == "backward"):
        t = np.arange(0., 1., step_size)
        t = t * num_lines

        # TODO: add scalable offset
        #offset_index = np.where(t >= offset)[0][0]
        #t = np.resize(t, num_samples + offset_index)
        #t = t[offset_index:]

        if (readDirection == "backward"):
            t = np.where(t, num_lines-t, num_lines)

    elif (readDirection == "backforth"):
        half_t = np.arange(0.,1., step_size*2)
        t = np.append(half_t, half_t[::-1]) * 4

        # TODO: add scalable offset
        #offset_index = np.where(half_t >= offset)[0][0]
        #t = np.resize(np.append(half_t, half_t[::-1]), num_samples + offset_index)
        #t = t[offset_index:]

    else:
        return 0

    # get signal
    x = np.zeros(np.size(t), dtype = complex)
    for idx, ti in enumerate(t):
        # Write signal with correct points
        #   if first line, then math.floor(ti) == 0, thus points[0] and points[1]
        #   if second line, then math.floor(ti) == 1, thus points[1] and points[2]
        #   etc...
        x[idx] = bezier.linearBezierComplex(points[math.floor(ti)],points[math.ceil(ti)], ti-math.floor(ti))

    # repeat the period for the amount needed to fill the duration
    x = np.resize(x, num_samples)

    # extract horizontal and vertical movement
    x_real = np.real(x)
    x_imag = np.imag(x)

    # Scale amplitude of signals
    A = 0.8
    y_real = A * x_real
    y_imag = A * x_imag

    # Plot results
    if (plot):
        util.plotResults(x_real, x_imag, y_real, y_imag, fs, f, t, duration)

    return (y_real, y_imag)

