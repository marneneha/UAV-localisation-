#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import sys

bridge = CvBridge()

def image_callback(ros_image):
    print("i am getting in")
    print("in while")
    global bridge
    cv_image = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    cv2.imshow("Feed", cv_image)
    cv2.waitKey()
    print("end")


  
def main(args):
    rospy.init_node('image_converter', anonymous=True)
    try:
        image1= rospy.Subscriber("/uav1/bluefox_optflow/image_raw",Image,image_callback) 
	rospy.spin()
    except KeyboardInterrupt:
        print("Shutting Down")
    	cv2.destroyAllWindows()
if __name__ == '__main__':
    main(sys.argv)



