from spectraFuncs import *
from numpy import linspace

#plotSpectrumOutput( "vega_full.spc", 9400, 3.90, -0.50, "vega"  )
#plotSpectrumOutput_waveLen("vega_full.spc", 9400, 3.90, -0.50, [8000.0, 8006.8], 1.0, "vega_NaI")

"""
def g(x, m, b):
    return m*x + b

x = linspace(0,10)

plotFunction([x,2,5], g, ['x','g'], 'Test of Linear Function, g', 'testImg')

#Start at 300 [Ang] and go to 15 000 [Ang].
#  What visible colors are represented here?
wl = linspace(300,15000,1000)

plotFunction([wl, 5800], planckFunction, ['Wavelength [Ang]', 'Specific Int [We-10 sr^-1 m^-2 Ang^-1] '], 'Planck Function for Sun', 'planckTest')

print("Here is the documentation for the planckFunction:\n" + planckFunction.__doc__)

print("The value for the speed of light is %g Angstrom per second."%c)

"""
from sys import argv
#plotSpectrumOverPlanck(argv[1], int(argv[2]), 3.90, -0.50, [3000,10000], 'test')
plotSpectrumOverSpectrumContinuum(argv[1],argv[2], int(argv[3]), 3.90, -0.50, [3000,10000], 'test')
