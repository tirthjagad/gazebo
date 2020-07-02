#!/usr/bin/env python

import rospy
import rosbag
import time
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

class pubsub():
    def __init__(self):

        #subscribing into laserdata
        self.laser_scan = rospy.Subscriber('/base_scan',LaserScan,self.scan)

        #publishing the velocity
        self.mov= rospy.Publisher('/cmd_vel',Twist,queue_size=1)
        self.speed = Twist()
        

    #laserscanning
    def scan(self,laserdata):
        
        scan_data = list(laserdata.ranges)
        
        front = min(min(scan_data[0:5]),min(scan_data[140:149]),10)
        
        self.f=False
        if front <0.5:
            self.f=True

        self.control()    
        return self.f
        
        
    def control(self):
        
        if not self.f:
            self.speed.linear.x= 0.5
        
        self.mov.publish(self.speed)


    








if __name__ == '__main__':
    pubsub()
    rospy.init_node('youbot')
    rospy.spin()
    
                



     

    
