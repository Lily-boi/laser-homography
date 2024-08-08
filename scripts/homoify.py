import numpy as np

# me - this DAT
# scriptOp - the OP which is cooking

# press 'Setup Parameters' in the OP to call this function to re-create the parameters.
def onSetupParameters(scriptOp):
	multiply(scriptOp)
	return

# called whenever custom pulse parameter is pushed
def onPulse(par):
	return

def onCook(scriptOp):
	scriptOp.clear()
	return

def multiply(scriptOp):
	coords = op('merge2').numpyArray()
	coords[2] = 1
	Homo = op('Homography')
	H = []
	for i in range(3):
		H.append([float(Homo[i, 0]), float(Homo[i, 1]), float(Homo[i, 2])])
	H = np.array(H)
	new = H @ coords
	op('trans_line').par.value0 = new[0]/new[2] + 1
	op('trans_line').par.value1 = new[1]/new[2]
	op('trans_line').par.value2 = 0