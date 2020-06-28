#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
rospy.init_node('laser_scan_node')

def callback(msg):
  
  print msg.ranges[360]
  move = 1.0
  move1 = 0.0
  move2 = 0.0
  if msg.ranges[360] < 2 :
    move = 0.0
    move1 = 1.0
    move2 = 0.0

  pub.publish(move)
  pub1.publish(move1)
  pub2.publish(move2)



sub = rospy.Subscriber('scan_front', LaserScan , callback)
pub = rospy.Publisher('/cmd_vel' , Twist , queue_size=50)
pub1 = rospy.Publisher('/cmd_vel' , Twist , queue_size=50)
pub2 = rospy.Publisher('/cmd_vel' , Twist , queue_size=50)
msgg=Twist()
move=msgg.linear.x
move1=msgg.linear.y
move2=msgg.linear.z
rospy.spin()





