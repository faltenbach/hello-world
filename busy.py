import numpy
import sys 

fact = float(sys.argv[1]) 
Nbig = 10000000

for i in range(Nbig+1):         
    x = ( float(i) / ( fact * float(Nbig)) )
    y = numpy.arccos(x)

print fact, x , y
