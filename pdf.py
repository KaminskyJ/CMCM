from scipy.misc import imread
import numpy as np
import random

def gen_pdf(image, vals):
	img = imread(image)
	width, height, v = img.shape
	flat = img.reshape(width*height ,v)
	print(flat[0])


def gen_random_point():
	return [0,0]
	total = 30014
	a = random.random()
	color_of_interest = None
	if a < 5812/total:
		color_of_interest = [255,80,0]
	if a < (5812 + 5817)/total:
		color_of_interest = [255,0,0]
	if a < (5812 + 5817 + 6324)/total:
		color_of_interest = [155,0,0]
	if a < (5812 + 5817 + 6324 + 6279)/total:
		color_of_interest = [190,0,0]
	if a < (5812 + 5817 + 6324 + 6279 + 5782)/total:
		color_of_interest = [255,200,0]
	img = imread("districtpopulation.png")
	width, height, v = img.shape
	while(True):
		x = np.random.randint(0,width)
		y = np.random.randint(0,height)
		if(img[x,y].tolist() == color_of_interest):
			return [x,y]


def main():
	#[255,80,0] pop 5812
	#[255,0,0] pop 5817
	#[155,0,0] pop 6324
	#[190,0,0] pop 6279
	#[255,200,0] pop 5782
	#total = 30014
	
	print(gen_random_point())
	
if __name__ == "__main__":
	main()