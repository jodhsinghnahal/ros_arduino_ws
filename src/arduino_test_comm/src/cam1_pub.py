#!/usr/bin/env python3

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def camera_publisher():
    rospy.init_node('camera_publisher', anonymous=True)

    topic_name = 'camera_image'
    msg_type = Image

    image_pub = rospy.Publisher(topic_name, msg_type, queue_size=10)

    # Initialize the camera (camera index 0 by default)
    cap = cv2.VideoCapture(0)

    # Create a CvBridge to convert between OpenCV images and ROS Image messages
    bridge = CvBridge()

    rospy.loginfo("Camera Publisher Node is running.")

    rate = rospy.Rate(30)  
    while not rospy.is_shutdown():
        # Read a frame from the camera
        ret, frame = cap.read()

        if ret:
            # Convert the OpenCV frame to a ROS Image message
            ros_image = bridge.cv2_to_imgmsg(frame, encoding="bgr8")

            # Publish the ROS Image message to the specified topic
            image_pub.publish(ros_image)

        rate.sleep()

    # Release the camera resources
    cap.release()

if __name__ == '__main__':
    try:
        camera_publisher()
    except rospy.ROSInterruptException:
        pass
