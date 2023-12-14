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
