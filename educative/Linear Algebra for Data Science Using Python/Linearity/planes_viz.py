import plotly.graph_objects as go
import numpy as np

# Function to generate 3 planes passing through origin in the given x-axis and y-axis range
def func(x, y):
    a, b = 10, -5, 
    z1 = a*x + b*y
    a, b = -1, 10, 
    z2 = a*x + b*y
    a, b = -10, -5, 
    z3 = a*x + b*y
    return z1,z2,z3 

# Defining range of x-axis and y-axis
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

# Creating a grid and the planes
X, Y = np.meshgrid(x, y)
z1,z2,z3 = func(X, Y)

# Plotting the planes
fig = go.Figure(data=[
    go.Surface(x=X,y=Y,z=z1,showscale=False,colorscale='bugn'),
    go.Surface(x=X,y=Y,z=z2,showscale=False,colorscale='oxy'),
    go.Surface(x=X,y=Y,z=z3,showscale=False,colorscale='deep')

])
fig.show()
