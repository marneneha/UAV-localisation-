#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import sys

bridge = CvBridge()
cap = cv2.VideoCapture(0)

  
def main(args):
    rospy.init_node('image_converter', anonymous=True)
    try:
	while(1):
		_,frame = cap.read()
		cv2.imshow('Contours',frame)              
		k=cv2.waitKey(10)
    except KeyboardInterrupt:
        print("Shutting Down")
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main(sys.argv)
