import rosbag
import os
from sensor_msgs.msg import CameraInfo
import json
import numpy as np
import cv2
from cv_bridge import CvBridge
from match import match

DESTINATION_DIR = '/scratchdata/processed/stair4'

if not os.path.exists(DESTINATION_DIR):
    os.makedirs(DESTINATION_DIR)
if not os.path.exists(os.path.join(DESTINATION_DIR, "rgb")):
    os.makedirs(os.path.join(DESTINATION_DIR, "rgb"))
if not os.path.exists(os.path.join(DESTINATION_DIR, "depth")):
    os.makedirs(os.path.join(DESTINATION_DIR, "depth"))

# Open the rosbag file
bag = rosbag.Bag('/scratchdata/stair4.bag', 'r')

# Camera Info
camera_info = {}
for topic, msg, t in bag.read_messages(topics=['/camera/color/camera_info']):
    print(msg)
    camera_info["D"] = msg.D
    camera_info["K"] = msg.K
    camera_info["R"] = msg.R
    camera_info["P"] = msg.P
    camera_info["height"] = msg.height
    camera_info["width"] = msg.width
    break
# Save the camera info as a JSON file
with open(os.path.join(DESTINATION_DIR,'camera_info.json'), 'w') as json_file:
    json.dump(camera_info, json_file, indent=4)

print("Camera info has been saved to 'camera_info.json'.")

rgb = []
depth = []
pose = []

for topic, msg, t in bag.read_messages(topics=['/camera/color/image_raw']):
    rgb_img = np.frombuffer(msg.data, dtype=np.uint8).reshape(msg.height, msg.width, 3)
    rgb_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2RGB)
    rgb.append((rgb_img, t))

for topic, msg, t in bag.read_messages(topics=['/camera/depth/image_raw']):
    depth_img = np.frombuffer(msg.data, dtype=np.uint16).reshape(msg.height, msg.width)
    depth.append((depth_img, t))

for topic, msg, t in bag.read_messages(topics=['/camera/gyro_accel/sample']):
    pose.append(([msg.linear_acceleration.x, msg.linear_acceleration.y, msg.linear_acceleration.z, msg.angular_velocity.x, msg.angular_velocity.y, msg.angular_velocity.z],t))

depth = match(rgb,depth)
pose = match(rgb,pose)

print(len(rgb), len(depth), len(pose))

for i in range(len(rgb)):
    rgb_img = rgb[i][0]
    depth_img = depth[i][0]
    depth_img = depth_img.astype(np.uint16)
    # Save the RGB image
    cv2.imwrite(os.path.join(DESTINATION_DIR, "rgb", f'{i}.png'), rgb_img)
    # Save the depth image
    cv2.imwrite(os.path.join(DESTINATION_DIR, "depth", f'{i}.png'), depth_img)   

pose_np = []
for i in range(len(pose)):
    pose_np.append(np.array(pose[i][0]))
pose_np = np.array(pose_np, dtype=np.float32)
print(pose_np.shape)
np.savetxt(os.path.join(DESTINATION_DIR, "pose.csv"), pose_np, fmt='%f', delimiter=',')

# Tie everythng to rgb img

# Close the ROS bag
bag.close()

