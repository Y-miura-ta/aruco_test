# -*- coding: utf-8 -*

# ROS環境との競合を避ける
# import sys
# sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

dictionary_name = cv2.aruco.DICT_4X4_50
dictionary = cv2.aruco.getPredefinedDictionary(dictionary_name)

SEARCH_IDs = [1, 2, 3]

while True:
    ret, frame = cap.read()
    
    frame = cv2.resize(frame, (frame.shape[1], frame.shape[0]))
    
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(frame, dictionary)
    frame = cv2.aruco.drawDetectedMarkers(frame, corners, ids)
    
    if(type(ids) != type(None)):
        match_ids = np.intersect1d(ids, SEARCH_IDs)
        match_num = len(match_ids)
        if(match_num != 0):
            print("ID No : {} is found".format(match_ids))
    
    cv2.imshow('Edited Frame', frame)
    
    k = cv2.waitKey(1)
    if k == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
