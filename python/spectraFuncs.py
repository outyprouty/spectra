from matplotlib import pyplot as plt
from numpy import sqrt, exp, log, power, loadtxt


c   =   2.99792458e18    #Ang s^-1
h   =   6.6260755e-14   #Ang^2 kg s^-1
kB  =   1.380658e-3    #Ang^2 kg s^-2 K^-1

def getIndex(wLs, spacing, desiredWl):
    
    index = (desiredWl - wLs[0])/spacing
    
    return int(index)

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
    
def plotSpectrumOutput(spectrumOutputFile, Teff, logg, metalicity, imageName):
    data = loadtxt(spectrumOutputFile).T
    waveLen = data[0]
    relaInt = data[1]
    
    plt.plot(waveLen, relaInt)
    plt.title("%s; Teff=%d logg=%0.2f [M/H]=%0.2f" %(spectrumOutputFile, Teff, logg, metalicity))
    plt.xlabel('Wavelength [Ang]')
    plt.ylabel('Relative Intensity')
    plt.grid(True)
    
    plt.savefig("%s.png"%imageName)
    
    plt.close()

def plotSpectrumOutput_waveLen(spectrumOutputFile, Teff, logg, metalicity, waveLimits, spacing, imageName):
    data = loadtxt(spectrumOutputFile).T
    waveLen = data[0]
    relaInt = data[1]

    wL1 = getIndex(waveLen, spacing, waveLimits[0]) 
    wL2 = getIndex(waveLen, spacing, waveLimits[1])

    plt.plot(waveLen[wL1: wL2], relaInt[wL1: wL2])
    plt.title("%s; Teff=%d logg=%0.2f [M/H]=%0.2f" %(spectrumOutputFile, Teff, logg, metalicity))
    plt.xlabel('Wavelength [Ang]')
    plt.ylabel('Relative Intensity')
    plt.grid(True)

    plt.savefig("%s.png"%imageName)

    plt.close()
    
def plotSpectrumOverPlanck(spectrumOutputFile, Teff, logg, metalicity, waveLimits, spacing, imageName):
    data = loadtxt(spectrumOutputFile).T
    waveLen = data[0]
    relaInt = data[1]

    wL1 = getIndex(waveLen, spacing, waveLimits[0])
    wL2 = getIndex(waveLen, spacing, waveLimits[1])
    
    planck = planckFunction(waveLen[wL1: wL2], Teff)

    plt.plot(waveLen[wL1: wL2], relaInt[wL1: wL2] * planck, label='SPECTRUM')
    plt.plot(waveLen[wL1: wL2], planck, 'r--', label='Planck')
    
    plt.title("%s w/ Planck Function\n Teff=%d logg=%0.2f [M/H]=%0.2f" %(spectrumOutputFile, Teff, logg, metalicity))
    plt.xlabel(r'Wavelength [$\AA$]')
    plt.ylabel(r'Intensity [$Wm^{-2}\AA^{-1}sr^{-1}$]')
    plt.grid(True)
    plt.legend(loc=0)

    plt.savefig("%s_pf.png"%imageName)

    plt.close() 

