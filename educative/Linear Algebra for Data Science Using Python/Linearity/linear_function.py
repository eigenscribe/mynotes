import numpy as np

def f1(x):
    return 2*x
def f2(x):
    return x**2

#Initializing variables
x1, x2, isf1Linear, isf2Linear = np.random.randn(), np.random.randn(), True, True

for i in range(10000):
    #Generating random scalars for linearity test
    alpha, beta = np.random.randn(), np.random.randn()
    #Verifying additivity and homogeneity for f1
    if f1(alpha*x1+beta*x2) != alpha*f1(x1)+beta*f1(x2):
        isf1Linear = False
    #Verifying additivity and homogeneity for f2
    if f2(alpha*x1+beta*x2) != alpha*f2(x1)+beta*f2(x2):
        isf2Linear = False

print('In 10000 random tries: f1 is ', ['Non Linear', 'Linear'][isf1Linear],' and f2 is ', ['Non Linear', 'Linear'][isf2Linear])
