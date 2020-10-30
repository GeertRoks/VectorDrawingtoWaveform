import numpy as np
import math

import bezierCurves as bezier
import utilFunctions as util

circle = np.array([ [1+0j,1+1j, 0+1j], [0+1j,-1+1j, -1+0j], [-1+0j,-1-1j,0-1j], [0-1j,1-1j,1+0j] ])

def multiQuadraticBezierOscillator(path, f, fs, duration, readDirection = "forward", plot=False):
    '''
        Input:
            path(array(array):          Array of array with complex numbers that denote the individual lines of the bezier figure
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
    num_lines = path.shape[0]
    num_samples = int(math.ceil(fs * duration))
    step_size = f/fs # step size for one line: 1/(samples per period) * num_lines = 1/(fs/f) * numlines = f*num_lines/fs

    phase_offset = 0.5 # TODO: add scalable offset

    # get phase function
    t = util.linearPhaseFunction(step_size, num_lines, readDirection, phase_offset)

    # get signal
    x = np.zeros(np.size(t), dtype = complex)
    for idx, ti in enumerate(t):
        # Write signal with correct points
        #   if first line, then math.floor(ti) == 0, thus points[0] and points[1]
        #   if second line, then math.floor(ti) == 1, thus points[1] and points[2]
        #   etc...
        x[idx] = bezier.quadraticBezierComplex(path[math.floor(ti)][0],path[math.floor(ti)][1],path[math.floor(ti)][2], ti-math.floor(ti))

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
        util.plotResults(x_real, x_imag, y_real, y_imag, fs, f, t, duration, phase_offset)

    return (y_real, y_imag)
