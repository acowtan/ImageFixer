import matplotlib.pyplot as plt
from scipy import misc
import numpy as np
from numpy import fft
import random as rand

#read in the image and show it pre-algorithm
im= misc.imread("desync4.pgm")
plt.imshow(im, cmap=plt.cm.gray)
plt.show()

#create a copy of the original image and calculate the dimensions of the image
shiftedIm=np.copy(im)
col_len = len(im[:,1])
row_len=len(im[1,:])

#define function which finds the shift between two lines using the relationship between Fourier transforms and cross-correlation
def GetShift (a=list, b=list):
    f1=fft.fft(a)
    f2=fft.fft(b)
    mult= f1*(np.conj(f2))
    #finds the cross-correlation of the lines
    crosscorr=fft.ifft(mult)
    #finds the location of the maximum value (peak) of the cross-correlation
    shift= np.argmax(crosscorr)
    return shift

#main loop, which runs through the rows of the image, starting from the 3rd row
i=2
while i<(col_len-4):

    #find the shifts between the line of interest, the previous 2 lines and the next 4 lines
    shift_a= GetShift(shiftedIm[i-2,:], im[i,:])  
    shift = GetShift(shiftedIm[i-1,:], im[i,:])
    shift_b= GetShift(im[i+1,:], im[i,:])  
    shift_c= GetShift(im[i+2,:], im[i,:]) 
    shift_d= GetShift(im[i+3,:], im[i,:])
    shift_e= GetShift(im[i+4,:], im[i,:])                         
      
      
    #using the results of the checks, set the shift to 0 if a block of similar lines is detected     
    if shift_a<2:
        shift=0
    if shift_b<2:
        shift=0
    if shift_c<2:
        shift=0
    if shift_d<2:
        shift=0           
    if shift_e<2:
        shift=0 
         
    #using the elements of the previous line, replace the noise at the edges of the image
    for j in range(row_len):
        shiftedIm[i,j]=im[i,(j-shift)]
        if j>(row_len-shift):
            shiftedIm[i,j]=shiftedIm[i-1,j]
        if j<shift:
            shiftedIm[i,j]=shiftedIm[i-1,j]

               
        
    i+=1

#show the image after algorithm
plt.imshow(shiftedIm, cmap=plt.cm.gray)
plt.show()
