import numpy as np
class Halo: 
    def __init__(self): 
        pass

    def xyz_to_RADECZ(self): 
        '''
        Convert x, y, x positions of halos into 
        RA, Dec, and Redshift values
        '''

        self.ra = 
        self.dec = 
        self.z = 

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
    halo_x = getattr(halo, 'x')  
    halo_y = getattr(halo, 'y')  
    halo_z = getattr(halo, 'z')  

if __name__=="__main__": 
    maxhalo = readHalofile('halo_chunk_max.dat')
    maxhalo.xyz_to_RADECZ()

    maxhalo_galaxies = Halo()
    
