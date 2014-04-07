import numpy as np


# # Extract relevant columns from halo catalogue:
# # (id, Mvir, Rvir, X, Y, Z, Vx, Vy, Vz)
# halo_cols = np.loadtxt("simul_dat/hlist_0.91000.list",
#                        usecols=(1, 10, 11, 17, 18, 19, 20, 21, 22))
#
# np.savetxt("simul_dat/halo_cols_abbr.dat", halo_cols)

# Get columns from abbreviated data
halo_cols = np.loadtxt("simul_dat/halo_cols_abbr.dat")

# # Now slice in (X, Y) a 10 Mpc square to try find a good place
# # to sample a cylinder. Just take a block 10 Mpc in from corner.
# sq_bool = (halo_cols[:, 3] > 110.0) * (halo_cols[:, 3] < 120.0) * \
#           (halo_cols[:, 4] > 110.0) * (halo_cols[:, 4] < 120.0)
# sq_inds = np.where(sq_bool == True)
#
# halo_cols = halo_cols[sq_inds]
#
# # Now get a 5 Mpc deep box in the z-direction for cylinder depth
# cyl_bool = (halo_cols[:, 5] > 497.5) * (halo_cols[:, 5] < 502.5)
# cyl_inds = np.where(cyl_bool == True)
#
# halo_cols = halo_cols[cyl_inds]

# Run code to find largest halo
max_mass = np.argmax(halo_cols[:, 1])
max_loc = halo_cols[max_mass, 3:6]

sq_bool = (halo_cols[:, 3] > max_loc[0] - 5.0) * \
          (halo_cols[:, 3] < max_loc[0] + 5.0) * \
          (halo_cols[:, 4] > max_loc[1] - 5.0) * \
          (halo_cols[:, 4] < max_loc[1] + 5.0)
sq_inds = np.where(sq_bool == True)

halo_cols = halo_cols[sq_inds]

cyl_bool = (halo_cols[:, 5] > max_loc[2] - 2.5) * \
           (halo_cols[:, 5] < max_loc[2] + 2.5)
cyl_inds = np.where(cyl_bool == True)

halo_cols = halo_cols[cyl_inds]


# Save result to a smaller text file
np.savetxt("dat/halo_chunk_max.dat", halo_cols)

halo_cols = np.loadtxt("dat/halo_chunk_max.dat")

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
    circles.append(plt.Circle((halo[3], halo[4]), 0.001 * halo[2],
                              color='b', alpha=0.25))

fig = plt.figure()
ax = fig.add_subplot(111)
#ax.set_xlim([100., 130.])
#ax.set_ylim([100., 130.])

ax.set_xlim([max_loc[0] - 15.0, max_loc[0] + 15.0])
ax.set_ylim([max_loc[1] - 15.0, max_loc[1] + 15.0])

for crc in circles:
    print crc
    ax.add_artist(crc)

fig.savefig("plots/plotcircles_max.png")
