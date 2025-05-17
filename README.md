# Quasi-Identifier Estimation From Pseudo-LiDar Depthmaps

## Dataset
The original dataset from which we performed processes on to create a depthmap dataset is the [Celeb-FBI](https://doi.org/10.48550/arXiv.2407.03486) (https://doi.org/10.48550/arXiv.2407.03486) dataset by Debnath et al.
Download the converted dataset [here](https://drive.google.com/drive/folders/1WkfvErPv3X2jbSwig-ket4a9BJVdyL2_?usp=sharing).

## Processing on Dataset
For the training of our models, we followed a process outlined by [Wang et al.](https://doi.org/10.48550/arXiv.1812.07179) (https://doi.org/10.48550/arXiv.1812.07179) where converting images to depthmaps can be used as a substitute for LiDar pointclouds.
In our case we used the Celeb-FBI dataset however any image dataset could be used in future works following this project.
- The images are converted to a depthmap represented by a numpy array using the MiDaS v3 - Large Depth Estimation model by Intel.
- From here the depthmaps are then resized to 224x224 with BiLinear Interpolation whilst preserving the original images aspect ratio and adding padding with value 0.0 to any empty space.
- The data is then ready to be fed into our models for training and testing.

## Using The Files
- In the Image_To_Depthmap directory, modify the directory variables to be the path of the directory of the image dataset, the output path of the depthmap images, and the output path of the depthmap numpy files. Run the python file to convert the images to depthmaps.
- In npy_resize, modify the directory variables to be the path of the numpy files and the output path of the resized numpy files. Run each cell of the notebook sequentially to resize the depthmap numpy arrays.
- - From here you are ready to train, test and use the models.
- Each directory following the naming convention "X_estimation" contains:
- - A .csv containing the labels in the format Filename, Label.
  - A Jupyter Notebook File.
  - Our trained model
  - readme.txt
- To reproduce our results you can simply use the provided annotations in the .csv file and run the cells in the notebook file.
- For your own dataset, it will be necesarry to recreate the annotations yourself.
