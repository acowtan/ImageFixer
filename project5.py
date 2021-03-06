from scipy import misc      # Import misc
import matplotlib.pyplot as plt
import numpy as np
from numpy import fft

#read in the file to be synced
im = misc.imread("desync4.pgm")
im2 = im

plt.imshow(im, cmap=plt.cm.gray)
plt.show()

#print the length of a column so we know how long the next loop is running through
col_len = len(im[:,1])
print(str(col_len))
row_len = len(im[1,:])

shift_list = []
#cross correlate each line with the next one
for k in range(col_len-1):
    i = col_len-1-k
    a = im2[i,:]
    b = im2[i-1,:]
    A = fft.fft(im2[i,:])
    B = fft.fft(im2[i-1,:])
    f = np.zeros(len(A), dtype=np.complex)
    f = B*np.conj(A)

    #find inverse fourier transform to get the cross correlation
    
    corr = fft.ifft(f)

    #use peak of cross correlation to shift the next line in line with the current one
    #first line of image is assumed to be correct
    shift = np.argmax(corr)

    shift_list.append(shift)
    for j in range(row_len):
        if j < row_len-shift:
            im2[i-1,j] = im2[i-1, (j-(row_len-shift))]
    #shift_list.append(shift)
    
#print(len(shift_list))
#print(shift_list)
#print(f)
#print(corr)

plt.imshow(im2, cmap=plt.cm.gray)
plt.show()

