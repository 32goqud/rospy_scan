#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
import numpy as np
import matplotlib.pyplot as plt
import math
from numpy import inf


angle = ()
cosine_theta =()
sine_theta =()

for i in range(180,-180,-1):
    angle = np.array(np.append(angle,i))

for j in range(360):
    cosine_array = math.cos(math.radians(angle[j]))
    sine_array = math.sin(math.radians(angle[j]))
    cosine_theta = np.array(np.append(cosine_theta,cosine_array))
    sine_theta = np.array(np.append(sine_theta,sine_array))

#data
def callback(msg):
    global r
    r=msg.ranges[::1]
    r = np.array(r)
    r[r == -inf] = 0
    r[r == inf] = 0

def distance(self):
    global x # global value define
    global y # global value define
    x = r*sine_theta
    y = r*cosine_theta
    return x,y

def distance_pop(self):
    plt.axis([-10,10,-10,10])
    sub1, = plt.plot(x,y,'o',color='blue', ms=4)
    plt.pause(0.0000000001)
    sub1.remove()

def clustering(self):
    global data
    data = np.array(list(zip(x, y))).reshape(len(x), 2)
    K = 3
    kmeans = KMeans(n_clusters=K).fit(data)
    color= {0 : 'r', 1 : 'g', 2: 'b'}
    color_label = np.array([color[i] for i in kmeans.labels_]) # color array(shape = (271,0))
    print kmeans.labels_

#subscriber 
def listener():
    rospy.init_node('scan_values')
    rospy.Subscriber('/p3dx/laser/scan', LaserScan, callback)
    rospy.Subscriber('/p3dx/laser/scan', LaserScan, distance)
    rospy.Subscriber('/p3dx/laser/scan', LaserScan, distance_pop)
    #rospy.Subscriber('/scan', LaserScan, clustering)
    rospy.spin()

#executable
if __name__ == '__main__':
    try:
        listener()

    except rospy.ROSInterruptException:
        pass
