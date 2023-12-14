class Person:
    def __init__(self, Navn, Alder, telefon, Epost):
        self.Navn = Navn
        self.Alder = Alder
        self.telefon = telefon
        self.Epost = Epost

class Biletter(Person):
    def __init__(self, Navn, Alder, telefon, Epost, stykke:str, antallBiletter:int=1)
        super()__init__(Navn, Alder, telefon, Epost)
        self.stykke = stykke
        self.antallBiletter = antallBiletter
