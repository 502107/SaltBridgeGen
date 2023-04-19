# SaltBridgeGen
Generate salt bridge input file (`SB.in`) for cpptraj, and `SB.sh` to concat. the data[^1].

After running `SB.sh`[^2], `SBmat.dat` is created -- a matrix with the % each salt bridge is expressed in the system. This can be plotted in any way using a contour/heatmap plot, but also including a simple R script for a preliminary low-res render of the plot.

Salt-bridges are only considered in a distance > 3.2 Å. To change this to a maximum of 6 Å[^3], edit the CUTOFF flag in `./dat/SB.awk`.

**The atom description is specific to AMBER force fields. Double check that `SB.py` has the same atom names as in the topology used to run the simulations.**

[^1]: Requires python (pkg: pandas, numpy, sys)
[^2]: Requires R
[^3]: See DOI: [10.1021/ja039159c](https://pubs.acs.org/doi/10.1021/ja039159c)
