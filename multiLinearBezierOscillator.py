import bezierCurves as bezier
import matplotlib.pyplot as plt
import numpy as np

def multiLinearBezierOscillator(f, fs, duration, readDirection):

    # point up /\
    p_left = -1-1j
    p_middle = 0+1j
    p_right = 1-1j
    points = np.array([p_left, p_middle, p_right])
    num_lines = np.size(points) - 1
    print(num_lines)

    # init parameters
    num_samples = fs * duration
    step_size = f*num_lines/fs # step size: 1/(samples per period) = 1/(fs/f) = f/fs

    #offset = 0.5 # TODO: add scalable offset

    # setup the step waveform t through the bezier curve: choice for forward, backward or back-and-forth
    if (readDirection == "forward" or readDirection == "backward"):
        t = np.arange(0., 1., step_size)
        t = np.resize(t, num_samples)

        # TODO: add scalable offset
        #offset_index = np.where(t >= offset)[0][0]
        #t = np.resize(t, num_samples + offset_index)
        #t = t[offset_index:]

        if (readDirection == "backward"):
            t = np.where(t, 1-t, 1.)

    elif (readDirection == "backforth"):
        half_t = np.arange(0.,1., step_size*2)
        t = np.resize(np.append(half_t, half_t[::-1]), num_samples)

        # TODO: add scalable offset
        #offset_index = np.where(half_t >= offset)[0][0]
        #t = np.resize(np.append(half_t, half_t[::-1]), num_samples + offset_index)
        #t = t[offset_index:]

    else:
        return 0

    # get signal
    x = np.zeros(num_samples, dtype = complex)
    sel_line = 0
    prev_t = 0
    for idx, ti in enumerate(t):
        if ti - prev_t < 0:
            sel_line = (sel_line + 1) % num_lines

        prev_t = ti

        # Write signal with correct points 
        #   if first line, then sel_line == 0, thus points[0] and points[1]
        #   if second line, then sel_line == 1, thus points[1] and points[2]
        x[idx] = bezier.linearBezierComplex(points[sel_line],points[sel_line+1], ti)

    # extract horizontal and vertical movement
    x_real = np.real(x)
    x_imag = np.imag(x)

    # Scale amplitude of signals
    A = 0.8
    y_real = A * x_real
    y_imag = A * x_imag

    # Plot results
    fig, axes = plt.subplots(3, 1)

    plt.subplot(311)
    plt.plot(x_real, x_imag)
    axes[0].set_xlim((0,2))
    axes[0].set_ylim((0,2))
    x0,x1 = axes[0].get_xlim()
    y0,y1 = axes[0].get_ylim()
    axes[0].set_aspect(abs(x1-x0)/abs(y1-y0))
    axes[0].grid(b=True, which='major', color='k', linestyle='--')
    plt.autoscale(tight = True)

    plt.subplot(312)
    plt.plot(t, x_real, label="x_real")
    plt.plot(t, x_imag, label="x_imag")
    plt.autoscale(tight = True)

    plt.subplot(313)
    plt.plot(np.arange(0,num_samples/fs,1/fs), y_real, label="y_real")
    plt.plot(np.arange(0,num_samples/fs,1/fs), y_imag, label="y_imag")
    plt.autoscale(tight = True)

    plt.tight_layout()
    plt.legend()
    plt.show()

    return (y_real, y_imag)

