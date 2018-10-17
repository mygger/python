#Esimene rühm. Varmo Pilt
#Ülesanne 1
#Kirjutage funktsiooni list_sum(list) mis võtab argumendiks listi (massiivi) ja tagastab tema elementide summa.

def list_sum(list):
    '''Funktsioon võtab argumendiks numbrite listi ja tagastab elementide summa numbrina'''
    return sum(list)

#Ülesanne 2
#Kirjutage funktsiooni liblikas(string), mis võtab argumendiks lause (sõnad jagatud tühikutega) ja kui sõna
#algab tähega "a" asendab teda sõnaga "liblikas". Kui lauses on kaks või rohkem sõna mis algavad "a"-ga
#asendada ainult viimane.


def liblikas(string):
    '''Funktsioon võtab argumendiks lause ja tagastab stringi, kus on asendatud viimane a-ga algava sõna sõnaga
    "liblikas"'''
    stringlist = []
    stringlist=string.split()
    abilist=[]
    for i in range(len(stringlist)):
        aa=stringlist[i]
        if aa[0]=="a":
            abilist.append(i)
    stringlist[max(abilist)]="liblikas"
    lause=''
    for sona in stringlist:
        lause=lause+sona + " "
    return lause[:-1]


#Ülesanne 3
#Kirjutage funktsiooni common_symbols(string, string), mis võtab vastu kaks string-tüüpi sama pikkusega
#muutujat, mis koosnevad suurtest tähetest ja väljastab komaga jagatud numbid, mis vastavad järgmisele
#tingimustele:    1) Samad sümbolid samades kohtades 2) Sümbolite mis leiduvad mõlemas muutujates arv kokku

def common_symbols(string1, string2):
    '''Funktsioon võtab argumendiks kaks sama pikkusega stringi ja tagastab 2 arvu, millest esimene on samade
    sübolite arv, mis on samal kohtadel mõlema stringis ja teine on mõlemas strings sisalduvate sümbolite arv
    kokku. Numbrid on komaga eraldatud.'''
    arv1=0
    arv2=0
    abilist=[]
    for i in range(len(string1)):
        if string1[i]==string2[i]:
            arv1=arv1+1
        for j in range(len(string1)):
            if string1[i]==string2[j]:
                on=0
                for taht in abilist:
                    if taht==string1[i]:
                        on=1
                if on==0:
                    arv2=arv2+1
                    abilist.append(string1[i])
    return str(arv1) + "," + str(arv2)
