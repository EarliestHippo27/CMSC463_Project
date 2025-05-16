resize_all is a program which takes in single channel 2d numpy arrays and resized them to be
224x224 whilst preserving the original numpy array's aspect ratio.
Empty space as a result of this is is filled with 0, representing infinitely far away.

A potentially better implementation would instead stretch the background value across all empty space.

TLDR, resizes the npy arrays to 224x224 and adds padding if needed.