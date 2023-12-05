class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name
 

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        log = open(self.file_name, 'w')
        log.write(f'Population Size: {pop_size}\n'
                        f'Vaccination Percentage: {vacc_percentage}\n'
                        f'Virus Name: {virus_name}\n'
                        f'Mortality Rate: {mortality_rate}\n'
                        f'Basic Reproduction Number: {basic_repro_num}\n'
        )
        log.close()

    def log_interactions(self, number_of_fatalities, number_of_new_infections):
        log = open(self.file_name, 'a')
        log.write(f'\nNumber of New Infections: {number_of_new_infections}\n'
                            f'Number of New Deaths: {number_of_fatalities}\n')
        log.close()

    def log_infection_survival(self, population_count, number_of_new_fatalities, number_of_vaccinations):
        log = open(self.file_name, 'a')
        log.write('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                            f'\nCurrent Population Count: {population_count}\n'
                            f'Total Number of Deaths: {number_of_new_fatalities}\n'
                            f'Total Number of Vaccinations Administered: {number_of_vaccinations}\n\n\n')
        log.close()

    def log_time_step(self, time_step_number):
        log = open(self.file_name, 'a')
        log.write('\n\n----------------------------\n'
                            f'Time Step Number: {time_step_number}'
                            '\n----------------------------\n')
        log.close()

    def end_of_sim_stats(self, surivor_count, fatality_count, total_vaccinated_count, reason_for_ending, interaction_count, new_vaccinated_count, newly_infected_count, initial_population, vaccine_saves):
        log = open(self.file_name, 'a')
        log.write('-~-~-~-~-~-~-~-~-~-~-~-~-~-\n'
                            f'\nNumber of Survivors: {surivor_count}\n'
                            f'Total Number of Deaths: {fatality_count}\n'
                            f'Total Number of Vaccinations: {total_vaccinated_count}\n'
                            f'Reason for Simulation Ending: {reason_for_ending}\n'
                            f'Total Number of Interactions: {interaction_count}\n'
                            f'Newly Vaccinated Count: {new_vaccinated_count}\n'
                            f'Perecentage of Population That Became Infected: {round(newly_infected_count / initial_population * 100, 2)}%\n'
                            f'Perecentage of Population That Died: {round(fatality_count / initial_population * 100, 2)}%\n'
                            f'Number of Lives Saved by Vaccinations: {vaccine_saves}\n')
        log.close()