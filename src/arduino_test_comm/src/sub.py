#!/usr/bin/env python3
#source ~/ros_arduino_ws/devel/setup.bash
#rosrun arduino_test_comm sub.py
import rospy
import cv2
from std_msgs.msg import Int16
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

state = False

def potentiometer_callback(msg):
    global state

    rospy.set_param('usb_cam/framerate', msg.data)
    print(rospy.get_param('usb_cam/framerate'))

    rospy.loginfo("Received Potentiometer State: %d", msg.data)
    if msg.data > 0:
        state = True
    else:
        state = False

def cam1_callback(msg):
    if state:
        bridge = CvBridge()
        frame = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        frame = cv2.flip(frame, 1)
        cv2.imshow('Webcam Feed', frame)
        cv2.waitKey(1) 
    else:
        cv2.destroyAllWindows()

def potentiometer_subscriber():
    rospy.init_node('potentiometer_subscriber', anonymous=True)

    rospy.Subscriber('potentiometer_state', Int16, potentiometer_callback)
    rospy.Subscriber('/usb_cam/image_raw', Image, cam1_callback)

    rospy.loginfo("Potentiometer Subscriber Node is running.")
    rospy.spin()

if __name__ == '__main__':
    try:
        potentiometer_subscriber()
    except rospy.ROSInterruptException:
        pass
