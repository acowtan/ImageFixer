from scipy import misc      # Import misc
import matplotlib.pyplot as plt
def main():
    #         Get the filename as string
    #fn = str(raw_input("File:"))
    #        Read file it np array
    im = misc.imread("desync1.pgm")
    #Display with grayscale colour map
    print(im)
    plt.imshow(im,cmap=plt.cm.gray)
    #         Show the image
    plt.show()

main()        # Run the progra
