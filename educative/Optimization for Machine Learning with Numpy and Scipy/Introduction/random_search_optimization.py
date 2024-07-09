import numpy as np
import matplotlib.pyplot as plt

# objective function
def objective(x):
 return (x+2)*(x-5) + 15
 
a, b = -10.0, 10.0 # range of random points to be sampled
N = 1000

datapoints = a + np.random.rand(N) * (b-a) # generate 100 random points between [a,b]

outputs = objective(datapoints) # evaluate objective on random data points
index = np.argmin(outputs)

# summarize best solution
print('Best: f(%.5f) = %.5f' % (datapoints[index], outputs[index]))

# plot the curve for graphic visualization
plt.figure(figsize=(10,10))
plt.rcParams.update({'font.size': 22})
x = np.arange(-10, 10, 0.1)
plt.plot(x, objective(x), linewidth=2)

# plot the random datapoints sample
plt.axvline(x=datapoints[index], ls='--', color='red', label='optimum')
plt.axhline(y=0, ls='-', color='black')
plt.axvline(x=0, ls='-', color='black')
plt.legend()
plt.savefig('./output/plot.png')
