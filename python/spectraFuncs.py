"""
With standard 'pyplotting' module created for pi_hoban users.
"""

from matplotlib import pyplot as plt
from numpy import sqrt, exp, log, power, loadtxt, argmax, pi


c       =   2.99792458
cPow    =   18    #ang s^-1
h       =   6.6260755
hPow    =   -27   #erg s
kB      =   1.380658
kBPow   =   -16    #erg K^-1

def getIndex(wLs, desiredWl):
    spacing = wLs[1] - wLs[0]
    
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
        Function on. [cm, 1e-2m]
    Teff (int or float): Value of effective temperature. [Kelvin]

    Returns:
    Float or array of Flots with values of Planck Function. 
    Same shape as wl. [erg s^-1 sr^-1 cm^-2 cm^-1]

    Notes:
    Used https://www.spectralcalc.com/blackbody_calculator/blackbody.php
         to verify results
    """

    p = 1.19106e+27
    
    p1 = power(wl,5.0)*(exp(1.43879e+08/(wl*Teff)) -1.0)

    return p/p1
    
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

def plotSpectrumOutput_waveLen(spectrumOutputFile, Teff, logg, metalicity, waveLimits, imageName):
    data = loadtxt(spectrumOutputFile).T
    waveLen = data[0]
    relaInt = data[1]

    wL1 = getIndex(waveLen, waveLimits[0]) 
    wL2 = getIndex(waveLen, waveLimits[1])

    plt.plot(waveLen[wL1: wL2], relaInt[wL1: wL2])
    plt.title("%s; Teff=%d logg=%0.2f [M/H]=%0.2f" %(spectrumOutputFile, Teff, logg, metalicity))
    plt.xlabel('Wavelength [Ang]')
    plt.ylabel('Relative Intensity')
    plt.grid(True)

    plt.savefig("%s.png"%imageName)

    plt.close()
    
def plotSpectrumOverPlanck(spectrumOutputFile, Teff, logg, metalicity, waveLimits, imageName):
    data = loadtxt(spectrumOutputFile).T
    waveLen = data[0]
    inten = data[1]
    
    wL1 = getIndex(waveLen, waveLimits[0])
    wL2 = getIndex(waveLen, waveLimits[1])

    wlRange = waveLimits[1] - waveLimits[0]

    waveLen = waveLen[wL1: wL2]
    dWl = waveLen[2] - waveLen[1]
    
    planck = planckFunction(waveLen, Teff)*1e10
    inten = inten[wL1: wL2]
    print("Planck Function at %0.1g Ang: %0.2g erg/cm^2/Ang/sr"%(7000, planckFunction(7000,Teff)))

    plt.plot(waveLen, inten, label='SPECTRUM')
    plt.plot(waveLen, planck, 'r--', label='Planck')
    
    plt.title("%s w/ Planck Function\n Teff=%d logg=%0.2f [M/H]=%0.2f" %(spectrumOutputFile, Teff, logg, metalicity))
    plt.xlabel(r'Wavelength [$\AA$]')
    plt.ylabel(r'Intensity [$erg cm^{-2}\AA^{-1}sr^{-1}$]')
    plt.xlim([waveLen[0]-wlRange*0.01, waveLen[-1]+wlRange*0.01])
    plt.ylim([max(inten)*-0.01, max(inten)*1.1])
    plt.grid(True)
    plt.legend(loc=0)
    plt.show()
#    plt.savefig("%s_pf.png"%imageName)

 #   plt.close() 

def plotSpectrumOverSpectrumContinuum(spectrumOutputFile, spectrumContFile, Teff, logg, metalicity, waveLimits, imageName):
    data = loadtxt(spectrumOutputFile).T
    waveLen = data[0]
    inten = data[1]
    
    data = loadtxt(spectrumContFile).T
    cont = data[1]

    wL1 = getIndex(waveLen, waveLimits[0])
    wL2 = getIndex(waveLen, waveLimits[1])

    wlRange = waveLimits[1] - waveLimits[0]

    waveLen = waveLen[wL1: wL2]
    dWl = waveLen[2] - waveLen[1]
    
    inten = inten[wL1: wL2]*power(pi,-1)
    cont = cont[wL1: wL2]
    planck = planckFunction(waveLen, Teff)
    print("dWl: ", dWl)
    print("Planck Function at %0.1g Ang: %0.2g erg/cm^2/Ang/sr"%(7000, planckFunction(7000,Teff)), planck[getIndex(waveLen,7000)])
    print("Continuum at %0.1g Ang: %0.2g erg/cm^2/Ang/sr"%(7000, cont[getIndex(waveLen,7000)]))


    plt.plot(waveLen, inten, label='SPECTRUM')
    plt.plot(waveLen, cont, 'k-.', label='SPECTRUM Cont')
    plt.plot(waveLen, planck, 'r--', label='Planck')
    
    plt.title("%s w/ Cont & Planck Function\n Teff=%d logg=%0.2f [M/H]=%0.2f" %(spectrumOutputFile, Teff, logg, metalicity))
    plt.xlabel(r'Wavelength [$\AA$]')
    plt.ylabel(r'Intensity [$erg cm^{-2}\AA^{-1}sr^{-1}$]')
    plt.xlim([waveLen[0]-wlRange*0.01, waveLen[-1]+wlRange*0.01])
    plt.ylim([max(inten)*-0.01, max(inten)*1.1])
    plt.grid(True)
    plt.legend(loc=0)
    plt.show(block=True)
#    plt.savefig("%s_pf.png"%imageName)

 #   plt.close() 

if __name__ == "__main__":
    print("p = %0.5g"%(2*h*c*c*power(10,hPow+cPow+cPow)))
    print("p1= %0.5g"%(h*c/kB * power(10,hPow+cPow-kBPow)))
