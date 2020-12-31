from spectraFuncs import plotFunction

def g(x, m, b):
    return m*x + b

from numpy import linspace

x = linspace(0,10)

plotFunction([x,2,2], g, ['x','g'], 'test', 'testImg')

from spectraFuncs import planckFunction

wl = linspace(300,15000,1000)

plotFunction([wl, 5000], planckFunction, ['Wavelength [Ang]', 'Specific Int [We-10 sr^-1 m^-2 Ang^-1] '], 'Planck Func', 'planckTest')
