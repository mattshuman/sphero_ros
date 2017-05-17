#!/usr/bin/env python
import roslib;
import rospy

import hokuyo_node
import sensor_msgs.msg

def callback(data):
    pass
def laser_listener():
    pass
    rospy.init_node('laser_listener', anonymous=True)
    rospy.Subscriber("/sensor_msgs/LaserScan",sensor_msgs.msg.LaserScan,callback,20)
    rospy.spin()

if __name__ == '__main__':
    laser_listener()
