import datetime
import it 
from pick import pick
import time
import os
import pywhatkit
import json
import re
import random

os.system('cls')
 
 


#Person classe
class Person:
    def __init__(self, navn, alder, telefonNr, epost, adresse):
        self.navn = navn
        self.alder = alder
        self.telefonNr = telefonNr
        self.epost = epost
        self.adresse = adresse

#Bilett classe
class Bilett(Person):
    def __init__(self, navn:str, alder:int, telefonNr:int, epost:str,adresse:str, stykke:str, dato:str,sete, erStudent:str = 'nei',antallBilett:int=1):
        super().__init__(navn, alder, telefonNr, epost, adresse)
        self.ordinarPris = 300
        self.antallBilett = antallBilett
        self.dato = dato
        self.sete = sete
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
        elif self.antallBilett>1:
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
                Alder_erStudent = int(input(f'\tAlderen {i}.person: '))
                rabatt = 1
                if Alder_erStudent < 10:
                    rabatt -= 0.5
                elif Alder_erStudent > 67:
                    rabatt -= 0.3
                pris += self.ordinarPris*rabatt
            return pris
        
            
    
    def visKvittering(self):
        return f'Biletten under {self.navn} er følgende:\n\tNavn: {self.navn}\n\tAlder: {self.alder} år\n\tTelefon nummer: {self.telefonNr}\n\tEpost: {self.epost}\n\tStykke: {self.stykke}\n\tDato: {self.dato}\n\tAntall bilett: {self.antallBilett}\n\tTotal pris: {self.pris} kr\n'
        

#Sal klasse
class Sal:
    def __init__(self, salNavn, stykke, antallPlasser) -> None:
        self.salNavn = salNavn
        self.stykke = stykke
        self.antallPlasser = antallPlasser

Gold = Sal('Gold','De elendige',150)
Sølv = Sal('Sølv','Vildanden',100)

