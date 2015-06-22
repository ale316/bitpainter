from PIL import Image
from os import walk, path
from random import randint

walker = walk('portraits')
root, folders, files = next(walker)

totH = 0
totW = 0
portraits = []

for fname in files:
	portrait = Image.open(path.join('portraits',fname))
	portraits.append(portrait)
	w, h = portrait.size

	totW += w
	totH += h

avgW = totW / len(files)
avgH = totH / len(files)
maxAvgDim = avgW if avgW > avgH else avgH

for portrait in portraits: 
	w, h = portrait.size
	w_h = w/float(h)
	h_w = h/float(w)
	size = (maxAvgDim, int(maxAvgDim*h_w)) if w < h else (int(maxAvgDim*w_h), maxAvgDim)
	portrait = portrait.resize(size)

	dx = int(abs(size[0]-avgW)*0.5)
	dy = int(abs(size[1]-avgH)*0.5)

	portrait = portrait.crop((dx, dy, avgW+dx, avgH+dy))
	# portrait.save(str(randint(0,10000))+'.jpg')
	print portrait.size
	
