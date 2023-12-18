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



#Version 2

import datetime

class Person:
    def __init__(self, navn, alder, telefonNr, epost):
        self.navn = navn
        self.alder = alder
        self.telefonNr = telefonNr
        self.epost = epost

class Bilett(Person):
    def __init__(self, navn:str, alder:int, telefonNr:int, epost:str, stykke:str, dato:str, erStudent:str = 'nei',antallBilett:int=1):
        super().__init__(navn, alder, telefonNr, epost)
        self.ordinarPris = 300
        self.antallBilett = antallBilett
        self.dato = dato
        self.erStudent = erStudent
        self.stykke = stykke
        self.pris = 0


    def bergnPris(self):
        if self.antallBilett == 1:
            rabatt = 1
            if self.alder < 10:
                rabatt -= 0.5
            elif self.alder > 67:
                rabatt -= 0.3
            elif self.erStudent == 'ja':
                rabatt -=0.2
            
            self.pris = self.ordinarPris*rabatt
            return self.pris
        elif self.antallBilett > 1:
            pris = 0

            rabattP = 1
            if self.alder < 10:
                rabattP -= 0.5
            elif self.alder > 67:
                rabattP -= 0.3
            elif self.erStudent == 'ja':
                rabattP -=0.2
            pris += self.ordinarPris*rabattP

            for i in range(2,self.antallBilett+1):
                Alder_erStudent = int(input(f'Hei skriv alderen til person{i}: '))
                rabatt = 1
                if Alder_erStudent < 10:
                    rabatt -= 0.5
                elif Alder_erStudent > 67:
                    rabatt -= 0.3
                pris += self.ordinarPris*rabatt
            self.pris = pris
            return self.pris
    
    def visKvittering(self):
        print(f'Biletten under {self.navn} er følgende:\n\tNanv: {self.navn}\n\tAlder: {self.alder}\n\tStykke: {self.stykke}\n\tDato: {self.dato}\n\tAntall bilett: {self.antallBilett}\n\tTotal pris: {self.bergnPris()}')

class GruppeBilett(Bilett):
    def __init__(self, navn:str, alder:int, telefonNr:int, epost:str, stykke:str, dato:str, erStudent:str = 'nei',antallBilett:int=1):
        super().__init__(navn, alder, telefonNr, epost,stykke,dato,erStudent,antallBilett)
        self.pris = GruppeBilett.totPris


    def bergnPris(self):
            pris = 0

            rabattP = 1
            if self.alder < 10:
                rabattP -= 0.5
            elif self.alder > 67:
                rabattP -= 0.3
            elif self.erStudent == 'ja':
                rabattP -=0.2
            pris += self.ordinarPris*rabattP

            for i in range(2,self.antallBilett+1):
                Alder_erStudent = int(input(f'Hei skriv alderen til person{i}: '))
                rabatt = 1
                if Alder_erStudent < 10:
                    rabatt -= 0.5
                elif Alder_erStudent > 67:
                    rabatt -= 0.3
                pris += self.ordinarPris*rabatt
            GruppeBilett.totPris = pris
            return self.pris
    
    def visKvittering(self):
        print(f'Biletten under {self.navn} er følgende:\n\tNanv: {self.navn}\n\tAlder: {self.alder}\n\tStykke: {self.stykke}\n\tDato: {self.dato}\n\tAntall bilett: {self.antallBilett}\n\tTotal pris: {self.bergnPris()}')


class Sal:
    def __init__(self, salNavn, stykke, antallPlasser) -> None:
        self.salNavn = salNavn
        self.stykke = stykke
        self.antallPlasser = antallPlasser


class Teater(Bilett):
    Datoer = []
    for i in range(15):
        Datoer.append(datetime.date(2024,2,1)+datetime.timedelta(i))
    print(Datoer[14].strftime('%A'))


    Gold = Sal('Gold','De elendige',150)
    Sølv = Sal('Sølv','Vilanden',100)

    antallPlasserIgjenGold = [150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150]
    antallPlasserIgjenSølv = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100] 
    def __init__(self):
        self.bestilinger = []

    
    def legTilBestiling(self, navn, alder, telefonNr, epost, stykke: str, dato: str,erStudent:str='nei', antallBilett: int = 1):

        alder = alder
        datoSplit = dato.split(',')
        datoIndex = Teater.Datoer.index(datetime.date(int(datoSplit[0]),int(datoSplit[1]),int(datoSplit[2])))

        if(stykke == Teater.Gold.stykke):
            if Teater.antallPlasserIgjenGold[datoIndex]-antallBilett >= 0:
                Teater.antallPlasserIgjenGold[datoIndex]-= antallBilett
            else:
                print('ikke mer tilgjenlig plass i tilhørende sal denne datoen')
                return 
        elif(stykke == Teater.Sølv.stykke):
            if Teater.antallPlasserIgjenSølv[datoIndex]-antallBilett >= 0:
                Teater.antallPlasserIgjenSølv[datoIndex]-= antallBilett
            else:
                print('ikke mer tilgjenlig plass i tilhørende sal denne datoen')
                return 
        
        if(antallBilett>1):
            self.bestilinger.append(GruppeBilett(navn, alder, telefonNr,stykke, epost, dato,stykke, antallBilett))
        elif antallBilett == 1:
            self.bestilinger.append(Bilett(navn, alder, telefonNr,stykke, epost, dato,stykke, antallBilett))
    
    def visAntallPlasserIgjen(self, sal:str):
        if sal.capitalize() == 'Gull':
            print(Teater.antallPlasserIgjenGold)
        if sal.capitalize() == 'Sølv':
            print(Teater.antallPlasserIgjenGold)
    
    def totaltTjent(self):
        tjent = 0
        for i in range(len(self.bestilinger)):
            tjent+=self.bestilinger[i].bergnPris()
        return tjent
    
Teater1 = Teater()
Teater1.legTilBestiling('Yonatan Moknen', 18, 48342012, 'Nanikanblidet@gmail.com', 'De elendige', '2024,02,05')
print(Teater1.bestilinger[0].visKvittering())
print(Teater1.antallPlasserIgjenGold())

