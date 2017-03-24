import matplotlib.pyplot as plt
from scipy import misc
import numpy as np
from numpy import fft
import random as rand
im= misc.imread("desync2.pgm")

plt.imshow(im, cmap=plt.cm.gray)
plt.show()

shiftedIm=np.copy(im)

col_len = len(im[:,1])
row_len=len(im[1,:])

#define function which finds the shift between two lines using the fourier transforms relation to cross-correlation

def GetShift (a=list, b=list):
    f1=fft.fft(a)
    f2=fft.fft(b)
    vect= f1*(np.conj(f2))
    corr=fft.ifft(vect)
    shift= np.argmax(corr)
    return shift

#main loop, which runs through the rows of the image
i=2
while i<(col_len-4):

    #find the shifts between the line of interest, the 2 previous and the 4 next
    shift0= GetShift(shiftedIm[i-2,:], im[i,:])  
    shift = GetShift(shiftedIm[i-1,:], im[i,:])
    shift2= GetShift(im[i+1,:], im[i,:])  
    shift3= GetShift(im[i+2,:], im[i,:]) 
    shift4= GetShift(im[i+3,:], im[i,:])
    shift5= GetShift(im[i+4,:], im[i,:])                         
      
      
         
    if shift0<2:
        shift=0
        
    elif shift2<2:
        shift=0
        
    elif shift3<2:
        shift=0
        
    elif shift4<2:
        shift=0
           
    elif shift5<2:
        shift=0 
         
    
    for j in range(row_len):
        shiftedIm[i,j]=im[i,(j-shift)]
        if j>(row_len-shift):
            #x = rand.random()
            #if x >= 0.5:
            M=shiftedIm[i-1,j]
            #if x < 0.5:
            N = im[i-1, j]
            shiftedIm[i,j] = 0.5*(M+N)
        elif j<shift:
            #x = rand.random()
            #if x >= 0.5:
            M = shiftedIm[i-1,j]
            N = im[i-1, j]
            #if x < 0.5:
            shiftedIm[i,j]=0.5*(M+N)

               
        
    i+=1

plt.imshow(shiftedIm, cmap=plt.cm.gray)
plt.show()
