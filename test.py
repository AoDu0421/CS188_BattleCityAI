#for test
import random
import pygame
import copy

if __name__ == "__main__":
	searchedMap = [[] for irow in range(4)]
	for itimes in range(4):
		searchedMap[itimes] = [0 for jcolumn in range(4)]
	print searchedMap

	if searchedMap[0][1] == 0:
		searchedMap[0][1] = 1
	else:
		searchedMap[0][2] = 1
	print searchedMap

	a1 = pygame.Rect([3,1], [26, 26])
	a2 = pygame.Rect([3,5], [26, 26])
	a3 = pygame.Rect([3,7], [26, 26])
	searchQueue = []
	searchQueue.insert(0,1)
	print searchQueue
	print searchQueue.pop()

	print searchQueue.push()

	