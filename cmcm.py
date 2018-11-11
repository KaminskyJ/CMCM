import random
import numpy as np
from scipy.spatial import distance
import pdf

X_WIDTH = 3
Y_WIDTH = 3

def gen_unif(x, y):
	return (random.uniform(0,x),random.uniform(0,y))

def find_closest_amb(ambs, coord):
	best_amb = None
	best_dist = None
	for x in ambs:
		if x[1] != 0:
			break
		new_dist = distance.euclidean(x[0],coord)
		if(best_dist == None or best_dist > new_dist):
			best_amb = x
			best_dist = new_dist
	
	return [best_amb, best_dist]

#MONTE CARLO SIMULATION
def run_sim(ambs):
	num_of_success = 0
	num_of_failure = 0
	for x in range(1440*1000):
		for ambo in ambs:
			if ambo[1] > 0:
				ambo[1] -= 1
		if random.random() > 0.00763888888:
			continue
		coord = gen_unif(X_WIDTH,Y_WIDTH)
		amb, best_dist = find_closest_amb(ambs, coord)
		if amb == None or best_dist > 2:
			num_of_failure += 1
		else:
			amb[1] = 30
			num_of_success += 1
	
	return num_of_failure/(num_of_failure + num_of_success)

def find_best(ambs, score_to_beat):
	
	pass

def main():
	amb1 = [(1,1),0]
	amb2 = [(2,2),0]
	print(run_sim([amb1,amb2]))


if __name__ == "__main__":
	main()


"""
THRESHOLD = .1
def find_best(amb_loc, score_to_beat):
	a,b = amb_loc
	print((round(a,1),round(b,1)))
	
	right_score = run_sim((a+THRESHOLD,b))
	if score_to_beat > right_score:
		return find_best((a+THRESHOLD,b), right_score)
	left_score = run_sim((a-THRESHOLD,b))
	if score_to_beat > left_score:
		return find_best((a-THRESHOLD,b), left_score)
	down_score = run_sim((a,b-THRESHOLD))
	if score_to_beat > down_score:
		return find_best((a,b-THRESHOLD), down_score)
	up_score = run_sim((a,b+THRESHOLD))
	if score_to_beat > up_score:
		return find_best((a,b+THRESHOLD), up_score)
	else:
		return (round(a,1),round(b,1))
"""
