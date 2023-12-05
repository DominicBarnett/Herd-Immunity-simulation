import random, math
# random.seed(42)
from datetime import date
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        self.logger = Logger(f'{virus.name}_log_file.txt')
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_vaccination_count = math.floor(self.pop_size * self.vacc_percentage)
        self.array_of_infected = []
        self.initial_infected = initial_infected
        self.population = self._create_population()
        self.vaccination_count = 0
        self.newly_infected = []
        self.newly_dead = []
        self.interaction_count = 0
        self.vaccine_saves = 0



    def _create_population(self):
        population_list = []

        for i in range(0, self.pop_size):
            population_list.append(Person(i, False))
        for i in range(0, (self.initial_vaccination_count)):
            population_list[i].is_vaccinated = True
        for i in range(0, (self.initial_infected)):
            population_list[i].infection = self.virus
        return population_list
        

    def _simulation_should_continue(self):
        for person in self.population:
            if person.is_alive and not person.is_vaccinated:
                return True
        return False

    def run(self):
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate, date.today().strftime('%Y-%m-%d'))

        time_step_counter = 0
        should_continue = True

        while should_continue:
            time_step_counter += 1
            self.time_step(time_step_counter)
            should_continue = self._simulation_should_continue()
        
        fatality_count = len(self.population) - self.pop_size
        infected_count = 0

        for person in self.population:
            if person.infection != None:
                infected_count += 1

        newly_infected_count = infected_count - self.initial_infected
        total_vaccination_count = self.vaccination_count + self.initial_vaccination_count
        reason_for_ending = 'The entire population has died.' if fatality_count == len(self.population) else 'All living people have been vaccinated.'
        self.logger.end_of_sim_stats(self.pop_size, fatality_count, total_vaccination_count, reason_for_ending, self.interaction_count, self.vaccination_count, newly_infected_count, len(self.population), self.vaccine_saves)


    def time_step(self, time_step_counter):
        self.logger.log_time_step(time_step_counter)
        for person in self.population:
            if person.infection != None and person.is_alive:
                for i in range(0, 100):
                    random_person = random.choice(self.population)
                    while not random_person.is_alive:
                        random_person = random.choice(self.population)
                    self.interaction(person, random_person)
        self._infect_newly_infected()
        fatality_count = len(self.population) - self.pop_size
        self.logger.log_interactions(len(self.newly_infected), len(self.newly_dead))
        self.newly_infected = []
        self.newly_dead = []
        self.logger.log_infection_survival(self.pop_size, fatality_count, self.vaccination_count)


    def interaction(self, infected_person, random_person):
        self.interaction_count += 1
        if random_person.infection is None and not random_person.is_vaccinated:
            if random.random() < self.virus.repro_rate:
                self.newly_infected.append(random_person)


    def _infect_newly_infected(self):
        for person in self.newly_infected:
            person.infection = self.virus
            if person.did_survive_infection():
                self.vaccination_count += 1
                person.is_vaccinated = True
                self.vaccine_saves += 1
            else:
                person.is_alive = False
                self.pop_size -= 1
                self.newly_dead.append(person)


if __name__ == '__main__':
    # Test your simulation here
    virus_name = 'Sniffles'
    repro_num = 0.5
    mortality_rate = 0.12

    # Set some values used by the simulation
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10

    # Make a new instance of the simulation
    virus = Virus(virus_name, repro_num, mortality_rate)
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    sim.run()
