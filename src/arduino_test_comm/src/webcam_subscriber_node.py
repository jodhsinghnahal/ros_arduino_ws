#!/usr/bin/env python3

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def webcam_subscriber_callback(msg):
    bridge = CvBridge()
    frame = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
    cv2.imshow('Webcam Feed', frame)
    cv2.waitKey(1) 

def webcam_subscriber():
    rospy.init_node('webcam_subscriber', anonymous=True)
    rospy.Subscriber('/usb_cam/image_raw', Image, webcam_subscriber_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        webcam_subscriber()
    except rospy.ROSInterruptException:
        pass
