"""
the worker fle called in main.py
"""

import cv2


def findThreshold(img):
    
    threshold = 20
    params = cv2.SimpleBlobDetector_Params()
    params.filterByArea = True
    params.minArea = 100
    detector = cv2.SimpleBlobDetector_create(params)

    while threshold <= 60:
        threshold += 10
        _, thrash = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
        keypoints = detector.detect(thrash)
        
        if len(keypoints) >= 2:
            break

    else:
        return -1, False
    threshold = threshold - 10 if threshold >= 50 else threshold
    return threshold, True

 
def check_and_write_text(frame, pupil_consec, pupil_flag):
    if pupil_flag and pupil_consec >= 3:
        cv2.putText(frame, 'PUPIL NOT DETECTED', (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)
        return 0, False
    return pupil_consec, pupil_flag
