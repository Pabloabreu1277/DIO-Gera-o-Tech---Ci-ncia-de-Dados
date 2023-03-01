import matplotlib

from sklearn.datasets import make_regression
x, y = make_regression(n_samples=400, n_features=1, noise=50)
import matplotlib.pyplot as plt

plt.scatter(x,y)
plt.show()