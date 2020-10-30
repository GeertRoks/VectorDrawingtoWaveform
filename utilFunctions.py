import matplotlib.pyplot as plt
import numpy as np
import math
import pygame
from time import sleep

def plotResults(x_real, x_imag, y_real, y_imag, fs, f, t, duration, phase_offset):
    fig, axes = plt.subplots(3, 1, figsize=(9.5,9.5))

    # Bezier figure
    axes[0].plot(x_real[:int(fs/f)], x_imag[:int(fs/f)])
    axes[0].set_xlim((-1.5,1.5))
    axes[0].set_ylim((-1.5,1.5))
    x0,x1 = axes[0].get_xlim()
    y0,y1 = axes[0].get_ylim()
    axes[0].set_aspect(abs(x1-x0)/abs(y1-y0))
    axes[0].grid(b=True, which='major', color='k', linestyle='--')

    # Period plot
    # TODO plot period with phase offset and with segment lines intact
    num_lines = int(math.ceil(np.max(t)))
    period_t = np.where(t/num_lines - phase_offset < 0.0, t + (num_lines - phase_offset), t/num_lines - phase_offset)
    axes[1].plot(t, x_real[:np.size(t)], label="x_real")
    axes[1].plot(t, x_imag[:np.size(t)], label="x_imag")
    for xc in range(1,math.ceil(t[-1])):
        axes[1].axvline(x=xc, color ="red", linestyle='--')
    axes[1].autoscale(tight = True)

    # Synthesis plot
    axes[2].plot(np.arange(0,duration,1/fs), y_real, label="y_real")
    axes[2].plot(np.arange(0,duration,1/fs), y_imag, label="y_imag")
    axes[2].set_xlim((0,duration))
    axes[2].set_ylim((-1.,1.))

    plt.tight_layout()
    plt.legend()
    plt.show()

def plotBezier(bezier, t, curvePoints = np.array([])):
    fig, axes = plt.subplots(1, 1, figsize=(8,8))

    # setup axes
    axes.set_xlim((-1.5,1.5))
    axes.set_ylim((-1.5,1.5))
    x0,x1 = axes.get_xlim()
    y0,y1 = axes.get_ylim()
    axes.set_aspect(abs(x1-x0)/abs(y1-y0))
    axes.grid(b=True, which='major', color='k', linestyle=':')
    axes.axhline(0, color='black') # origin x-axis accent
    axes.axvline(0, color='black') # origin y-axis accent

    # plot bezier curve
    if bezier.dtype == 'complex':
        plt.plot(np.real(bezier), np.imag(bezier))
        # Add points to begin and end points and to control points if there are any
        plt.plot(np.real(bezier[0]),np.imag(bezier[0]), marker='x', color='red')
        plt.plot(np.real(bezier[-1]),np.imag(bezier[-1]), marker='x', color='red')
        if curvePoints.size != 0:
            for cp in curvePoints:
                plt.scatter(np.real(cp),np.imag(cp), marker='x', color='red')
    else:
        plt.plot(bezier[:,0], bezier[:,1])
        # Add points to begin and end points and to control points if there are any
        plt.plot(bezier[0,0], bezier[0,1], marker='x', color='red')
        plt.plot(bezier[-1,0],bezier[-1,1], marker='x', color='red')
        if curvePoints.size != 0:
            for cp in curvePoints:
                plt.scatter(cp[0],cp[1], marker='x', color='red')

    plt.show()

def playSound(sound, fs):
    sound = (sound*32768).astype(np.int16)
    pygame.mixer.pre_init(fs, size=-16, channels=1)
    pygame.mixer.init()
    audio = pygame.sndarray.make_sound(sound)

    audio.play()
    sleep(0.01)


def linearPhaseFunction(step_size, num_lines, readDirection='forward', phase_offset=0.0):
    # setup the step waveform t through the bezier curve for one period: choice for forward, backward or back-and-forth
    if (readDirection.lower() == "forward" or readDirection.lower() == "backward"):
        t = np.arange(0., 1., step_size)
        t = t * num_lines

        # TODO: add scalable offset
        #offset_index = np.where(t >= offset)[0][0]
        #t = np.resize(t, num_samples + offset_index)
        #t = t[offset_index:]

        if (readDirection.lower() == "backward"):
            t = np.where(t, num_lines-t, num_lines)

        period_size = t.size
        t = np.roll(t,-int(math.floor(period_size*phase_offset)))

    elif (readDirection.lower() == "backforth"):
        half_t = np.arange(0.,1., step_size*2)
        t = np.append(half_t, half_t[::-1]) * 4

        # TODO: add scalable offset
        #offset_index = np.where(half_t >= offset)[0][0]
        #t = np.resize(np.append(half_t, half_t[::-1]), num_samples + offset_index)
        #t = t[offset_index:]

    else:
        return 0

    return t
