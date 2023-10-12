import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,1)
y = np.sin(x)

#fig, ax = plt.subplots()
#ax.set_title('')
#ax.yaxis.set_major_formatter('')

np.random.seed(19680801)  # seed the random number generator.
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')

ax.plot()

plt.show()