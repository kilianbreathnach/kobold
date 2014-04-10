import numpy as np
import CosmologicalDistance as cosmodist

class Halo: 
    def __init__(self): 
        pass

    def xyz2radecz(self): 
        '''
        Convert x, y, z positions of halos into 
        RA, Dec, and Redshift values
        ''' 
        cosmo = cosmodist.CosmologicalDistance() 
        print cosmo.__dict__.keys()
        # compute the Line-of-Sight Comoving Distance  
        los_comovdist = np.sqrt(self.x**2+self.y**2+self.z**2)
        # convert to spherical coordinates
        dradeg = 180.0/np.pi
        phi = dradeg*np.arccos(self.z/los_comovdist)
        theta = dradeg*np.arctan(self.y/self.x)
        # now to RA, Dec, and Redshift
        self.ra = theta
        self.dec = np.pi/2.0 - phi
        self.redshift = np.array([cosmo.inverse_comoving_distance(los_comovdist[i]) \
                for i in range(len(los_comovdist))])

class Galaxies: 
    def __init__(self): 
        pass
    def assignGalaxies(self, halo): 
        attributes = ['ra', 'dec', 'redshift']
        for attr in attributes: 
            halo_attr = getattr(halo, attr)
            if (attr == 'redshift'): 
                halo_attr = scatterRedshift(halo_attr)
                setattr(self, attr, halo_attr)
            else: 
                setattr(self, attr, halo_attr)

def readHalofile(filename='halo_chunk.dat'): 
    '''
    '''
    dir = 'dat/' 
    halodata = np.loadtxt(''.join([dir, filename]))
    halo = Halo()
    columns = ['id', 'Mvir', 'Rvir', 'x', 'y', 'z', 'vx', 'vy', 'vz']
    cosmo = cosmodist.CosmologicalDistance()
    for col_index, name in enumerate(columns):
        if name=='z': 
            # shift galaxies in z-direction to comoving distance 
            # corresponding to z ~ 0.1
            setattr(halo, name, halodata[:, col_index]+cosmo.comoving_distance(0.1))
        else: 
            setattr(halo, name, halodata[:, col_index])
    return halo 


def scatterRedshift(redshift): 
    sigma_z = (1.0+redshift)*0.005  # PRIMUS error model
    dz = sigma_z*np.random.randn(len(redshift))
    print redshift
    print dz
    return redshift+dz

if __name__=="__main__": 
    maxhalo = readHalofile('halo_chunk_max.dat')
    maxhalo.xyz2radecz()

    maxhalo_galaxies = Galaxies()
    maxhalo_galaxies.assignGalaxies(maxhalo)
    print maxhalo_galaxies.ra
    print maxhalo_galaxies.dec
