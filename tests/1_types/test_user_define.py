class Worker:
    def __init__(self, name, pay): # Constructor
        self.name = name
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay *= (1.0 + percent)


class TestUserDefinedObjects:
    def test_custom_object(self):
        sue = Worker('Sue Jones', 60000)
        assert sue.last_name() == 'Jones'
        assert sue.pay == 60000
        sue.give_raise(10)
        assert sue.pay == 660000.0

