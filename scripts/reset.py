# me - this DAT
# 
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
# 
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.

def onOffToOn(channel, sampleIndex, val, prev):
	ur = op('../ur')
	ul = op('../ul')
	dr = op('../dr')
	dl = op('../dl')
	xmax = ur.par.repositionxmax
	ymax = ur.par.repositionymax
	ur.par.x = xmax
	ur.par.y = ymax
	ul.par.x = 0
	ul.par.y = ymax
	dr.par.x = xmax
	dr.par.y = 0
	dl.par.x = 0
	dl.par.y = 0	

	return

def whileOn(channel, sampleIndex, val, prev):
	return

def onOnToOff(channel, sampleIndex, val, prev):
	return

def whileOff(channel, sampleIndex, val, prev):
	return

def onValueChange(channel, sampleIndex, val, prev):
	return
	