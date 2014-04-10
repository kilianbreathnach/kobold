import numpy as np
class Halo: 
    def __init__(self): 
        pass

class Galaxies: 
    def __init__(self): 
        pass

def readHalofile(filename='halo_chunk.dat'): 
    '''
    '''
    dir = 'dat/' 
    halodata = np.loadtxt(''.join([dir, filename]))
    halo = Halo()
    columns = ['id', 'Mvir', 'Rvir', 'x', 'y', 'z', 'vx', 'vy', 'vz']
    for col_index, name in enumerate(columns):
        setattr(halo, name, halodata[:, col_index])
    return halo 

def assignGalaxies(halo, galaxy): 
    

if __name__=="__main__": 
    maxhalo = readHalofile('halo_chunk_max.dat')
    print maxhalo.__dict__.keys()
    print maxhalo.Mvir

    maxhalo_galaxies = Halo()
    
