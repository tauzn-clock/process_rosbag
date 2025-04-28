import numpy as np
import matplotlib.pyplot as plt

base = "/home/daoxin/scratchdata/processed/stair4"
filtered = "/home/daoxin/scratchdata/processed/stair4_filtered"

# Open pose data with numpy
pose = np.loadtxt(f"{base}/pose.csv", delimiter=",")
filtered_pose = np.loadtxt(f"{filtered}/pose.csv", delimiter=",")

print(pose.shape)
print(filtered_pose.shape)

# Plot the pose data
fig, ax = plt.subplots(3, 2, figsize=(10, 10))
ax[0,0].plot(pose[:,0])
ax[0,0].plot(filtered_pose[:,0])
ax[0,0].set_title("X")
ax[0,1].plot(pose[:,1])
ax[0,1].plot(filtered_pose[:,1])
ax[0,1].set_title("Y")
ax[1,0].plot(pose[:,2])
ax[1,0].plot(filtered_pose[:,2])
ax[1,0].set_title("Z")
ax[1,1].plot(pose[:,3])
ax[1,1].plot(filtered_pose[:,3])
ax[1,1].set_title("Roll")
ax[2,0].plot(pose[:,4])
ax[2,0].plot(filtered_pose[:,4])
ax[2,0].set_title("Pitch")
ax[2,1].plot(pose[:,5])
ax[2,1].plot(filtered_pose[:,5])
ax[2,1].set_title("Yaw")
ax[0,0].legend(["Original", "Filtered"])
ax[0,1].legend(["Original", "Filtered"])
ax[1,0].legend(["Original", "Filtered"])
ax[1,1].legend(["Original", "Filtered"])
ax[2,0].legend(["Original", "Filtered"])
ax[2,1].legend(["Original", "Filtered"])

plt.show()