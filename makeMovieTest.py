# import visit_utils, we will use it to help encode our movie
from visit_utils import *
DeleteAllPlots()

var = "z_velocity"
varout = "z_vorticity"

OpenDatabase("localhost:./box.nek5000", 0)

AddPlot("Pseudocolor",var)
PseudocolorAtts = PseudocolorAttributes()
PseudocolorAtts.minFlag = 1 # Min and Max contour level
PseudocolorAtts.min = -0.67
PseudocolorAtts.maxFlag = 1
PseudocolorAtts.max = 0.67 
PseudocolorAtts.opacityType = PseudocolorAtts.Constant  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
PseudocolorAtts.opacityVariable = ""
PseudocolorAtts.opacity = 0.7
PseudocolorAtts.opacityVarMin = 0
PseudocolorAtts.opacityVarMax = 1
PseudocolorAtts.opacityVarMinFlag = 0
PseudocolorAtts.opacityVarMaxFlag = 0
SetPlotOptions(PseudocolorAtts)

AnnotationAtts = AnnotationAttributes()
AnnotationAtts.axes3D.visible = 0
AnnotationAtts.axes3D.triadFlag = 1
AnnotationAtts.axes3D.bboxFlag = 1
SetAnnotationAttributes(AnnotationAtts)


AddOperator("Isosurface",1)
IsosurfaceAtts = IsosurfaceAttributes()
IsosurfaceAtts.contourNLevels = 2
IsosurfaceAtts.contourValue = ()
IsosurfaceAtts.contourPercent = ()
IsosurfaceAtts.contourMethod = IsosurfaceAtts.Level  # Level, Value, Percent
IsosurfaceAtts.minFlag = 0
IsosurfaceAtts.min = -0.67 
IsosurfaceAtts.maxFlag = 0
IsosurfaceAtts.max = 0.67
IsosurfaceAtts.scaling = IsosurfaceAtts.Linear  # Linear, Log
IsosurfaceAtts.variable = "default"
SetOperatorOptions(IsosurfaceAtts, 1)

DrawPlots()
 
# Set a better view
# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.5, 0.25, 0.80)
View3DAtts.focus = (6.28, 0., 2.094)
View3DAtts.viewUp = (-0.15, 0.95, -0.2)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 6
View3DAtts.nearPlane = -10
View3DAtts.farPlane = 10
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.8 
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (6.28, 0, 2.094)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state
