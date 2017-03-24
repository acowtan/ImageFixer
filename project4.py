from scipy import misc      # Import misc
import matplotlib.pyplot as plt
import numpy as np
from numpy import fft

#read in the file to be synced
im = misc.imread("desync2.pgm")
im2 = im

plt.imshow(im, cmap=plt.cm.gray)
plt.show()

#print the length of a column so we know how long the next loop is running through
col_len = len(im[:,1])
print(str(col_len))
row_len = len(im[1,:])

shift_list = []
#cross correlate each line with the next one
for i in range(col_len-3):
    a = im2[i,:]
    b = im2[i+1,:]
    c = im2[i+2, :]
    d = im2[i+3, :]

    A = fft.fft(a)
    B = fft.fft(b)
    C = fft.fft(c)
    D = fft.fft(d)

    f = np.zeros(len(A), dtype=np.complex)
    f = B*np.conj(A)
    g = C*np.conj(A)
    h = D*np.conj(A)

    #find inverse fourier transform to get the cross correlation
    
    corr1 = fft.ifft(f)
    corr2 = fft.ifft(g)
    corr3 = fft.ifft(h)

    #use peak of cross correlation to shift the next line in line with the current one
    #first line of image is assumed to be correct
    shift1 = np.argmax(corr1)
    shift2 = np.argmax(corr2)
    shift3 = np.argmax(corr3)

    shift = (shift1+shift2+shift3)/3

    shift_list.append(shift)
    for j in range(row_len):
        if j < row_len-shift:
            im2[i+3,j] = im2[i+3, (j-(row_len-shift))]
    #shift_list.append(shift)
    
#print(len(shift_list))
#print(shift_list)
#print(f)
#print(corr)

plt.imshow(im2, cmap=plt.cm.gray)
plt.show()

