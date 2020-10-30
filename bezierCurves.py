import numpy as np

# Linear Bezier line
def linearBezier(p0, p1, t):
    pFinal = np.zeros(2)
    pFinal[0] = (1-t) * p0[0] + t*p1[0]
    pFinal[1] = (1-t) * p0[1] + t*p1[1]

    return pFinal

def linearBezierComplex(p0, p1, t):
    pFinal = (1-t) * np.real(p0) + t*np.real(p1) + 1.0j*((1-t) * np.imag(p0) + t*np.imag(p1))
    return pFinal

# Quadratic Bézier curve
def quadraticBezier(p0, p1, p2, t):
    pFinal = np.zeros((t.size,2))
    pFinal[:,0] = (1-t)**2 * p0[0] + 2*(1-t)*t * p1[0] + t*t * p2[0]
    pFinal[:,1] = (1-t)**2 * p0[1] + 2*(1-t)*t * p1[1] + t*t * p2[1]

    return pFinal

def quadraticBezierComplex(p0, p1, p2, t):
    pFinal = (1-t)**2 * np.real(p0) + 2*(1-t)*t * np.real(p1) + t*t * np.real(p2) + 1.0j* ( (1-t)**2 * np.imag(p0) + 2*(1-t)*t * np.imag(p1) + t*t * np.imag(p2) )
    return pFinal
