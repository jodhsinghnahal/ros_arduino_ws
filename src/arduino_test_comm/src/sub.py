#!/usr/bin/env python3
#source ~/ros_arduino_ws/devel/setup.bash
#rosrun arduino_test_comm sub.py
import rospy
import cv2
from std_msgs.msg import Int16


def potentiometer_callback(msg):
    if msg.data > 50:
        cam = cv2.VideoCapture(0)

        # Capture a single frame
        check, frame = cam.read()

        # Display the captured frame
        cv2.imshow('video', frame)
        cv2.waitKey(0)  # Wait for a key press

        # Release the video capture resources
        cam.release()
        cv2.destroyAllWindows()

    rospy.loginfo("Received Potentiometer State: %d", msg.data)

def potentiometer_subscriber():
    rospy.init_node('potentiometer_subscriber', anonymous=True)

    # Define the topic to subscribe to and the message type
    topic_name = 'potentiometer_state'
    msg_type = Int16

    # Create a subscriber
    rospy.Subscriber(topic_name, msg_type, potentiometer_callback)

    rospy.loginfo("Potentiometer Subscriber Node is running.")
    rospy.spin()

if __name__ == '__main__':
    try:
        potentiometer_subscriber()
    except rospy.ROSInterruptException:
        pass
