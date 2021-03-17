import numpy as np
import scipy.stats as st
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

def p(x):
    return st.norm.pdf(x, loc=30, scale=10) + st.norm.pdf(x, loc=80, scale=20)

def q(x):
    return st.norm.pdf(x, loc=50, scale=30)

x = np.arange(-50, 151)
M = max(p(x) / q(x)) # p(x) / q(x) <= M <--> p(x) <= M q(x)

def rejection_sampling(iter):
    samples = []
    # TO COMPLETE
    # Use np.random
    for i in range(iter):
        x = np.random.normal(50, 30)
        u = np.random.uniform(0, M*q(x))

        if u <= p(x):
            samples.append(x)

    return np.array(samples)

s = rejection_sampling(iter=100000)

print(M)

fig = plt.figure(figsize=(10,5))
ax = fig.subplots(1,1)
ax.plot(x, p(x))
ax.plot(x, M*q(x))
plt.xlim([-50, 150])


fig = plt.figure(figsize=(10,5))
ax = fig.subplots(1,2)
sns.histplot(s, ax=ax)
plt.xlim([-50, 150]) 


