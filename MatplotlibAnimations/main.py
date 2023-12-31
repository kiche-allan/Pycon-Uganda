import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import random

x_values = []
y_values = []

for _ in range(1000):
    x_values.append(random.randint(0, 100))
    y_values.append(random.randint(0, 100))

    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.scatter(x_values, y_values)
    plt.pause(0.0001)
plt.show()