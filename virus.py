class Virus(object):
    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate


# Test this class
if __name__ == '__main__':
    virus = Virus('HIV', 0.8, 0.3)
    assert virus.name == 'HIV'
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3


    # Additional test 1:
    virus1 = Virus('Ebola', 0.4, 0.9)
    assert virus1.name == 'Ebola'
    assert virus1.repro_rate == 0.4
    assert virus1.mortality_rate == 0.9


    # Additional test 2:
    virus2 = Virus('Covid', 0.6, 0.2)
    assert virus2.name == 'Covid'
    assert virus2.repro_rate == 0.6
    assert virus2.mortality_rate == 0.2
