import numpy as np
import matplotlib.pyplot as plt


def get_rect(t):
    s = 1
    r = 1
    sgn = np.sign
    cos = np.cos(t)
    sin = np.sin(t)
    sin2tsq = np.sin(2*t) ** 2

    wtf = np.sqrt(1 - (np.sqrt(1 - s**2*sin2tsq)))

    x = ((r * sgn(cos)) / (s*np.sqrt(2)*abs(sin))) * wtf
    y = ((r * sgn(sin)) / (s*np.sqrt(2)*abs(cos))) * wtf

    return (x,y)
    
t = np.arange(0.0, 2*np.pi, 0.01)

plt.scatter(*get_rect(t))
plt.show()
