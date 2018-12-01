'''
Date: 
Author: Maggie Wu 

To find all paths in all angles from every location 

'''

import math 
import numpy as np 
from scipy import stats 

distance = 100
branch = 10

def collide(x, y, size, angle, block, collision=False):
    # right bounce
    if  block.x > x > block.x - size:
        if block.y < y < block.y + block.size[1]: 
            x = block.x - size
            angle = - angle 
            collision = True 

    # left bounce 
    elif block.x + block.size[0] < x < block.x + block.size[0] + size: 
        if block.y < y < block.y + block.size[1]: 
            x =  block.x + block.size[0] + size 
            angle = - angle
            collision = True 

    # up bounce 
    elif block.y > y > block.y - size: 
    	if block.x < x < block.x + block.size[0]: 
    		y = block.y - size 
    		angle = math.pi - angle 
    		collision = True 

    # down bounce 
    elif block.y + block.size[1] < y < block.y + block.size[1] + size: 
        if block.x < x < block.x + block.size[0]: 
            y = block.y + block.size[1] + size 
            angle = math.pi - angle 
            collision = True 

    return collision, angle, x, y

def getPaths(x, y, width, height, size, angle, blocks, targets):
	# range of ~20 degrees 
	# gaussian distribution from 45 degrees 
	# path = {angle: {pos: [(block, bounce)]}}

	# per angle either hits target or has number of bounce 
	# {angle: [hitTarget, number bounce]}

	path = dict() 
	possible_angles = np.linspace(angle-math.pi/16, angle+math.pi/16, branch)
	distributions = stats.norm(angle, math.pi/32)
	dist_vals = [distributions.pdf(p) for p in possible_angles]

	for a in range(len(possible_angles)): 
		dist = 1
		extend = 1

		current_angle = possible_angles[a]
		prob = dist_vals[a]
		current_x = x 
		current_y = y 

		bounce = 0
		hit = 'none'

		while dist <= distance: 
			next_x = current_x + min(dist, extend)*math.sin(current_angle)
			next_y = current_y - min(dist, extend)*math.cos(current_angle)
			for b in blocks: 
				collision, new_angle, new_x, new_y = collide(next_x, next_y, size, current_angle, b)
				if collision: 
					current_angle = new_angle
					current_x = new_x
					current_y = new_y 
					extend = 0
					bounce += 1
			for t in targets: 
				collision, new_angle, new_x, new_y = collide(next_x, next_y, size, current_angle, t)
				if collision: 
					hit = t.name
					dist = distance

			dist += 1
			extend += 1 

		# return in degree to make it easier to debug 
		path[180*possible_angles[a]/math.pi] = (hit, bounce, prob)

	return path 

def getDistribution(x, y, width, height, size, angle, blocks, targets): 
	path = getPaths(x, y, width, height, size, angle, blocks, targets)
	dist = {'green':0, 'red':0, 'none':0}
	n = len(path)

	for angle in path: 
		hit, bounce, prob = path[angle]
		dist[hit] += prob

	norm_dist = {hit: dist[hit]/sum(dist.values()) for hit in dist}
	return norm_dist 



