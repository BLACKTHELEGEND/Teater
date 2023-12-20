import datetime
import it#Dette er en biblotek fra min folder, hvor jeg f.eks hener ut funksjonen riktigInputInt_float_eller_int()
from pick import pick
import time
import os

os.system('cls')

class Person:
    def __init__(self, navn, alder, telefonNr, epost, adresse):
        self.navn = navn
        self.alder = alder
        self.telefonNr = telefonNr
        self.epost = epost
        self.adresse = adresse

class Bilett(Person):
    def __init__(self, navn:str, alder:int, telefonNr:int, epost:str,adresse:str, stykke:str, dato:str, erStudent:str = 'nei',antallBilett:int=1):
        super().__init__(navn, alder, telefonNr, epost, adresse)
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
            return self.ordinarPris*rabatt
        
            
    
    def visKvittering(self):
        return f'Biletten under {self.navn} er følgende:\n\tNavn: {self.navn}\n\tAlder: {self.alder} år\n\tTelefon nummer: {self.telefonNr}\n\tEpost: {self.epost}\n\tStykke: {self.stykke}\n\tDato: {self.dato}\n\tAntall bilett: {self.antallBilett}\n\tTotal pris: {self.pris} kr\n'

class GruppeBilett(Bilett):
    def __init__(self, navn:str, alder:int, telefonNr:int, epost:str,adresse, stykke:str, dato:str, erStudent:str = 'nei',antallBilett:int=1):
        super().__init__(navn, alder, telefonNr, epost,adresse,stykke,dato,erStudent,antallBilett)
        self.pris = 0

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
        return pris


class Sal:
    def __init__(self, salNavn, stykke, antallPlasser) -> None:
        self.salNavn = salNavn
        self.stykke = stykke
        self.antallPlasser = antallPlasser


class Teater:
    Datoer = []
    for i in range(14):
        Datoer.append(datetime.date(2024,2,1)+datetime.timedelta(i))
    print(Datoer[3].strftime('%A'))


    Gold = Sal('Gold','De elendige',150)
    Sølv = Sal('Sølv','Vilanden',100)

    antallPlasserIgjenGold = [150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150]
    antallPlasserIgjenSølv = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100] 
    def __init__(self):
        self.bestilinger = []

    
    def legTilBestiling(self, navn, alder, telefonNr, epost,adresse, stykke: str, dato: str,erStudent:str='nei', antallBilett: int = 1):

        alder = alder
        datoIndex = Teater.Datoer.index(dato)

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
            self.bestilinger.append(GruppeBilett(navn, alder, telefonNr,epost,adresse,stykke,dato,erStudent,antallBilett))
        elif antallBilett == 1:
            self.bestilinger.append(Bilett(navn, alder, telefonNr,epost,adresse,stykke,dato,erStudent))
    
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

