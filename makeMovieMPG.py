
################
# use visit_utils.encoding to encode these images into a "wmv" movie
#
# The encoder looks for a printf style pattern in the input path to identify the frames of the movie. 
# The frame numbers need to start at 0. 
# 
# The encoder selects a set of decent encoding settings based on the extension of the
# the output movie file (second argument). In this case we will create a "wmv" file. 
# 
# Other supported options include ".mpg", ".mov". 
#   "wmv" is usually the best choice and plays on all most all platforms (Linux ,OSX, Windows). 
#   "mpg" is lower quality, but should play on any platform.
#
# 'fdup' controls the number of times each frame is duplicated. 
#  Duplicating the frames allows you to slow the pace of the movie to something reasonable. 
#
################
 
from visit_utils import *
varout = "z_vorticity"
input_pattern = "box_%04d.png"
output_movie = varout+".mpg"
encoding.encode(input_pattern,output_movie)


#encoding.extract(output_movie,"frames%04d.png")
#encoding.encode("frames%04d.png","slower_movie.mpg",4)
#exit()
