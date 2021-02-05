class Computer():
    def __init__(self, serie, ram, rom):
        self.serie = serie
        self.ram = ram
        self.rom = rom
    
    def getspecs(self):
        print('insert specs...')
        self.serie = input('Enter serie: ')
        self.ram = input('Enter ram: ')
        self.rom = input('Enter rom: ')
    
    def displayspecs(self):
        print('This is a computer...')
        print('Serie: ',self.serie)
        print('Ram: ',self.ram)
        print('Rom: ',self.rom)

class Desktop(Computer):

    def __init__(self, weight):
        self.weight = weight

    def set_weight(self):
        self.weight = input('Enter weight: ')

class Laptop(Computer):

    def __init__(self, casecolor):
        self.casecolor = casecolor

    def set_casecolor(self):
        self.casecolor = input('Enter casecolor: ')

Compu1 = Laptop('')
Compu1.getspecs()
Compu1.set_casecolor()
Compu1.displayspecs()

Compu2 = Desktop('')
Compu2.getspecs()
Compu2.set_weight()
Compu2.displayspecs()