import cv2
import numpy as np

# me - this DAT
# 
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
# 
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.

def onOffToOn(channel, sampleIndex, val, prev):
	original_points = np.array([[0, 0], [1, 0], [0, 1], [1, 1]], dtype='float32')
	coords = op('coords')
	target_points = []
	for i in range(4):
		target_points.append([float(coords[i, 0]), float(coords[i, 1])])
	target_points = np.array(target_points)
	H, _ = cv2.findHomography(original_points, target_points)
	homo = op('Homography')
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
	