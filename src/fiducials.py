#!/usr/bin/env python

import rospy, cv2, cv_bridge, numpy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
import math
from fiducial_msgs.msg import FiducialTransformArray


class Follower:
    def __init__(self):
        self.bridge = cv_bridge.CvBridge()
        #self.image_sub = rospy.Subscriber('/camera/rgb/image_raw', Image, self.image_callback)
        #self.centroid_pub = rospy.Publisher('centroid', Image, queue_size=1)
        self.cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
        self.fiducial_sub = rospy.Subscriber('/fiducial_transforms', FiducialTransformArray, self.fiducial_callback)
        self.twist = Twist()
        self.first_fiducial = 101
        self.second_fiducial = 105
        self.distance = 0
        self.angle = 0

    def fiducial_callback(self, data):
        #data transform 
        if data.transforms != []:
            fiducial = data.transforms[0]
            translation = fiducial.transform.translation #getting the pose
            print(self.distance) 

            if translation.z != None:
                self.distance = translation.z #bc z is distance measurement 
            if translation.x != None:
                self.angle = translation.x #and x is the angle of the robot 
                
            if self.distance > 0.50:
                #switching the angle of the robot so it does not blindly go straight 
                if self.angle > 0:
                    self.twist.angular.z = -0.1
                    self.twist.linear.x = 0.1
                    self.cmd_vel_pub.publish(self.twist)
                    self.twist.linear.x = 0.1
                    self.cmd_vel_pub.publish(self.twist)
                elif self.angle < 0:
                    self.twist.angular.z = 0.1
                    self.cmd_vel_pub.publish(self.twist)
                    self.twist.linear.x = 0.1
                    self.cmd_vel_pub.publish(self.twist)
        else: 
            #turns in its place until fiducial found
            if self.distance <= 0.50:
                self.twist.linear.x = 0
                self.twist.angular.z = -0.1
                self.cmd_vel_pub.publish(self.twist)

rospy.init_node('follower')
follower = Follower()
rospy.spin()