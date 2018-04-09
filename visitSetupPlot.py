
AddPlot("Pseudocolor",var)
PseudocolorAtts = PseudocolorAttributes()
PseudocolorAtts.scaling = PseudocolorAtts.Linear
PseudocolorAtts.minFlag = 1 # Min and Max contour level
PseudocolorAtts.min = minval
PseudocolorAtts.maxFlag = 1
PseudocolorAtts.max = maxval
PseudocolorAtts.opacityType = PseudocolorAtts.Constant  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
PseudocolorAtts.opacityVariable = ""
PseudocolorAtts.opacity = 0.5
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
IsosurfaceAtts.contourNLevels = ncontour
IsosurfaceAtts.contourValue = ()
IsosurfaceAtts.contourPercent = ()
IsosurfaceAtts.contourMethod = IsosurfaceAtts.Level  # Level, Value, Percent
IsosurfaceAtts.minFlag = 1
IsosurfaceAtts.min = minval
IsosurfaceAtts.maxFlag = 1
IsosurfaceAtts.max = maxval
IsosurfaceAtts.scaling = IsosurfaceAtts.Linear  # Linear, Log
IsosurfaceAtts.variable = "default"
SetOperatorOptions(IsosurfaceAtts, 1)
