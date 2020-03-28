<<<<<<< HEAD


class Adventurer():
    def __init__(self, name, job):
        self.name = name
=======
from job import Apprentice


class Adventurer(Apprentice):
    def __init__(self, name):
        self.userName = name
        self.item = {}
        self.job = Apprentice.__init__()
>>>>>>> 8dac46c14b71ecfad25c86ef7b7e2b37b4dadce8
