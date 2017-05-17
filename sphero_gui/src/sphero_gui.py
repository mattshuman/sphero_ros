#!/usr/bin/env python

import roslib; 
import rospy
import sys

from std_msgs.msg import String
from std_msgs.msg import ColorRGBA
from geometry_msgs.msg import Twist

from PySide.QtCore import * 
from PySide.QtGui import * 

class GUI:

  def __init__(self): 
    # A publisher for move messages
    self.pub1 = rospy.Publisher('cmd_vel', Twist, queue_size=0)
        
    #A publisher for the Sphero
    self.pub2 = rospy.Publisher('set_color', ColorRGBA, queue_size=0)

    # A subscriber for our own messages
    #self.sub = rospy.Subscriber('loopback', String, self.sub_callback)

    self.widget = QWidget()
    self.widget.show()  

    self.labLinX = QLabel("Linear.X", self.widget)
    self.labLinX.move(10,35)
    self.labLinX.show()

    self.bLinX = QDoubleSpinBox(self.widget)
    self.bLinX.setRange(-1, 1)
    self.bLinX.setSingleStep(.1)
    self.bLinX.setDecimals(1)
    self.bLinX.move(80,30)
    self.bLinX.show()
    
    self.labLinY = QLabel("Linear.Y", self.widget)
    self.labLinY.move(210,35)
    self.labLinY.show()

    self.bLinY = QDoubleSpinBox(self.widget)
    self.bLinY.setRange(-1, 1)
    self.bLinY.setSingleStep(.1)
    self.bLinY.setDecimals(1)
    self.bLinY.move(280,30)
    self.bLinY.show()
    
    self.labLinZ = QLabel("Linear.Z", self.widget)
    self.labLinZ.move(410,35)
    self.labLinZ.show()

    self.bLinZ = QDoubleSpinBox(self.widget)
    self.bLinZ.setRange(-1, 1)
    self.bLinZ.setSingleStep(.1)
    self.bLinZ.setDecimals(1)
    self.bLinZ.move(480,30)
    self.bLinZ.show()

    self.labAngX = QLabel("Angular.X", self.widget)
    self.labAngX.move(10,75)
    self.labAngX.show()

    self.bAngX = QDoubleSpinBox(self.widget)
    self.bAngX.setRange(-1, 1)
    self.bAngX.setSingleStep(.1)
    self.bAngX.setDecimals(1)
    self.bAngX.move(80,70)
    self.bAngX.show()
    
    self.labAngY = QLabel("Angular.Y", self.widget)
    self.labAngY.move(210,75)
    self.labAngY.show()

    self.bAngY = QDoubleSpinBox(self.widget)
    self.bAngY.setRange(-1, 1)
    self.bAngY.setSingleStep(.1)
    self.bAngY.setDecimals(1)
    self.bAngY.move(280,70)
    self.bAngY.show()
    
    self.labAngZ = QLabel("Angular.Z", self.widget)
    self.labAngZ.move(410,75)
    self.labAngZ.show()

    self.bAngZ = QDoubleSpinBox(self.widget)
    self.bAngZ.setRange(-1, 1)
    self.bAngZ.setSingleStep(.1)
    self.bAngZ.setDecimals(1)
    self.bAngZ.move(480,70)
    self.bAngZ.show()
    
    self.button3 = QPushButton('&Move', self.widget)
    self.button3.move(220,105)
    self.button3.clicked.connect(self.moveSphero)
    self.button3.show()

    self.redBox = QCheckBox('&Red', self.widget)
    self.redBox.move(30,150)
    self.redBox.show()
   
    self.greenBox = QCheckBox('&Green', self.widget)
    self.greenBox.move(80,150)
    self.greenBox.show()
    
    self.blueBox = QCheckBox('B&lue', self.widget)
    self.blueBox.move(150,150)
    self.blueBox.show()
    
    self.colorButton = QPushButton('C&hange Color', self.widget)
    self.colorButton.move(50,180)
    self.colorButton.clicked.connect(self.changeColor)
    self.colorButton.show()
    
  def moveSphero(self):
    command = Twist()
    command.linear.x = self.bLinX.value()
    command.linear.y = self.bLinY.value()
    command.linear.z = self.bLinZ.value()
    command.angular.x = self.bAngX.value()
    command.angular.y = self.bAngY.value()
    command.angular.z = self.bAngZ.value()
    print command
    self.pub1.publish(command)
 
  def changeColor(self):
    command = ColorRGBA()
    command.r = int(self.redBox.checkState())
    command.g = int(self.greenBox.checkState())
    command.b = int(self.blueBox.checkState())
    command.a = 0
    self.pub2.publish(command)

  def sub_callback(self, msg):
    print 'Sphero:', msg.data

if __name__ == '__main__':
  # Initialize the node
  rospy.init_node('sphero_gui')

  # Initialize Qt
  app = QApplication(sys.argv)

  gui = GUI()

  app.exec_()
