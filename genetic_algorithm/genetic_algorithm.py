import random
import genetic_algorithm.notes as notes

class GeneticAlgorithm:
    def __init__(self, max_generations, population_size, mutation_rate, elitism_rate, melody_length):
        self.max_generations = max_generations
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.elitism_rate = elitism_rate
        self.melody_length = melody_length

        self.best_fitnesses = list()

        self.population = self.initialize_population()

    def generate_random_melody(self):
        melody = []
        while len(melody) < self.melody_length:
            # Extend the melody with a random building block
            block = random.choice(notes.building_blocks)
            melody.extend(block)
        return melody[:self.melody_length]
    
    def initialize_population(self):
        # Generate a random melody for each individual in the population
        return [self.generate_random_melody() for _ in range(self.population_size)]
    
    def fitness(self, melody):
        duration_variety = len(set(duration for _, duration in melody))
        note_variety = len(set(note for note, _ in melody))
        note_scale_matches = sum(note[:-1] in notes.c_major_scale for note, _ in melody)
        rhythmic_diversity = len(set(duration for _, duration in melody))

        repetition_penalty = -sum(melody[i] == melody[i + 1] for i in range(len(melody) - 1))

        rhythmic_patterning = sum(melody[i:i+3] == melody[i+3:i+6] for i in range(len(melody) - 5))
        ending_stability = melody[-1][0][:-1] in ['c', 'e', 'g']

        contour_changes = sum(
            (notes.random_note.index(melody[i][0][0]) < notes.random_note.index(melody[i+1][0][0]) > notes.random_note.index(melody[i+2][0][0])) or
            (notes.random_note.index(melody[i][0][0]) > notes.random_note.index(melody[i+1][0][0]) < notes.random_note.index(melody[i+2][0][0]))
            for i in range(len(melody) - 2)
        )

        # Combining all aspects with appropriate weights
        fitness = (
            duration_variety * 1 + 
            note_variety * 2 + 
            note_scale_matches * 2 + 
            rhythmic_diversity * 1 + 
            repetition_penalty * 1 +
            rhythmic_patterning * 1 + 
            ending_stability * 2 + 
            contour_changes * 2
        )

        return fitness

    def selection(self, population, fitnesses):
        # Select the best individuals in the population based on their fitness
        best_indices = sorted(range(len(fitnesses)), key=lambda i: fitnesses[i], reverse=True)[:int(self.elitism_rate * self.population_size)]
        return [population[i] for i in best_indices]
    
    def crossover(self, parent1, parent2):
        if random.random() < self.mutation_rate:
            # Perform two-point crossover
            crossover_points = sorted(random.sample(range(1, len(parent1) - 1), 2))
            child1 = parent1[:crossover_points[0]] + parent2[crossover_points[0]:crossover_points[1]] + parent1[crossover_points[1]:]
            child2 = parent2[:crossover_points[0]] + parent1[crossover_points[0]:crossover_points[1]] + parent2[crossover_points[1]:]
            return child1, child2
        
        return parent1, parent2
    
    def mutate(self, melody):
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

            new_population = self.selection(self.population, fitnesses)
            # Create new population
            while len(new_population) < self.population_size:
                # Select two parents from the elite population
                parents = random.choices(self.population, weights = fitnesses, k = 2)
                # Create offspring by unpacking the parents
                offspring = self.crossover(*parents)
                # Add offspring to the new population
                new_population.extend(self.mutate(child) for child in offspring)

            # Replace the old population with the new one
            self.population = new_population[:self.population_size]
            # Store the best fitness of the current generation
            self.best_fitnesses.append(max(fitnesses))
        
        best_melody = self.population[fitnesses.index(max(fitnesses))]
        bass_melody = self.change_octave(best_melody, '2')

        return best_melody, bass_melody