import random

X_WIDTH = 1000
Y_WIDTH = 1000

def pdf_unif(x, y):
	if x > 0 and y > 0:
		if x < X_WIDTH and y < Y_WIDTH:
			return 1/(X_WIDTH*Y_WIDTH)
	return 

def modify (arr, coord, dist):
	to_return = arr
	for x in range(coord[0][0]-dist,coord[0][0]+dist):
		for y in range(coord[0][1]-dist,coord[0][1]+dist):
			if (x-amb[0][0])**2+ (y-amb[0][1])**2 < dist**2:
				to_return[x,y] = 0
	return to_return

def pdf_at_time(amb, ambs):
	arr = np.zeroes(X_WIDTH,Y_WIDTH)
	for x in range(X_WIDTH):
		for y in range(Y_WIDTH):
			arr[x,y] += pdf_unif(x,y)
	for amb in ambs:
		 arr = modify(arr, amb[0], 500)

def find_prob(amb, ambs, dist):
	total_prob = 0
	for x in range(amb[0][0]-dist,amb[0][0]+dist):
		for y in range(amb[0][1]-dist,amb[0][1]+dist):
			if (x-amb[0][0])**2+ (y-amb[0][1])**2 < dist**2:
				total_prob += pdf_unif(x,y)
	return total_prob

def optimize():
	pass

def main():
	amb1 = [(0,0),0]
	amb2 = [(X_WIDTH,Y_WIDTH),0]
	ambs = [amb1,amb2]
	print(find_prob(amb1, ambs, 500))


if __name__ == "__main__":
	main()