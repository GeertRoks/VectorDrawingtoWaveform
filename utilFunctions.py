import matplotlib.pyplot as plt
import numpy as np
import math
import pygame
from time import sleep

def plotResults(onePeriod, fullSample, num_lines, fs, f, duration, readDirection, phase_offset=0.0):
    fig, axes = plt.subplots(3, 1, figsize=(9.5,9.5))

    # Bezier figure
    axes[0].plot(np.real(onePeriod[:int(fs/f)]), np.imag(onePeriod[:int(fs/f)]))
    #plot information
    axes[0].set_title('Bezier figure')
    axes[0].set_xlim((-1.5,1.5))
    axes[0].set_ylim((-1.5,1.5))
    axes[0].set_xticks([-1.5,-1,-0.5,0,0.5,1,1.5])
    axes[0].set_yticks([-1.5,-1,-0.5,0,0.5,1,1.5])
    #set aspectratio of plot
    x0,x1 = axes[0].get_xlim()
    y0,y1 = axes[0].get_ylim()
    axes[0].set_aspect(abs(x1-x0)/abs(y1-y0))
    axes[0].grid(b=True, which='major', color='k', linestyle='--')

    # Period plot
    period_t = np.arange(0.,1., f/fs) * num_lines
    #period_t = np.roll(t,int(math.floor(t.size*phase_offset))) # undo phase shift to normalize to 0 on plot
    #plot the data with the normalized t
    axes[1].plot(period_t, np.real(onePeriod), label="x")
    axes[1].plot(period_t, np.imag(onePeriod), label="y")
    #draw segment indicators
    if (readDirection.lower() == 'backforth'):
        for xc in range(1, 2*num_lines +1):
            axes[1].axvline(x=(xc - phase_offset)/2, color="red", linestyle='--')
    else:
        for xc in range(1,num_lines+1):
            axes[1].axvline(x=xc - phase_offset, color="red", linestyle='--')
    #plot information
    axes[1].set_title('One period of the x and y output')
    axes[1].set_xlabel('t')
    axes[1].autoscale(tight = True)

    # Synthesis plot
    axes[2].plot(np.arange(0,duration,1/fs), np.real(fullSample), label="x")
    axes[2].plot(np.arange(0,duration,1/fs), np.imag(fullSample), label="y")
    axes[2].set_xlim((0,duration))
    axes[2].set_ylim((-1.,1.))
    axes[2].set_title('Full duration of generated sample')
    axes[2].set_xlabel('seconds')
    plt.legend()

    plt.tight_layout()
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
            #t = np.where(t, num_lines-t, num_lines)
            t = t[::-1]

        period_size = t.size
        t = np.roll(t,-int(math.floor(period_size*phase_offset)))

    elif (readDirection.lower() == "backforth"):
        half_t = np.arange(0.,1., step_size*2)
        t = np.append(half_t, half_t[::-1])
        t = t * num_lines

        period_size = t.size
        t = np.roll(t,-int(math.floor(period_size*phase_offset)))

    else:
        return 0

    return t
