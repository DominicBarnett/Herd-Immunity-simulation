import random
from virus import Virus


class Person(object):
    def __init__(self, _id, is_vaccinated, infection = None):
        self._id = _id  # int
        self.is_vaccinated = is_vaccinated
        self.infection = infection
        self.is_alive = True

    def did_survive_infection(self):
        if self.infection is not None:
            if random.random() < self.infection.mortality_rate:
                self.is_alive = False
            else:
                self.is_vaccinated = True
                self.infection = None
        return self.is_alive

if __name__ == '__main__':
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None


    unvaccinated_person = Person(2, False)

    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None

    virus = Virus('Dysentery', 0.7, 0.2)

    infected_person = Person(3, False, virus)

    assert infected_person._id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert infected_person.infection is virus

    people = []
    for i in range(1, 100):
        people.append(Person(i, False, virus))


    for person in people:
        survived = person.did_survive_infection()

   
    did_survive = 0
    did_not_survive = 0

    for person in people:
        if person.did_survive_infection():
            did_survive += 1
        else:
            did_not_survive += 1

    print(f'People who survived: {did_survive}')
    print(f'People who did not survive: {did_not_survive}\n')

    # Additional test 1
    virus1 = Virus('HIV', 0.8, 0.3)

    uninfected_people1 = []
    became_infected1 = 0
    became_vaccinated1 = 0

    for i in range(1, 100):
        uninfected_people1.append(Person(i, False))

    for person in uninfected_people1:
        if random.random() < virus1.repro_rate:
            person.infection = virus1
            became_infected1 += 1
        else:
            became_vaccinated1 += 1

    print(f'People who became infected: {became_infected1}')
    print(f'Virus infection rate out of 100: {int(virus1.repro_rate * 100)}')
    print(f'People who became vaccinated: {became_vaccinated1}\n')

    # Additional test 2
    virus2 = Virus('Ebola', 0.4, 0.9)

    uninfected_people2 = []
    became_infected2 = 0
    became_vaccinated2 = 0

    for i in range(1, 100):
        uninfected_people2.append(Person(i, False))

    for person in uninfected_people2:
        if random.random() < virus2.repro_rate:
            person.infection = virus2
            became_infected2 += 1
        else:
            became_vaccinated2 += 1

    print(f'People who became infected: {became_infected2}')
    print(f'Virus infection rate out of 100: {int(virus2.repro_rate * 100)}')
    print(f'People who became vaccinated: {became_vaccinated2}\n')


    # Additional test 3
    virus3 = Virus('Covid', 0.6, 0.2)

    uninfected_people3 = []
    became_infected3 = 0
    became_vaccinated3 = 0

    for i in range(1, 100):
        uninfected_people3.append(Person(i, False))

    for person in uninfected_people3:
        if random.random() < virus3.repro_rate:
            person.infection = virus3
            became_infected3 += 1
        else:
            became_vaccinated3 += 1

    print(f'People who became infected: {became_infected3}')
    print(f'Virus infection rate out of 100: {int(virus3.repro_rate * 100)}')
    print(f'People who became vaccinated: {became_vaccinated3}')
