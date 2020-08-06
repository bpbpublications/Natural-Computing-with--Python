import random
  
model = [1,1,1,1,1,9,9,9,9,9]  
length = 10  
num = 10  
pressure = 3  
mutation_chance = 0.2  
  
print("\n\nmodel: %s\n"%(model))  
  
def individual(min, max):
    
    return[random.randint(min, max) for i in range(length)]
  
def population():
   
    return [individual(1,9) for i in range(num)]
  
def fitness(individual):
   
    fitness = 0
    for i in range(len(individual)):
        if individual[i] == model[i]:
            fitness += 1
  
    return fitness
  
def selection_and_reproduction(population):
   
    value = [ (fitness(i), i) for i in population]  
    value = [i[1] for i in sorted(value)]  
    population = value
    selected =  value[(len(value)-pressure):]    
  
  
    for i in range(len(population)-pressure):
        point = random.randint(1,length-1)  
        father = random.sample(selected, 2)  
        population[i][:point] = father[0][:point]  
        population[i][point:] = father[1][point:]
  
    return population  
  
def mutation(population):

    for i in range(len(population)-pressure):
        if random.random() <= mutation_chance:  
            point = random.randint(0,length-1)  
            new_value = random.randint(1,9)  
  
            while new_value == population[i][point]:
                new_value = random.randint(1,9)
  
            population[i][point] = new_value
  
    return population
      
  
  
population = population()
print("Initial Population:\n%s"%(population))  
  
  
for i in range(1000):
    population = selection_and_reproduction(population)
    population = mutation(population)
  
  
print("\nFinal Population:\n%s"%(population))  
print("\n\n")
