#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()
print(iris.data.shape, iris.target.shape)
iris.data = iris.data.reshape((150, 2, 2))
print(iris.data.shape)

for i in range(10):
    print(i)

persons = [name for name in range(10)]