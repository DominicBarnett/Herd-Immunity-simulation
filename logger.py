class Logger(object):
    def __init__(self, file_name):
        # TODO:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name
    # The methods below are just suggestions. You can rearrange these or 
    # rewrite them to better suit your code style. 
    # What is important is that you log the following information from the simulation:
    # Meta data: This shows the starting situtation including:
    #   population, initial infected, the virus, and the initial vaccinated.
    # Log interactions. At each step there will be a number of interaction
    # You should log:
    #   The number of interactions, the number of new infections that occured
    # You should log the results of each step. This should inlcude: 
    #   The population size, the number of living, the number of dead, and the number 
    #   of vaccinated people at that step. 
    # When the simulation concludes you should log the results of the simulation. 
    # This should include: 
    #   The population size, the number of living, the number of dead, the number 
    #   of vaccinated, and the number of steps to reach the end of the simulation. 

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        # TODO: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        log = open(self.file_name, 'w')
        log.write(f'Population Size: {pop_size}\n'
                        f'Vaccination Percentage: {vacc_percentage}\n'
                        f'Virus Name: {virus_name}\n'
                        f'Mortality Rate: {mortality_rate}\n'
                        f'Basic Reproduction Number: {basic_repro_num}\n'
        )
        log.close()

    def log_interactions(self, number_of_fatalities, number_of_new_infections):
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        log = open(self.file_name, 'a')
        log.write(f'\nNumber of New Infections: {number_of_new_infections}\n'
                            f'Number of New Deaths: {number_of_fatalities}\n')
        log.close()

    def log_infection_survival(self, population_count, number_of_new_fatalities, number_of_vaccinations):
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
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