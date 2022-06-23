# nonzero() - This function is used to determine the position of the elements which are non zero. \
                # This function returns an array that contains the indexes of the element of the array \
                    # Which are not equal to zero
            # synax - numpy.nonzero(a)


from numpy import *

a = array([100,0,200,300,400,0])
c = nonzero(a)
print(c)

