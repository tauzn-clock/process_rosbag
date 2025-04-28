import numpy as np

def filter_odom(pose,n):
    new_pose = []

    for i in range(len(pose)):
        pose[i] = (np.array(pose[i][0]),pose[i][1])
        tot = np.zeros(6)
        for j in range(max(0,i-n+1),i+1):
            tot += pose[j][0]
        tot /= (min(i+1,n))
        new_pose.append([tot,pose[i][1]])

    return new_pose