class Teater:
    Datoer = []
    for i in range(14):
        if (datetime.date(2024,2,1)+datetime.timedelta(i)).strftime('%A') != 'Sunday':
            Datoer.append(f'{datetime.date(2024,2,1)+datetime.timedelta(i)}, {(datetime.date(2024,2,1)+datetime.timedelta(i)).strftime("%A")}')
        else:
            Datoer.append(f'{datetime.date(2024,2,1)+datetime.timedelta(i)}, {(datetime.date(2024,2,1)+datetime.timedelta(i)).strftime("%A")}: stengt')


    Gold = Sal('Gold','De elendige',150)
    Sølv = Sal('Sølv','Vildanden',100)

    antallPlasserIgjenGull = [150, 150, 150, 's', 150, 150, 150, 150, 150, 150, 's', 150, 150, 150, 150]
    seterGull = [[],[],[],[],[]]
    fordeling = ['A', 'B', 'C', 'D', 'E']
    for i in range(5):
        for x in range(30):
            seterGull[i].append(f'{fordeling[i]}{x+1}')
    
    seterGullForAlleDager = [seterGull.copy(),seterGull.copy(),seterGull.copy(),'s',seterGull.copy(),seterGull.copy(),seterGull.copy(),seterGull.copy(),seterGull.copy(),seterGull.copy(),'s',seterGull.copy(),seterGull.copy(),seterGull.copy()]

    antallPlasserIgjenSølv = [100, 100, 100, 's', 100, 100, 100, 100, 100, 100, 's', 100, 100, 100, 100] 
    seterSølv = [[],[],[],[]]
    for i in range(4):
        for x in range(25):
            seterSølv[i].append(f'{fordeling[i]}{x+1}')
    
    seterSølvForAlleDager = [seterSølv.copy(),seterSølv.copy(),seterSølv.copy(),'s',seterSølv.copy(),seterSølv.copy(),seterSølv.copy(),seterSølv.copy(),seterSølv.copy(),seterSølv.copy(),'s',seterSølv.copy(),seterSølv.copy(),seterSølv.copy()]

    def __init__(self):
        self.bestilinger = []
        self.nyestePris = 0

    
    def legTilBestiling(self, navn, alder, telefonNr, epost,adresse, stykke: str, dato: str,sete,erStudent:str='nei', antallBilett: int = 1):

        alder = alder
        datoIndex = Teater.Datoer.index(dato)

        if(stykke == Teater.Gold.stykke):

            for i in range(len(sete)):
                if sete[i][0] == 'A':
                    Teater.seterGullForAlleDager[datoIndex][0].pop(Teater.seterGullForAlleDager[datoIndex][0].index(sete[i]))
                elif sete[i][0] == 'B':
                    Teater.seterGullForAlleDager[datoIndex][1].pop(Teater.seterGullForAlleDager[datoIndex][0].index(sete[i]))
                elif sete[i][0] == 'C':
                    Teater.seterGullForAlleDager[datoIndex][2].pop(Teater.seterGullForAlleDager[datoIndex][0].index(sete[i]))
                elif sete[i][0] == 'D':
                    Teater.seterGullForAlleDager[datoIndex][3].pop(Teater.seterGullForAlleDager[datoIndex][0].index(sete[i]))
                elif sete[i][0] == 'E':
                    Teater.seterGullForAlleDager[datoIndex][4].pop(Teater.seterGullForAlleDager[datoIndex][0].index(sete[i]))

            if Teater.antallPlasserIgjenGull[datoIndex]-antallBilett >= 0:
                Teater.antallPlasserIgjenGull[datoIndex]-= antallBilett
            else:
                print('ikke mer tilgjenlig plass i tilhørende sal denne datoen')
                return 
        elif(stykke == Teater.Sølv.stykke):
            for i in range(len(sete)):
                if sete[i][0] == 'A':
                    Teater.seterSølvForAlleDager[datoIndex][0].pop(Teater.seterSølvForAlleDager[datoIndex][0].index(sete[i]))
                elif sete[i][0] == 'B':
                    Teater.setersølvForAlleDager[datoIndex][1].pop(Teater.seterSølvForAlleDager[datoIndex][0].index(sete[i]))
                elif sete[i][0] == 'C':
                    Teater.setersølvForAlleDager[datoIndex][2].pop(Teater.seterSølvForAlleDager[datoIndex][0].index(sete[i]))
                elif sete[i][0] == 'D':
                    Teater.setersølvForAlleDager[datoIndex][3].pop(Teater.seterSølvForAlleDager[datoIndex][0].index(sete[i]))

            if Teater.antallPlasserIgjenSølv[datoIndex]-antallBilett >= 0:
                Teater.antallPlasserIgjenSølv[datoIndex]-= antallBilett
            else:
                print('ikke mer tilgjenlig plass i tilhørende sal denne datoen')
                return 
        
        
        self.bestilinger.append(Bilett(navn, alder, telefonNr,epost,adresse,stykke,dato,sete,erStudent,antallBilett)) 
        data = {'navn':navn, 'alder':alder, 'telefonNr':telefonNr,'epost':epost,'adresse':adresse,'stykke':stykke,'dato':f'{dato}','sete': sete,'erStudent':erStudent,'antallBilett':antallBilett,'pris':self.nyestePris}    
        with open('Bestillinger.json', 'r') as f:
            data2 = json.load(f)
        data2.append(data)
        with open('Bestillinger.json', 'w') as f:
            json.dump(data2,f,indent=2)
        
    
    def visAntallPlasserIgjen(self, sal:str):
        if sal.capitalize() == 'Gull':
            print(Teater.antallPlasserIgjenGull)
        if sal.capitalize() == 'Sølv':
            print(Teater.antallPlasserIgjenGull)
    
    def totaltTjent(self):
        tjent = 0
        for i in range(len(self.bestilinger)):
            tjent+=self.bestilinger[i].bergnPris()
        return tjent

with open('Bestillinger.json', 'r') as f:
    data2 = json.load(f)
 
with open('Bestillinger.json', 'w') as f:
    json.dump([],f,indent=2)
Teater1 = Teater()
for i in data2:
    datoSplit = i['dato'].split('-')
    Teater1.nyestePris = i['pris']
    Teater1.legTilBestiling(i['navn'],i['alder'],i['telefonNr'],i['epost'],i['adresse'],i['stykke'],i['dato'],i['sete'],i['erStudent'], i['antallBilett'])
    Teater1.bestilinger[-1].pris = Teater1.nyestePris
print(Teater1.seterSølvForAlleDager)
time.sleep(3)

