import numpy as np
import matplotlib.pyplot as plt
import math

def linearBezier(p0, p1, t):
    pFinal = np.zeros(2)
    pFinal[0] = (1-t) * p0[0] + t*p1[0]
    pFinal[1] = (1-t) * p0[1] + t*p1[1]

    return pFinal

def linearBezierComplex(p0, p1, t):
    pFinal = (1-t) * np.real(p0) + t*np.real(p1) + 1.0j*((1-t) * np.imag(p0) + t*np.imag(p1))
    return pFinal


def bezierOscillator(f, fs, seconds, readType = "forward"):
    '''

        Input:
            f(float):           frequency of the oscillator
            fs(int):            sampling rate of the oscillator
            seconds(float):     duration of the synthesized sound in seconds
            readType(string):   The way how the oscillator reads the vector. Options: forward, backward and backforth

        Output:
            y_real(numpy.array):    synthesized sound from the horizontal movement over the vector image (x-axis, real)
            y_imag(numpy.array):    synthesized sound from the vertical movement over the vector image (y-axis, imaginary)

    '''
    # init parameters
    num_samples = fs * seconds
    step_size = f/fs # step size: 1/(samples per period) = 1/(fs/f) = f/fs
    offset = 0.5

    # setup the step waveform t through the bezier curve: choice for forward, backward or back-and-forth
    if (readType == "forward" or readType == "backward"):
        t = np.arange(0., 1., step_size)
        offset_index = np.where(t >= offset)[0][0]
        t = np.resize(t, num_samples + offset_index)
        t = t[offset_index:]

        if (readType == "backward"):
            t = np.where(t, 1-t, 1.)

    elif (readType == "backforth"):
        half_t = np.arange(0.,1., step_size*2)
        offset_index = np.where(half_t >= offset)[0][0]
        t = np.resize(np.append(half_t, half_t[::-1]), num_samples + offset_index)
        t = t[offset_index:]

    else:
        return 0

    # vector coördinates
    p0 = -1-1j
    p1 = 1+1j

    # get signal
    x = linearBezierComplex(p0, p1, t)

    # extract horizontal and vertical movement
    x_real = np.real(x)
    x_imag = np.imag(x)

    # Scale amplitude of signals
    A = 0.8
    y_real = A * x_real
    y_imag = A * x_imag


    # Plot results
    plt.figure(1,(9.5,6))

    plt.subplot(211)
    plt.plot(t, x_real, label="x_real")
    plt.plot(t, x_imag, label="x_imag")
    plt.autoscale(tight = True)

    plt.subplot(212)
    plt.plot(np.arange(0,num_samples/fs,1/fs), y_real, label="y_real")
    plt.plot(np.arange(0,num_samples/fs,1/fs), y_imag, label="y_imag")
    plt.autoscale(tight = True)

    plt.tight_layout()
    plt.legend()
    plt.show()

    return (y_real, y_imag)


def playSound(sound, fs):
    import pygame
    from time import sleep

    sound = (sound*32768).astype(np.int16)
    pygame.mixer.pre_init(fs, size=-16, channels=1)
    pygame.mixer.init()
    audio = pygame.sndarray.make_sound(sound)

    audio.play()
    sleep(0.01)

