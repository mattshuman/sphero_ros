#!/usr/bin/env python

import roslib; 
import rospy

from geometry_msgs.msg import Pose
from sensor_msgs.msg import LaserScan

from PySide.QtCore import * 
from PySide.QtGui import * 
import sys

class imuTracker:

  def __init__(self): 
    # A publisher for integrated accelerations used to estimate Sphero position
    self.pub1 = rospy.Publisher('imuLocation', String, queue_size=0)
        
    # A subscriber for IMU data from SpheroNode
    self.sub = rospy.Subscriber('imu', String, self.sub_callback)

  def pub1_callback(self):
    print "publishing new location"
    #self.pub1.publish('Publishing a new location')
   
  def sub_callback(self, msg):
    print "Received: ", msg.data


if __name__ == '__main__':
  # Initialize the node
  rospy.init_node('imuTracker')

  # Initialize Qt
  app = QApplication(sys.argv)

  gui = GUI()

  app.exec_()
