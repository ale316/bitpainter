from PIL import Image
from os import walk, path

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

print avgW, avgH
	
for portrait in portraits: 
	w, h = portrait.size
	w_h = w/float(h)
	h_w = h/float(w)
	size = (maxAvgDim, int(maxAvgDim*h_w)) if w < h else (int(maxAvgDim*w_h), maxAvgDim)
	print w_h, h_w, w,h,size
	portrait = portrait.resize(size)

	dx = abs(size[0]-avgW)*0.5
	dy = abs(size[1]-avgH)*0.5

	portrait = portrait.crop((dx, dy, avgW+dx, avgH+dy))

	print portrait.size
	