while True:
    #Denne delen skal da imitate en "meny" på en nettside go kunden kan da navigerer til ønsket funksjon og (Annet kan være f.eks: vis antall plasser det er på hver stykke i datoen fremover eller noe sånnt)
    titleHoved = 'Hva vi tilbyr: \n\tDe elendige:\n\t\tSal: Gull\n\t\tAntall seter: 150\n\tVilanden:\n\t\tSal: Sølv\n\t\tAntall seter: 100\nPriser\n\tVoksen: 300 kr\n\tHonnør: 210 kr, defineres som individer over 67år.\n\tStudent: 240 kr, definers som studenter fra og til og med 18år til 30år\n\tBarn: 150 kr, defineres som individer under 10år \nMeny: '
    menyInnhold = ['Leggtil bestilling', 'Vis kvitering', 'Ledig datoer']
    menyvalgt, index = pick(menyInnhold, titleHoved, indicator='=>', default_index=0)

    #Hvis kunden velger leggtil bestiling så kan de leggtil en bestiling
    if menyvalgt == 'Leggtil bestilling':
        while True:
            title = 'Ønsker du å registrer en ny bestilling: '
            options = ['Ja', 'Nei']
            option, index = pick(options, title, indicator='=>', default_index=0)

            if option == 'Ja':
                    print('Registrere din bestilling:')

                    navn = input('\tNavn: ')

                    alder = it.riktigInputInt_float_eller_int('int','\tAlder','Alder ikke godskjent, husk det må være hel tall! Prøv igjen.', 0,None)

                    telefonNr = it.riktigInputInt_float_eller_int('int','\tTelefon nummer','Nummer ikke godskjent, husk det må være hel tall! Prøv igjen.', 0,None)

                    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
                    while True:
                        try:
                            epost = input('\tepost: ')
                            if(not re.fullmatch(regex,epost)):
                                raise ValueError
                        except:
                            print(f'Epost ikke godskjent, Mulige Grunn:\n\tIkke riktig format på epost.')
                        else:
                            break
                    adresse = input('\tAdresse: ')

                    erStudent = 'nei'
                    if 18<=alder and alder <=35:
                        erStudent, erStudentIndex = pick(['ja','nei'],'\tEr du en stuent?:')

                    #henter inn antall bileter kunden ønsker å kjøpe
                    antallBilett = it.riktigInputInt_float_eller_int('int','\tHvor mange biletter ønsker du å bestille','Kunn heltall er godskjent. Prøv igjen',1,150)

                    #henter inn stykke kunden ønsker å se, her vil det være en droppdown
                    valgStykkListe = ['De elendige', 'Vildanden']
                    valgStykke, stykkeIndex = pick(valgStykkListe, '\tVelg stykke du ønsker å se: ', indicator='=>', default_index=0)



                    #viser datoenen som det er mulig å se stykke på, denne listen med valg ekskluderer søndager
                    tilgjenligeDatoer = []
                    for i in range(14):
                        if (datetime.date(2024,2,1)+datetime.timedelta(i)).strftime('%A') != 'Sunday':
                            if valgStykke == 'De elendige':
                                if not Teater1.antallPlasserIgjenGull[i]-antallBilett <0:
                                    tilgjenligeDatoer.append(f'{datetime.date(2024,2,1)+datetime.timedelta(i)}, {(datetime.date(2024,2,1)+datetime.timedelta(i)).strftime("%A")}')
                                else:
                                    tilgjenligeDatoer.append(f'FULLT/IKKE NOK PLASS')

                            elif valgStykke == 'Vildanden':
                                if not Teater1.antallPlasserIgjenSølv[i]-antallBilett<0:
                                    tilgjenligeDatoer.append(f'{datetime.date(2024,2,1)+datetime.timedelta(i)}, {(datetime.date(2024,2,1)+datetime.timedelta(i)).strftime("%A")}')
                                else:
                                    tilgjenligeDatoer.append(f'FULLT/IKKE NOK PLASS')
                        else:
                            tilgjenligeDatoer.append(f'{datetime.date(2024,2,1)+datetime.timedelta(i)}, {(datetime.date(2024,2,1)+datetime.timedelta(i)).strftime("%A")}: stengt')

                    while True:
                        valgtDato, datoIndex = pick(tilgjenligeDatoer,'Dato vi har tilgjenlige framover:','=>',default_index=0)
                        if valgtDato == 'FULLT/IKKE NOK PLASS' or valgtDato[-6:len(valgtDato)] == 'stengt':
                            continue
                        else:
                            break

                    seterValgt = []
                    forrigeSeterValgt = []
                    if valgStykke == 'De elendige':
                        føreste = True

                        for i in range(antallBilett):
                            bestemRadPosision, radIndexPos = pick(['A-Nederst','B-Nest nederst', 'C-Midt', 'D-Nest øverst', 'E-Øverst'],'Bestem ønsket rad', '=>')
                            if føreste:
                                bestemSete, bestemSeteIndex = pick(Teater1.seterGullForAlleDager[datoIndex][radIndexPos], f'Velg ønsket Sete i rad {bestemRadPosision}','=>')
                            else:
                                bestemSete, bestemSeteIndex = pick(Teater1.seterGullForAlleDager[datoIndex][radIndexPos], f'Velg ønsket Sete i rad {bestemRadPosision}, for per {i+1}','=>')

                            seterValgt.append(bestemSete)
                            forrigeSeterValgt.append([bestemSete,bestemSeteIndex,radIndexPos])
                            Teater1.seterGullForAlleDager[datoIndex][radIndexPos].pop(bestemSeteIndex)

                    elif valgStykke == 'Vildanden':
                        føreste = True

                        for i in range(antallBilett):
                            bestemRadPosision, radIndexPos = pick(['A-Nederst','B-Nest nederst', 'C-Midt', 'D-Nest øverst'],'Bestem ønsket rad', '=>')
                            if føreste:
                                bestemSete, bestemSeteIndex = pick(Teater1.seterSølvForAlleDager[datoIndex][radIndexPos], f'Velg ønsket Sete i rad {bestemRadPosision}','=>')
                            else:
                                bestemSete, bestemSeteIndex = pick(Teater1.seterSølvForAlleDager[datoIndex][radIndexPos], f'Velg ønsket Sete i rad {bestemRadPosision}, for per {i+1}','=>')
                            
                            seterValgt.append(bestemSete)
                            forrigeSeterValgt.append([bestemSete,bestemSeteIndex,radIndexPos])
                            Teater1.seterSølvForAlleDager[datoIndex][radIndexPos].pop(bestemSeteIndex)

                    forrigeSeterValgt.reverse()                    
                    for i in forrigeSeterValgt:
                        if valgStykke == 'De elendige':
                            (Teater1.seterGullForAlleDager[datoIndex][i[2]]).insert(i[1],i[0])
                        elif valgStykke == 'Vildanden':
                            (Teater1.seterSølvForAlleDager[datoIndex][i[2]]).insert(i[1],i[0])
                    print(Teater1.seterGullForAlleDager[datoIndex])
                    print(Teater1.seterSølvForAlleDager[datoIndex])

                    
                    """Denne delen har kunn et mål å det er å regne ut prisen kunden betaler både hvis det er gruppe betilling eller individuel bestiling"""
                    bestilling1 = Bilett(navn,alder,telefonNr,epost,adresse,valgStykke,valgtDato,seterValgt,erStudent,antallBilett)
                    pris = bestilling1.bergnPris()
                    os.system('cls')
                    
                    """Denne delen outputer informasjonen kunden har gitt (og her får kunden muligheten til å se gjenom informasjonen å evnetuelt endre på det: Denne delen er ikke gjort ennda)"""
                    tekst2 = f'Du har gitt følgende informasjone:\n\tNavn: {navn}\n\tAlder: {alder} år\n\tEpost: {epost}\n\tStykke: {valgStykke}\n\tDato: {valgtDato}\n\tSete/settervalgt: {"-".join(seterValgt)}\n\tTotalpris: {pris} kr\nStemmer informasjonen'
                    valgt, valgtIndex = pick(['Ja','Nei'],tekst2,'=>',default_index=0, min_selection_count=1)

                    #Her går koden videre med å registrerer kjøpet hvis kunden godskjener at informasjonen stemmer eller (få muligheten til å endre på det i: if valgt == 'Nei': Denne delen er heler ikke gjort ennå)
                    if valgt == 'Ja':
                        Teater1.nyestePris = pris
                        Teater1.legTilBestiling(navn,alder,telefonNr,epost,adresse,valgStykke,valgtDato,seterValgt,erStudent, antallBilett)
                        Teater1.bestilinger[-1].pris = Teater1.nyestePris
                        print('Takk for din bestiling den er lagt inn.', pris)    
                        time.sleep(3)
                        os.system('cls')
                        break
                    elif valgt == 'Nei':
                        while True:
                            stykkeJa = False
                            antallJa = False
                            datoEndret = False

                            angre_endre = pick(['Navn','Alder','Telefon nr','Epost','Adresse','Antall','Stykke (Denne endringen vil automatisk endere "Dato" og "Sete").','Dato','Sete'],f'Du har gitt følgende informasjone:\n\tNavn: {navn}\n\tAlder: {alder} år\n\tEpost: {epost}\n\tStykke: {valgStykke}\n\tDato: {valgtDato}\n\tSete/settervalgt: {"-".join(seterValgt)}\n\tTotalpris: {pris} kr\nVelg informasjone du ønsker å endre', '=>', default_index=0,multiselect=True,min_selection_count=1)
                            nylisteValgInnhold = []
                            for y in range(len(angre_endre)):
                                nylisteValgInnhold.append(angre_endre[y][0])

                            if 'Antall' in nylisteValgInnhold:
                                antallJa = True
                            if 'Stykke (Denne endringen vil automatisk endere "Dato" og "Sete").' in nylisteValgInnhold:
                                stykkeJa = True
                            if 'Dato' in nylisteValgInnhold:
                                datoEndret = True

                            print(angre_endre)
                            for i in angre_endre:

                                if i[0] == 'Navn':
                                    navn = input('\tNavn: ')

                                elif i[0] == 'Alder':
                                    alder = it.riktigInputInt_float_eller_int('int','\tAlder','Alder ikke godskjent, husk det må være hel tall! Prøv igjen.', 0,None)

                                elif i[0] == 'Telefon nr':
                                    telefonNr = it.riktigInputInt_float_eller_int('int','\tTelefon nummer','Nummer ikke godskjent, husk det må være hel tall! Prøv igjen.', 0,None)

                                elif i[0] == 'Epost':
                                    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
                                    while True:
                                        try:
                                            epost = input('\tepost: ')
                                            if(not re.fullmatch(regex,epost)):
                                                raise ValueError
                                        except:
                                            print(f'Epost ikke godskjent, Mulige Grunn:\n\tIkke riktig format på epost.')
                                        else:
                                            break

                                elif i[0] == 'Adresse':
                                    adresse = input('\tAdresse: ')

                                elif i[0] == 'Antall':
                                    antallBilett = it.riktigInputInt_float_eller_int('int','\tHvor mange biletter ønsker du å bestille','Kunn heltall er godskjent. Prøv igjen',1,150)

                                elif i[0] == 'Stykke (Denne endringen vil automatisk endere "Dato" og "Sete").':
                                    valgStykkListe = ['De elendige', 'Vildanden']
                                    valgStykke, stykkeIndex = pick(valgStykkListe, '\tVelg stykke du ønsker å se: ', indicator='=>', default_index=0)

                                    tilgjenligeDatoer = []
                                    for y in range(14):
                                        if (datetime.date(2024,2,1)+datetime.timedelta(y)).strftime('%A') != 'Sunday':
                                            if valgStykke == 'De elendige':
                                                if not Teater1.antallPlasserIgjenGull[y]-antallBilett <0:
                                                    tilgjenligeDatoer.append(f'{datetime.date(2024,2,1)+datetime.timedelta(y)}, {(datetime.date(2024,2,1)+datetime.timedelta(y)).strftime("%A")}')
                                                else:
                                                    tilgjenligeDatoer.append(f'FULLT/IKKE NOK PLASS')

                                            elif valgStykke == 'Vildanden':
                                                if not Teater1.antallPlasserIgjenSølv[y]-antallBilett<0:
                                                    tilgjenligeDatoer.append(f'{datetime.date(2024,2,1)+datetime.timedelta(y)}, {(datetime.date(2024,2,1)+datetime.timedelta(y)).strftime("%A")}')
                                                else:
                                                    tilgjenligeDatoer.append(f'FULLT/IKKE NOK PLASS')
                                        else:
                                            tilgjenligeDatoer.append(f'{datetime.date(2024,2,1)+datetime.timedelta(y)}, {(datetime.date(2024,2,1)+datetime.timedelta(y)).strftime("%A")}: stengt')

                                    while True:
                                        valgtDato, datoIndex = pick(tilgjenligeDatoer,'Dato vi har tilgjenlige framover:','=>',default_index=0)
                                        if valgtDato == 'FULLT/IKKE NOK PLASS' or valgtDato[-6:len(valgtDato)] == 'stengt':
                                            continue
                                        else:
                                            break

                                    
                                    seterValgt.clear()
                                    forrigeSeterValgt.clear()
                                    if valgStykke == 'De elendige':
                                        føreste = True

                                        for y in range(antallBilett):
                                            bestemRadPosision, radIndexPos = pick(['A-Nederst','B-Nest nederst', 'C-Midt', 'D-Nest øverst', 'E-Øverst'],'Bestem ønsket rad', '=>')
                                            if føreste:
                                                bestemSete, bestemSeteIndex = pick(Teater1.seterGullForAlleDager[datoIndex][radIndexPos], f'Velg ønsket Sete i rad {bestemRadPosision}','=>')
                                            else:
                                                bestemSete, bestemSeteIndex = pick(Teater1.seterGullForAlleDager[datoIndex][radIndexPos], f'Velg ønsket Sete i rad {bestemRadPosision}, for per {y+1}','=>')

                                            seterValgt.append(bestemSete)
                                            forrigeSeterValgt.append([bestemSete,bestemSeteIndex, radIndexPos])
                                            Teater1.seterGullForAlleDager[datoIndex][radIndexPos].pop(bestemSeteIndex)

                                    elif valgStykke == 'Vildanden':
                                        føreste = True

                                        for y in range(antallBilett):
                                            bestemRadPosision, radIndexPos = pick(['A-Nederst','B-Nest nederst', 'C-Midt', 'D-Nest øverst'],'Bestem ønsket rad', '=>')
                                            if føreste:
                                                bestemSete, bestemSeteIndex = pick(Teater1.seterSølvForAlleDager[datoIndex][radIndexPos], f'Velg ønsket Sete i rad {bestemRadPosision}','=>')
                                            else:
                                                bestemSete, bestemSeteIndex = pick(Teater1.seterSølvForAlleDager[datoIndex][radIndexPos], f'Velg ønsket Sete i rad {bestemRadPosision}, for per {y+1}','=>')
                                            
                                            seterValgt.append(bestemSete)
                                            forrigeSeterValgt.append([bestemSete,bestemSeteIndex,radIndexPos])
                                            Teater1.seterSølvForAlleDager[datoIndex][radIndexPos].pop(bestemSeteIndex)

                                    forrigeSeterValgt.reverse()                    
                                    for y in forrigeSeterValgt:
                                        if valgStykke == 'De elendige':
                                            (Teater1.seterGullForAlleDager[datoIndex][y[2]]).insert(y[1],y[0])
                                        elif valgStykke == 'Vildanden':
                                            (Teater1.seterSølvForAlleDager[datoIndex][y[2]]).insert(y[1],y[0])
                                    print(Teater1.seterGullForAlleDager[datoIndex])
                                    print(Teater1.seterSølvForAlleDager[datoIndex])
                                                
                                elif i[0] == 'Dato' and not stykkeJa:
                                    tilgjenligeDatoer = []
                                    for y in range(14):
                                        if (datetime.date(2024,2,1)+datetime.timedelta(y)).strftime('%A') != 'Sunday':
                                            if valgStykke == 'De elendige':
                                                if not Teater1.antallPlasserIgjenGull[y]-antallBilett <0:
                                                    tilgjenligeDatoer.append(f'{datetime.date(2024,2,1)+datetime.timedelta(y)}, {(datetime.date(2024,2,1)+datetime.timedelta(y)).strftime("%A")}')
                                                else:
                                                    tilgjenligeDatoer.append(f'FULLT/IKKE NOK PLASS')

                                            elif valgStykke == 'Vildanden':
                                                if not Teater1.antallPlasserIgjenSølv[y]-antallBilett<0:
                                                    tilgjenligeDatoer.append(f'{datetime.date(2024,2,1)+datetime.timedelta(y)}, {(datetime.date(2024,2,1)+datetime.timedelta(y)).strftime("%A")}')
                                                else:
                                                    tilgjenligeDatoer.append(f'FULLT/IKKE NOK PLASS')
                                        else:
                                            tilgjenligeDatoer.append(f'{datetime.date(2024,2,1)+datetime.timedelta(y)}, {(datetime.date(2024,2,1)+datetime.timedelta(y)).strftime("%A")}: stengt')

                                    while True:
                                        valgtDato, datoIndex = pick(tilgjenligeDatoer,'Dato vi har tilgjenlige framover:','=>',default_index=0)
                                        if valgtDato == 'FULLT/IKKE NOK PLASS' or valgtDato[-6:len(valgtDato)] == 'stengt':
                                            continue
                                        else:
                                            break

                                if (i[0] == 'Sete' and not stykkeJa) or (antallJa and not stykkeJa) or (datoEndret and not stykkeJa)  :

                                    seterValgt.clear()
                                    forrigeSeterValgt.clear()
                                    if valgStykke == 'De elendige':
                                        føreste = True

                                        for y in range(antallBilett):
                                            bestemRadPosision, radIndexPos = pick(['A-Nederst','B-Nest nederst', 'C-Midt', 'D-Nest øverst', 'E-Øverst'],'Bestem ønsket rad', '=>')
                                            if føreste:
                                                bestemSete, bestemSeteIndex = pick(Teater1.seterGullForAlleDager[datoIndex][radIndexPos], f'Velg ønsket Sete i rad {bestemRadPosision}','=>')
                                            else:
                                                bestemSete, bestemSeteIndex = pick(Teater1.seterGullForAlleDager[datoIndex][radIndexPos], f'Velg ønsket Sete i rad {bestemRadPosision}, for per {y+1}','=>')

                                            seterValgt.append(bestemSete)
                                            forrigeSeterValgt.append([bestemSete,bestemSeteIndex, radIndexPos])
                                            Teater1.seterGullForAlleDager[datoIndex][radIndexPos].pop(bestemSeteIndex)

                                    elif valgStykke == 'Vildanden':
                                        føreste = True

                                        for y in range(antallBilett):
                                            bestemRadPosision, radIndexPos = pick(['A-Nederst','B-Nest nederst', 'C-Midt', 'D-Nest øverst'],'Bestem ønsket rad', '=>')
                                            if føreste:
                                                bestemSete, bestemSeteIndex = pick(Teater1.seterSølvForAlleDager[datoIndex][radIndexPos], f'Velg ønsket Sete i rad {bestemRadPosision}','=>')
                                            else:
                                                bestemSete, bestemSeteIndex = pick(Teater1.seterSølvForAlleDager[datoIndex][radIndexPos], f'Velg ønsket Sete i rad {bestemRadPosision}, for per {y+1}','=>')
                                            
                                            seterValgt.append(bestemSete)
                                            forrigeSeterValgt.append([bestemSete,bestemSeteIndex,radIndexPos])
                                            Teater1.seterSølvForAlleDager[datoIndex][radIndexPos].pop(bestemSeteIndex)

                                    forrigeSeterValgt.reverse()                    
                                    for y in forrigeSeterValgt:
                                        if valgStykke == 'De elendige':
                                            (Teater1.seterGullForAlleDager[datoIndex][y[2]]).insert(y[1],y[0])
                                        elif valgStykke == 'Vildanden':
                                            (Teater1.seterSølvForAlleDager[datoIndex][y[2]]).insert(y[1],y[0])
                                    print(Teater1.seterGullForAlleDager[datoIndex])
                                    print(Teater1.seterSølvForAlleDager[datoIndex])

                            bestilling1 = Bilett(navn,alder,telefonNr,epost,adresse,valgStykke,valgtDato,seterValgt,erStudent,antallBilett)
                            pris = bestilling1.bergnPris()
                            os.system('cls')
                            
                            """Denne delen outputer informasjonen kunden har gitt (og her får kunden muligheten til å se gjenom informasjonen å evnetuelt endre på det: Denne delen er ikke gjort ennda)"""
                            tekst2 = f'Du har gitt følgende informasjone:\n\tNavn: {navn}\n\tAlder: {alder} år\n\tEpost: {epost}\n\tStykke: {valgStykke}\n\tDato: {valgtDato}\n\tSete/settervalgt: {"-".join(seterValgt)}\n\tTotalpris: {pris} kr\nStemmer informasjonen'
                            valgt, valgtIndex = pick(['Ja','Nei'],tekst2,'=>',default_index=0)

                            if valgt == 'Ja':
                                Teater1.nyestePris = pris
                                Teater1.legTilBestiling(navn,alder,telefonNr,epost,adresse,valgStykke,valgtDato,seterValgt,erStudent, antallBilett)
                                Teater1.bestilinger[-1].pris = Teater1.nyestePris
                                print('Takk for din bestiling den er lagt inn.', pris)    
                                time.sleep(3)
                                os.system('cls')

                                break
                            elif valgt == 'Nei':
                                continue




            elif option == 'Nei':
                break
    #Hvis kunden velger 'vis kvitering' så kan de søke etter sin egen kvitering via telefonnummer men her er det sikkert andre tryggerer måter å søke på???
    elif menyvalgt == 'Vis kvitering':
        os.system('cls')
        allEposter = []
        for i in Teater1.bestilinger:
            allEposter.append((i.epost).lower())
        while True:
            AVSLUTT = False
            while True:
                try:
                    brukerEpost= input('Skriv inn emailen du brukte under registrereing: ')
                    if(not brukerEpost.lower() in allEposter):
                        raise ValueError
                except:
                    print(f'Epost ikke godskjent, Mulige Grunn:\n\tIngen Kvittering registrert under eposten {brukerEpost}.')
                    x = pick(['Ja', 'Nei'], 'Ønsker du å prøve igjen', '=>')
                    if x[0] == 'Ja':
                        AVSLUTT = True
                        break
                else:
                    engangsKode = f'{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}'
                    pywhatkit.send_mail("nanikanblidet@gmail.com", "ubbl dwcl uglk jdwp", "Subject", f"Din engangskode er : {engangsKode}", brukerEpost)
                    os.system('cls')
                    print("Godskjent epost, engangskode sendt!")
                    time.sleep(3)
                    os.system('cls')
                    break

            if AVSLUTT:
                break

            Nei = False
            prøver = 0
            print('Skriv inn engangskoden som er sendt til din Epost')
            while True:
                if(prøver < 3):
                    kode = input(f'\tforsøk {prøver + 1}: ')
                    if kode == engangsKode:
                        print('Godskjent')
                        time.sleep(3)
                        break
                    else:
                        prøver+=1
                        continue
                else:
                    Nei = True
                    break

            if Nei:
                print('For mange feil forsøk.')
                time.sleep(3)
                break

            os.system('cls')

            
            alleKviteringer = ''
            
            for i in Teater1.bestilinger:
                if (i.epost).lower() == brukerEpost.lower():
                    alleKviteringer = i.visKvittering()
        

            valger2 = ['Ferdig', 'Finn ny kvitering']
            valgt2, valgtIndex2 = pick(valger2,alleKviteringer,'=>',default_index=0)

            if valgt2 == 'Ferdig':
                os.system('cls')
                break
            elif valgt2 == 'Finn ny kvitering':
                os.system('cls')
                continue
    else:
        datoer = []
        for i in range(14):
            if (datetime.date(2024,2,1)+datetime.timedelta(i)).strftime('%A') != 'Sunday':
                datoer.append(f'{datetime.date(2024,2,1)+datetime.timedelta(i)}, {(datetime.date(2024,2,1)+datetime.timedelta(i)).strftime("%A")}')
            else:
                datoer.append(f'{datetime.date(2024,2,1)+datetime.timedelta(i)}, {(datetime.date(2024,2,1)+datetime.timedelta(i)).strftime("%A")}: stengt')
            
        while True:
            velg, velgindex = pick(datoer,'Hvilken dato ønsker du å sjekke antall ledig biletter det er:','=>')

            velg2, velgindex2 = pick(['Ja','Nei'],f'{velg}:\n\tSalnavn: {Gold.salNavn}\n\t\tStykke: {Gold.stykke}\n\t\tTilgjenglige biletter igjen: {Teater1.antallPlasserIgjenGull[velgindex]}\n\tSalnavn: {Sølv.salNavn}\n\t\tStykke: {Sølv.stykke}\n\t\tTilgjenglige biletter igjen: {Teater1.antallPlasserIgjenSølv[velgindex]}\n\nØnsker du å sjekke en ny dato:','=>')

            if velg2 == 'Ja':
                continue
            else:
                break
