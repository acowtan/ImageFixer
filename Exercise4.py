import numpy as np
from numpy import fft
import matplotlib.pyplot as plt

fig = plt.figure()

samples = 400
length = 4
increments = np.arange(samples)

x_data = increments*length/samples
height = 2.0
#create discrete charge density function
def p(X, h=height):
    if X < 1:
        return 0.0
    if 1 <= X < 2:
        return h
    if 2 <= X < 3:
        return -1*h
    if 3 <= X:
        return 0.0

density = np.zeros(samples)
for i in range(samples):
    density[i] = p(x_data[i])

fig.add_subplot(211)
plt.plot(x_data, density, drawstyle='steps-mid')
plt.title('X domain of charge density')

#--------------------------------

#preform fft
densityF = fft.fft(density)

fig.add_subplot(212)
plt.plot(increments, densityF.real, increments, densityF.imag, drawstyle = 'steps-mid')
plt.title('Wavenumber domain of charge density')

plt.show()

#---------------------------------

function = np.zeros(samples)

###WHAT DO WE DO ABOUT THE n=0 TERM?###
for n in range(1, samples):
    
    function[n] = densityF[n]*(length/2)/(np.pi*n*complex(0.0, 1.0))

E_data = fft.ifft(function)
