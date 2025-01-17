import math
import random
from bisect import bisect_left
from random import randint
import matplotlib.pyplot as plt
import matplotlib

class colony:
	class ant:
		def __init__(self, colony):
			self.visited_food_locations = [colony.start]
			self.traveled_distance = 0
			
			self.unvisited_food_locations = \
                                                      colony.food_locations.difference\
                                                      (self.visited_food_locations)
			self.colony = colony
			self.current_location = colony.start

		def collect_food(self):
			while(self.unvisited_food_locations):
				self.visit_location()
			
		def reset(self, colony):
			self.__init__(colony)
			
			
		def visit_location(self):
			roulette_wheel = [0]
			locations = []

			for new_location in self.unvisited_food_locations:
				locations.append(new_location)
				roulette_wheel.append(roulette_wheel[-1] +
                                                      math.pow(colony.get_pheromones\
                                                               (self.current_location,\
                                                                                     new_location),
                                                               colony.alpha)*
                                                      math.pow((1.0/colony.distance\
                                                                (self.current_location,\
                                                                                    new_location)),\
                                                               colony.beta))
			
			ran = random.uniform(0, roulette_wheel[-1])
			i = bisect_left(roulette_wheel, ran)
			self.traveled_distance += colony.distance(self.current_location,\
                                                                  locations[i-1])
			self.current_location = locations[i-1]
			self.unvisited_food_locations.remove(self.current_location)
			self.visited_food_locations.append(self.current_location)
			return
			
		
	def __init__(self, food_locations, distance_callback, \
                     start, ant_count=50, iterations=80,\
                     alpha=.5, beta=1.2,  \
                     pheromone_evaporation_coefficient=.40, pheromone_constant=1.0):
		self.shortest_path_distance = float('inf')
		self.shortest_path = []
		
		self.food_locations = food_locations
		self.distance = distance_callback
		self.start = start
		if start not in food_locations: food_locations.add(start)
		self.ant_count = ant_count
		self.iterations = iterations
		self.alpha = alpha
		self.beta = beta
		self.pheromone_evaporation_coefficient = pheromone_evaporation_coefficient
		self.pheromone_constant = pheromone_constant
		self.pheromones = self.init_pheromones(food_locations)
		self.new_pheromones = self.init_pheromones(food_locations)

	def run(self):
		ant = self.ant(self)
		for _ in range(self.iterations):
			for ant_number in range(self.ant_count):
				ant.collect_food()
				if ant.traveled_distance < self.shortest_path_distance: 
					self.shortest_path_distance = ant.traveled_distance
					self.shortest_path = ant.visited_food_locations
				self.leave_pheromones_trail(ant.visited_food_locations,\
                                                            ant.traveled_distance)
				ant.reset(self)
			self.pheromone_evaporate()
			
	
	def init_pheromones(self, food_locations):
		return dict.fromkeys([(source_location,destination_location)\
                                      for source_location in food_locations \
                                      for destination_location in food_locations \
                                      if source_location != destination_location], 0.1)	


	def get_pheromones(self, source_location, destination_location):
		return self.pheromones[(source_location, destination_location)]


	def leave_pheromones_trail(self, path, traveled_distance):
		for i in range(len(path) - 1):
			self.new_pheromones[(path[i], path[i+1])] += \
                                                      self.pheromone_constant/traveled_distance
			
		
	def pheromone_evaporate(self):
		for k in self.new_pheromones.keys():
			self.new_pheromones[k] = \
                                               self.new_pheromones[k] * \
                                               self.pheromone_evaporation_coefficient
	


def draw_multiple_points(coord_list):
    for i in range(0,len(coord_list)):
        plt.scatter(coord_list[i][0], coord_list[i][1], s=10)
    plt.title("Food Locations ", fontsize=8)
    plt.xlabel("x Coord", fontsize=8)
    plt.ylabel("y Coord", fontsize=8)
   # plt.ion()
    plt.show()

def draw_line(coord_list):
    lenList = len(coord_list)
    x_number_values = []
    y_number_values = []
    for i in range(0,lenList):
        x_number_values.append(coord_list[i][0])
        y_number_values.append(coord_list[i][1])
    plt.plot(x_number_values, y_number_values, 'o-' , linewidth=1)
    plt.title("Best Route", fontsize=8)
    plt.xlabel("x Coord", fontsize=8)
    plt.ylabel("y Coord", fontsize=8)
    plt.tick_params(axis='both', labelsize=8)
    #plt.ion()
    plt.show()


if __name__ == '__main__':
    def distance_callback(source_location, destination_location):
        return abs(source_location[0] - destination_location[0]) + \
               abs(source_location[1] - destination_location[1])
    start = (0,0)
    food_locations = {start}
    for i in range(0,30):
        food_locations.add((randint(0,200),randint(0,200)))

    draw_multiple_points(list(food_locations))
    colony = colony(food_locations, \
                    distance_callback,\
                    start, \
                    50, \
                    80, \
                    .5, \
                    1.2,  \
                    .40, \
                    1.0)
    colony.run()
    print("shortest path distance = " , colony.shortest_path_distance)
    print("colony shortest distance = " ,colony.shortest_path)
    draw_line(list(colony.shortest_path))
