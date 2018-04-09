# get the number of timesteps
nts = TimeSliderGetNStates()
 
# set basic save options
swatts = SaveWindowAttributes()
#
# The 'family' option controls if visit automatically adds a frame number to 
# the rendered files. For this example we will explicitly manage the output name.
#
swatts.family = 0
#
# select PNG as the output file format
#
swatts.format = swatts.PNG 
#
# set the width of the output image
#
swatts.width = 1024 
#
# set the height of the output image
#
swatts.height = 1024
 
#the encoder expects file names with an integer sequence
# 0,1,2,3 .... N-1
 
file_idx = 1

for ts in range(file_idx,nts,1): # look at every 10th frame
    # Change to the next timestep
    TimeSliderSetState(ts)
    #before we render the result, explicitly set the filename for this render
    swatts.fileName = "png/"+varout+"_%04d.png" % file_idx
    SetSaveWindowAttributes(swatts)
    # render the image to a PNG file
    SaveWindow()
    file_idx +=1
