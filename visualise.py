import matplotlib.pyplot as plt
import cv2
import numpy as np

SOURCE_DIR = "/scratchdata/processed/stair4"
INDEX = 175

rgb = cv2.imread(f"{SOURCE_DIR}/rgb/{INDEX}.png")
depth = cv2.imread(f"{SOURCE_DIR}/depth/{INDEX}.png", cv2.IMREAD_UNCHANGED)
print(depth.max())

plt.imsave("rgb.png", rgb)
plt.imsave("depth.png", depth)