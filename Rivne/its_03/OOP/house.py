from person import Person

class House:

    def __init__(self, addr):
        self.__address = addr
        self.__residents = ['n/a']

    def set_address(self, addr):
        self.__address = addr

    def address(self):
        return self.__address

    def settle(self, p):
        if isinstance(p, Person):
            self.__residents.append(p)
            p.set_address(self.__address)

    def eviction(self, p):
        if isinstance(p, Person):
            self.__residents.pop(p)
            p.set_address = 'n/a'

    def show_residents(self):
        print('---------------------------')
        print('# Residents: ')
        for p in self.__residents:
            if isinstance(p, Person):
                print(f'# - {p._name}')
