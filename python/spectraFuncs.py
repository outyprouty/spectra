"""
With standard 'pyplotting' module created for pi_hoban users.
"""

from matplotlib import pyplot as plt
from numpy import sqrt, exp, log, power


c   =   2.99792458e18    #Ang s^-1
h   =   6.6260755e-14   #Ang^2 kg s^-1
kB  =   1.380658e-3    #Ang^2 kg s^-2 K^-1


def plotFunction(args, f, labels, title, imageName):
    """Creates PNG file of arbitrary function.

    Parameters:
    args (list): Domain and arguments of function f
    f (python func): float-valued function with support on args
    labels (2x1 list of strings): Labels for x and f, respectively
    title (string): Title for plot
    imageName (string): file name (without .png extension)

    Returns:
    None
    """

    x = args[0]
    xPad = (x[-1] - x[0])*0.01

    
    plt.plot( x, f(*args) )
    plt.xlim( [ x[0]-xPad, x[-1]+xPad ] )
    plt.grid(True)

    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.title(title)

    plt.savefig(imageName+".png")


def planckFunction(wl, Teff):
    """Calculate value of Planck Function. Units below.
    
    Parameters:
    wl (list or array): Values of wavelength to calculate Planck
        Function on. [Angstrom, 1e-10m]
    Teff (int or float): Value of effective temperature. [Kelvin]

    Returns:
    Float or array of Flots with values of Planck Function. 
    Same shape as wl. [We-10 sr^-1 m^-2 Ang^-1]

    Notes:
    Used https://www.spectralcalc.com/blackbody_calculator/blackbody.php
         to verify results
    """

    scalar      = 2 * h * c * c / power(wl, 5.0)

    expArgs     = h*c/(kB*Teff*wl)

    partition   = power( exp(expArgs) - 1.0 , -1)

    return scalar * partition
    
def plotSpectrumOutput(spectrumOutputFile, Teff, metalicity, logg, imageName):
    pass

def plotSpectrumOverPlanck(spectrumOutputFile, Teff, metalicity, logg, imageName):
    pass

