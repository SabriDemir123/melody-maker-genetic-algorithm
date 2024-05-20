import random
import genetic_algorithm.notes as notes

class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate, max_generations):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.max_generations = max_generations
        self.population = self.initialize_population()

    def generate_random_melody(self, length=100):
        melody = []
        while len(melody) < length:
            # Extend the melody with a random building block
            block = random.choice(notes.building_blocks)
            melody.extend(block)
        return melody[:length]
    
    def initialize_population(self):
        # Generate a random melody for each individual in the population
        return [self.generate_random_melody() for _ in range(self.population_size)]
    
    def fitness(self, melody):
        duration_variety = len(set(duration for _, duration in melody))
        note_variety = len(set(note for note, _ in melody))
        note_scale_matches = sum(note[:-1] in notes.c_major_scale for note, _ in melody)
        rhythmic_diversity = len(set(duration for _, duration in melody))

        repetition_penalty = -sum(melody[i] == melody[i + 1] for i in range(len(melody) - 1))

        return duration_variety + note_variety + note_scale_matches + rhythmic_diversity + repetition_penalty


    def selection(self, population, fitnesses):
        # Select the two individuals with the highest fitness
        best_indices = sorted(range(len(fitnesses)), key=lambda i: fitnesses[i], reverse=True)[:2]
        return [population[i] for i in best_indices]
    
    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, len(parent1) - 1)
        # Perform single-point crossover
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2
    
    def mutate(self, melody):
        # Mutate a building block
        if random.random() < self.mutation_rate:
            block = random.choice(notes.building_blocks)
            index = random.randint(0, len(melody) - len(block))
            melody[index:index+len(block)] = block
        # Mutate a single note
        if random.random() < self.mutation_rate:
            index = random.randint(0, len(melody) - 1)
            melody[index] = (random.choice(notes.random_note), random.choice(notes.random_duration))
        return melody

    def change_octave(self, melody, replacement):
        modified_melody = []
        # Replace the octave of each note in the melody with the replacement to create a bass melody
        for note, duration in melody:
            note = ''.join([replacement if char.isdigit() else char for char in note])
            modified_melody.append((note, duration))
        return modified_melody
    
    def run(self):
        # Run the genetic algorithm for a fixed number of generations
        for _ in range(self.max_generations):
            # Evaluate the fitness of each individual in the population
            fitnesses = [self.fitness(melody) for melody in self.population]

            new_population = list()
            # Create new population
            while len(new_population) < self.population_size:
                # Select parents with the highest fitness
                parents = self.selection(self.population, fitnesses)
                # Create offspring by unpacking the parents
                offspring = self.crossover(*parents)
                # Add offspring to the new population
                new_population.extend(self.mutate(child) for child in offspring)

            # Replace the old population with the new one
            self.population = new_population[:self.population_size]
        
        best_melody = self.population[fitnesses.index(max(fitnesses))]
        bass_melody = self.change_octave(best_melody, '2')

        return best_melody, bass_melody