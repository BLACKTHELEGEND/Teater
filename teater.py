class Person:
    def __init__(self, Navn, Alder, telefonNr, Epost):
        self.Navn = Navn
        self.Alder = Alder
        self.telefonNr = telefonNr
        self.Epost = Epost

class Biletter(Person):
    def __init__(self, Navn, Alder, telefonNr, Epost, stykke:str, antallBiletter:int=1):
        super().__init__(Navn, Alder, telefonNr, Epost)
        self.stykke = stykke
        self.antallBiletter = antallBiletter 



class Person: 
    def __init__(self, navn, adresse, telefon, epost, alder, student=False):
        self.navn = navn
        self.adresse = adresse
        self.telefon = telefon
        self.epost = epost
        self.alder = alder
        self.student = student
        self.billetter = []

    def get_rabatt(self):
        if self.alder > 67:
            return 0.3
        elif self.student:
            return 0.2
        elif self.alder < 10:
            return 0.5
        else:
            return 0

class Billett:
    def __init__(self, forestilling, kjoper):
        self.forestilling = forestilling
        self.kjoper = kjoper
        self.pris = 300 * (1 - kjoper.get_rabatt())

class Forestilling:
    def __init__(self, stykke, dato):
        self.stykke = stykke
        self.dato = dato
        self.billetter = []

    def legg_til_billett(self, kjoper):
        if len(self.billetter) < self.stykke.sal.kapasitet:
            self.billetter.append(Billett(self, kjoper))
        else:
            print("Beklager, denne forestillingen er utsolgt.")

class Stykke:
    def __init__(self, navn, sal):
        self.navn = navn
        self.sal = sal
        self.forestillinger = []

class Sal:
    def __init__(self, navn, kapasitet):
        self.navn = navn
        self.kapasitet = kapasitet
