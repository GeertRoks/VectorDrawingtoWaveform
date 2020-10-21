import numpy as np
import matplotlib.pyplot as plt
import math

fs = 48000
f = 440

t = np.arange(0., 1., f/fs)

def linearBezier(p0, p1, t):
    pFinal = np.zeros(2)
    pFinal[0] = (1-t) * p0[0] + t*p1[0]
    pFinal[1] = (1-t) * p0[1] + t*p1[1]

    return pFinal

def linearBezierComplex(p0, p1, t):
    pFinal = (1-t) * np.real(p0) + t*np.real(p1) + 1.0j*((1-t) * np.imag(p0) + t*np.imag(p1))
    return pFinal

x = np.zeros(math.floor(fs/f))

for ti in range(np.size(t)-1):
    x[ti] = linearBezier(np.array([-1,-1]), np.array([1,1]), ti)[0]

def bezierOscillator(f, fs, seconds):
    num_samples = fs * seconds
    step_size = f/fs # step size: 1/(samples per period) = 1/(fs/f) = f/fs
    offset = 0.5

    # setup the step waveform through the bezier curve saw form (add option for triangle form)
    t = np.resize(np.arange(0., 1., step_size), num_samples)
    t = np.where(t+offset > 1.0, t-(1-offset), t+offset)

    p0 = -1-1j
    p1 = 1+1j

    x = linearBezierComplex(p0, p1, t)

    # extract coordinates
    x_real = np.real(x) * np.pi
    x_imag = np.imag(x) * np.pi

    # generate sines
    A = 0.8
    y_real = A * np.cos(x_real)
    y_imag = A * np.sin(x_imag)


    # Plot results
    #plt.figure(1,(9.5,6))

    #plt.subplot(211)
    #plt.plot(t, x_real, label="x_real")
    #plt.plot(t, x_imag, label="x_imag")
    #plt.autoscale(tight = True)

    #plt.subplot(212)
    #plt.plot(np.arange(0,num_samples/fs,1/fs), y_real, label="y_real")
    #plt.plot(np.arange(0,num_samples/fs,1/fs), y_imag, label="y_imag")
    #plt.autoscale(tight = True)

    #plt.tight_layout()
    #plt.legend()
    #plt.show()

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

