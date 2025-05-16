#import sys
import os
import cv2
import torch
#import urllib.request
import numpy as np

#import matplotlib.pyplot as plt

input_directory = "input"
output_dm_directory = "o_dm"
output_npy_directory = "o_npy"

#print(len(os.listdir(input_directory)))

#Load Model
model_type = "DPT_Large"     # MiDaS v3 - Large     (highest accuracy, slowest inference speed)

midas = torch.hub.load("intel-isl/MiDaS", model_type)

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
midas.to(device)
midas.eval()

midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")

if model_type == "DPT_Large" or model_type == "DPT_Hybrid":
    transform = midas_transforms.dpt_transform
else:
    transform = midas_transforms.small_transform

#Prep and Computer image and depth map
for fn in os.listdir(input_directory):
    filename = os.path.join(input_directory, fn)
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    input_batch = transform(img).to(device)

    with torch.no_grad():
        prediction = midas(input_batch)

        prediction = torch.nn.functional.interpolate(
            prediction.unsqueeze(1),
            size=img.shape[:2],
            mode="bicubic",
            align_corners=False,
        ).squeeze()

    output = prediction.cpu().numpy()

    #plt.imshow(output)

    #Save depthmap and numpy array
    np.save(os.path.join(output_npy_directory, fn) + ".npy", output)
    cv2.imwrite(os.path.join(output_dm_directory, fn) + ".png", output)