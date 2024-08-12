import numpy as np

# me - this DAT
# scriptOp - the OP which is cooking

# press 'Setup Parameters' in the OP to call this function to re-create the parameters.
def onSetupParameters(scriptOp):
    scriptOp.clear()
    return

# called whenever custom pulse parameter is pushed
def onPulse(par):
	return

def onCook(scriptOp):
    multiply(scriptOp)
    scriptOp.clear()
    return

def multiply(scriptOp):
	coords = op('../vector').numpyArray()
	Homo = op('homography')
	H = []
	for i in range(3):
		H.append([float(Homo[i, 0]), float(Homo[i, 1]), float(Homo[i, 2])])
	H = np.array(H)
	new = H @ coords
	op('transformed').par.value0 = new[0]/new[2]
	op('transformed').par.value1 = new[1]/new[2]
	op('transformed').par.value2 = 0