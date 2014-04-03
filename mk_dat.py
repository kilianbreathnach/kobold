import numpy as np


# Extract relevant columns from halo catalogue:
# (id, Mvir, Rvir, X, Y, Z, Vx, Vy, Vz)
halo_cols = np.loadtxt("dat/hlist_0.91000.list",
                       usecols=(1, 10, 11, 17, 18, 19, 20, 21, 22))

# Now slice in (X, Y) a 10 Mpc square to try find a good place
# to sample a cylinder. Just take a block 10 Mpc in from corner.
sq_bool = (halo_cols[:, 3] > 10.0) * (halo_cols[:, 3] < 20.0) * \
          (halo_cols[:, 4] > 10.0) * (halo_cols[:, 4] < 20.0)
sq_inds = np.where(sq_bool == True)

halo_cols = halo_cols[sq_inds]

# Now get a 5 Mpc deep box in the z-direction for cylinder depth
cyl_bool = (halo_cols[:, 5] > 497.5) * (halo_cols[:, 5] < 502.5)
cyl_inds = np.where(cyl_bool == True)

halo_cols = halo_cols[cyl_inds]

# Save result to a smaller text file
np.savetxt("halo_chunk.dat", halo_cols)

# Let's visualise the halos in virial radius as seen along positive
# direction to determine where a good cylinder sample would be

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
rc('text', usetex=True)


circles = []

for halo in halo_cols:
    circles.append(plt.Circle((halo[3], halo[4]), halo[2],
                              color='b', alpha=0.25))

fig = plt.figure()
ax = fig.add_subplot(111)

for crc in circles:
    ax.add_artist(crc)

fig.savefig("plotcircles.pdf")

