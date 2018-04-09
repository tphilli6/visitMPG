# import visit_utils, we will use it to help encode our movie
from visit_utils import *
DeleteAllPlots()

MPGPath="makeMPGlib/"

#Variables specific to Nek5000
#var = "x_velocity"
#varout = "x_velocity"
#minval=0.0
#maxval=26.0
#ncontour=4
#
#var = "y_velocity"
#varout = "y_velocity"
#minval=-4.0
#maxval=4.0
#
#var = "z_velocity"
#varout = "z_velocity"
#minval=-4.0
#maxval=4.0

#OpenDatabase("localhost:./box.nek5000", 0)

var = "pressure"
varout = "Qinvariant"
minval=1e-6
maxval=0.01
ncontour=4

OpenDatabase("localhost:./vrtbox.nek5000", 0)


# Set up the axis for 3d contour plot
# Copy format from library and keep locally to modify between different plot styles
execfile("visitSetupPlot.py")
PseudocolorAtts.scaling=PseudocolorAtts.Log
SetPlotOptions(PseudocolorAtts)

IsosurfaceAtts.scaling=IsosurfaceAtts.Log
SetOperatorOptions(IsosurfaceAtts, 1)

execfile("visitSetupAxis.py")

# Convert plot to png files and store in ./png/(varout)_*.png
#execfile(MPGPath+"makeMoviePNG.py") 

#exit()

