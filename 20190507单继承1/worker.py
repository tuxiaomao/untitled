from person import Person

class Worker(Person):
    def __init__(self, name, age, money):
        super(Worker, self).__init__(name, age, money)