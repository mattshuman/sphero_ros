#!/usr/bin/env python

from visualization_msgs.msg import Marker
import rospy
import rospkg

rospack = rospkg.RosPack()

topic = 'visualization_marker'
pub = rospy.Publisher(topic, Marker, queue_size=1)

rospy.init_node('LidarMarker')

count = 1
def markLidar():
  marker = Marker()
  marker.header.frame_id = 'laser'
  marker.id = count
  marker.ns = str(count) 
  marker.type = marker.TEXT_VIEW_FACING #SPHERE
  marker.action = marker.ADD
  marker.scale.x = .15
  marker.scale.y = .15
  marker.scale.z = .15
  marker.color.a = 1.0
  marker.color.r = 1.0
  marker.color.g = 0.0
  marker.color.b = 0.0
  marker.pose.orientation.w = 1.0
  marker.pose.position.x = 0
  marker.pose.position.y = 0
  marker.pose.position.z = 0 
  marker.text = "LIDAR"
  return marker

while not rospy.is_shutdown():
   # Publish the MarkerArray
  marker = markLidar()
  pub.publish(marker)
  rospy.sleep(.1)
