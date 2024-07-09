import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0., 5., 0.2)
plt.plot(x, x**2, 'bs', x, x**3, 'g^')
plt.xlabel('x');plt.ylabel('f(x)')
plt.legend(['x^2', 'x^3'], loc='upper left')
