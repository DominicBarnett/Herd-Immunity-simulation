from simulation import Simulation
from person import Person
from logger import Logger
from virus import Virus

if __name__ == '__main__':
    virus_name = 'Sniffles'
    repro_num = 0.5
    mortality_rate = 0.12
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10


    # Test Virus
    virus = Virus(virus_name, repro_num, mortality_rate)

    # assert virus.name == 'Sniffles'
    # assert virus.repro_rate == 0.5
    # assert virus.mortality_rate == 0.12
    # virus1 = Virus('Ebola', 0.4, 0.9)
    # assert virus1.name == 'Ebola'
    # assert virus1.repro_rate == 0.4
    # assert virus1.mortality_rate == 0.9
    virus2 = Virus('Covid', 0.6, 0.2)
    assert virus2.name == 'Covid'
    assert virus2.repro_rate == 0.6
    assert virus2.mortality_rate == 0.2
    # Test Simulation
    sim = Simulation(virus2, pop_size, vacc_percentage, initial_infected)

    assert sim.pop_size == 1000
    assert sim.vacc_percentage == 0.1
    assert sim.initial_infected == 10

    # Test that values are changed/created after simulation
    sim.run()
    assert sim.pop_size != 1000
    assert sim.population != []
    assert sim.interaction_count != 0