while True:
    #Denne delen skal da imitate en "meny" på en nettside go kunden kan da navigerer til ønsket funksjon og (Annet kan være f.eks: vis antall plasser det er på hver stykke i datoen fremover eller noe sånnt)
    titleHoved = 'Meny: '
    menyInnhold = ['Leggtil bestilling', 'Vis kvitering', 'Annet']
    menyvalgt, index = pick(menyInnhold, titleHoved, indicator='=>', default_index=0)

    #Hvis kunden velger leggtil bestiling så kan de leggtil en bestiling
    if menyvalgt == 'Leggtil bestilling':
        while True:
            title = 'Ønsker du å registrer en ny bestilling: '
            options = ['Ja', 'Nei']
            option, index = pick(options, title, indicator='=>', default_index=0)

            if option == options[0]:
                print('Registrere din bestilling:')
                navn = input('\tNavn: ')
                alder = it.riktigInputInt_float_eller_int('int','\tAlder','Alder ikke godskjent, husk det må være hel tall! Prøv igjen.', 0,None)

                telefonNr = it.riktigInputInt_float_eller_int('int','\tTelefon nummer','Nummer ikke godskjent, husk det må være hel tall! Prøv igjen.', 0,None)

                epost = input('\tepost: ')
                adresse = input('\tAdresse: ')

                if 18<=alder and alder <=35:
                    erStudent, erStudentIndex = pick(['Ja','Nei'],'Er du en stuent?:')
                
                #henter inn antall bileter kunden ønsker å kjøpe
                antallBilett = it.riktigInputInt_float_eller_int('int','Hvor mange biletter ønsker du å bestille','Kunn heltall er godskjent. Prøv igjen',1,150)

                #henter inn stykke kunden ønsker å se, her vil det være en droppdown
                valgStykkListe = ['\tDe elendige', '\tVilanden']
                valgStykke, stykkeIndex = pick(valgStykkListe, '\tVelg stykke du ønsker å se: ', indicator='=>', default_index=0)
                valgStykke = valgStykke[1:len(valgStykke)-1]

                #viser datoenen som det er mulig å se stykke på, denne listen med valg ekskluderer søndager
                tilgjenligeDatoer = []
                for i in range(14):
                    if (datetime.date(2024,2,1)+datetime.timedelta(i)).strftime('%A') != 'Sunday':
                        tilgjenligeDatoer.append(datetime.date(2024,2,1)+datetime.timedelta(i))

                valgtDato, datoIndex = pick(tilgjenligeDatoer,'Dato vi har tilgjenlige framover:','=>',default_index=0)

                #Denne delen har kunn et mål å det er å regne ut prisen kunden betaler både hvis det er gruppe betilling eller individuel bestiling
                if antallBilett>1:
                    gruppe1 = GruppeBilett(navn,alder,telefonNr,epost,adresse,valgStykke,valgtDato,erStudent,antallBilett)
                    pris = gruppe1.bergnPris()
                    os.system('cls')
                else:
                    bestilling1 = Bilett(navn,alder,telefonNr,epost,adresse,valgStykke,valgtDato,erStudent)
                    pris = bestilling1.bergnPris()
                    
                """Denne delen outputer informasjonen kunden har gitt (og her får kunden muligheten til å se gjenom informasjonen å evnetuelt endre på det: Denne delen er ikke gjort ennda)"""
                tekst2 = f'Du har gitt følgende informasjone:\n\tNavn: {navn}\n\tAlder: {alder} år\n\tEpost: {epost}\n\tStykke: {valgStykke}\n\tDato: {valgtDato}, {valgtDato.strftime("%A")}\nStemmer informasjonen'
                valgt, valgtIndex = pick(['Ja','Nei'],tekst2,'=>',default_index=0)

                #Her går koden videre med å registrerer kjøpet hvis kunden godskjener at informasjonen stemmer eller (få muligheten til å endre på det i: if valgt == 'Nei': Denne delen er heler ikke gjort ennå)
                if valgt == 'Ja':
                    if antallBilett>1:
                        Teater1.legTilBestiling(navn,alder,telefonNr,epost,adresse,valgStykke,valgtDato,erStudent,antallBilett)
                        Teater1.bestilinger[-1].pris = pris
                    else:
                        Teater1.legTilBestiling(navn,alder,telefonNr,epost,adresse,valgStykke,valgtDato,erStudent)
                        Teater1.bestilinger[-1].pris = pris
                    print('Takk for din bestiling den er lagt inn.')    
                    time.sleep(3)
                    os.system('cls')
            elif option == options[1]:
                break
    #Hvis kunden velger vis kvitering så kan de søke etter sin egen kvitering via telefonnummer men her er det sikket andre tryggerer måter å søke på???
    elif menyvalgt == 'Vis kvitering':
        while True:
            telefonNr = it.riktigInputInt_float_eller_int('int','Hvilket telfon nummer er kviteringen registrert på','Nummer ikke godskjent, husk det må være hel tall! Prøv igjen.', 0,None)
            alleKviteringer = ''
            for i in Teater1.bestilinger:
                if i.telefonNr == telefonNr:
                    alleKviteringer += i.visKvittering()

            valger2 = ['Ferdig', 'Finn ny kvitering']
            valgt2, valgtIndex2 = pick(valger2,alleKviteringer,'=>',default_index=0)

            if valgt2 == 'Ferdig':
                os.system('cls')
                break
            elif valgt2 == 'Finn ny kvitering':
                os.system('cls')
                continue
        


        """
        datoMånde = it.riktigInputInt_float_eller_int('int','\tVelg månde','Ikke godsjent input, husk det er 12 månder i året så intervall tillat [1,12]. Prøv igjen.',1,12)
        månder = ['Januar','Februar','Mars','April','Mai','Juni','Juli','August','September','Oktober','November','Desember']
        datoDag = it.riktigInputInt_float_eller_int('int',f'\tVelg dagsdatoen alså x\'en i (x,{månder[datoMånde-1]},2024): ','Ikke godsjent input, husk det er 28,30 eller 31 dager i en måned, basert på hvilken måned det er. Prøv igjen.',1,31)
        """


        



 
