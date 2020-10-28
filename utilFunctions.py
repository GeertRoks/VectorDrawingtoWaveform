import matplotlib.pyplot as plt
import numpy as np
import math
import pygame
from time import sleep

def plotResults(x_real, x_imag, y_real, y_imag, fs, f, t, duration):
    fig, axes = plt.subplots(3, 1, figsize=(9.5,9.5))

    axes[0].plot(x_real[:int(fs/f)], x_imag[:int(fs/f)])
    axes[0].set_xlim((-1.5,1.5))
    axes[0].set_ylim((-1.5,1.5))
    x0,x1 = axes[0].get_xlim()
    y0,y1 = axes[0].get_ylim()
    axes[0].set_aspect(abs(x1-x0)/abs(y1-y0))
    axes[0].grid(b=True, which='major', color='k', linestyle='--')

    axes[1].plot(t, x_real[:np.size(t)], label="x_real")
    axes[1].plot(t, x_imag[:np.size(t)], label="x_imag")
    for xc in range(1,math.ceil(t[-1])):
        axes[1].axvline(x=xc, color ="red", linestyle='--')

    axes[1].autoscale(tight = True)

    axes[2].plot(np.arange(0,duration,1/fs), y_real, label="y_real")
    axes[2].plot(np.arange(0,duration,1/fs), y_imag, label="y_imag")
    axes[2].set_xlim((0,duration))
    axes[2].set_ylim((-1.,1.))

    plt.tight_layout()
    plt.legend()
    plt.show()
    #return plt

def playSound(sound, fs):
    sound = (sound*32768).astype(np.int16)
    pygame.mixer.pre_init(fs, size=-16, channels=1)
    pygame.mixer.init()
    audio = pygame.sndarray.make_sound(sound)

    audio.play()
    sleep(0.01)
