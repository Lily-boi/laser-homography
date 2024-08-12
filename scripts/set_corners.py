import numpy as np
import cv2
# me - this DAT
# 
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
# 
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.

def onOffToOn(channel, sampleIndex, val, prev):
    tab = op('../screen/coords')
    for i in range(4):
        x = op(f'../screen/geo1/line{5+i}').par.pax
        y = op(f'../screen/geo1/line{5+i}').par.pay
        tab[i, 0] = x
        tab[i, 1] = y
        

    original_points = np.array([[1, 1], [1, -1], [-1, -1], [-1, 1]])
    target_points = []
    for i in range(4):
        target_points.append([float(tab[i, 0]), float(tab[i, 1])])
    target_points = np.array(target_points)
    H, _ = cv2.findHomography(original_points, target_points)
    homo = op('../screen/homography')
    for i in range(3):
        for j in range(3):
            homo[i, j] = H[i, j]
    return

def whileOn(channel, sampleIndex, val, prev):
	return

def onOnToOff(channel, sampleIndex, val, prev):
	return

def whileOff(channel, sampleIndex, val, prev):
	return

def onValueChange(channel, sampleIndex, val, prev):
	return
	