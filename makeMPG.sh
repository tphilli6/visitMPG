
ffmpeg -r 1 -i $1_%04d.png -pix_fmt yuv420p -r 1 output.mp4
