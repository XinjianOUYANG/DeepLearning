from scipy.stats import beta
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)
a, b = 1, 1
mean, var, skew, kurt = beta.stats(a, b, moments='mvsk')

x = np.linspace(beta.ppf(0.01, a, b),
                beta.ppf(0.99, a, b), 100)
ax.plot(x, beta.pdf(x, a, b),
       'r-', lw=5, alpha=0.6, label='beta pdf')

plt.show()