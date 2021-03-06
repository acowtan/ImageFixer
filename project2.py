############################################
#THIS CHECKS THE SHIFTS OF 3 DIFFERENT ROWS#
############################################

from scipy import misc      # Import misc
import matplotlib.pyplot as plt
import numpy as np
from numpy import fft
from numpy import *

#read in the file to be synced
im = misc.imread("desync2.pgm")

plt.imshow(im, cmap=plt.cm.gray)
plt.show()

#print the length of a column so we know how long the next loop is running through
col_len = len(im[:,1])
print(str(col_len))
row_len = len(im[1,:])

shift_list = []
i = 1
#cross correlate each line with the next one
while i < col_len-2:
    a = im[i-1,:]
    b = im[i,:]
    c = im[i+1,:]


    A = fft.fft(a)
    B = fft.fft(b)
    C = fft.fft(c)


    f = np.zeros(len(A), dtype=np.complex)
    f = B*np.conj(A)
    g = np.zeros(len(A), dtype=np.complex)
    g = C*np.conj(B)


    #find inverse fourier transform to get the cross correlation
    
    corr1 = fft.ifft(f)
    corr2 = fft.ifft(g)


    #use peak of cross correlation to shift the next line in line with the current one
    #first line of image is assumed to be correct
    shift1 = np.argmax(corr1)
    shift2 = np.argmax(corr2)


    if shift1 == 0 or shift2 == 0:
        shift == 0
    if shift1 != 0 and shift2 != 0:
        shift = shift1
    
    shift_list.append(shift)
    for j in range(row_len):
        if j < row_len-shift1:
            im[i,j] = im[i, (j+shift1)]
    i+=1
    
    
#print(shift_list)
#print(f)
#print(corr)

plt.imshow(im, cmap=plt.cm.gray)
plt.show()

