def beolvas():
    adatok = {}
    tomb = []
    f = open("./helsinki.txt", "r")
    for sor in f:
        sor = sor.strip().split()
        sor[0] = int(sor[0])
        sor[1] = int(sor[1])
        adatok = { 
            "Helyezes" : sor[0],
            "Sportoloksz" : sor[1],
            "Sportag" : sor[2],
            "Versenyszam" : sor[3],
        }
        tomb.append(adatok)
        adatok = {}
    return tomb

def pontszamolas(tomb):
    pont = 0
    for i in tomb:
        pont += 1
    print(f"Pontszerző helyezések száma: {pont}")
    return pont   

def helyezesek(tomb):
    arany = 0
    ezust = 0
    bronz = 0

    for i in tomb:
        if i["Helyezes"] == 1 :
            arany += 1
        elif i["Helyezes"] == 2 :
            ezust += 1
        elif i["Helyezes"] == 3 :
            bronz += 1

    ossz =  arany + ezust + bronz

    print(f"Arany : {arany}")
    print(f"Ezüst : {ezust}")
    print(f"Bronz : {bronz}")
    print(f"Összesen : {ossz}")

def pontszámok(tomb):
    osszpont = 0

    for i in tomb:
        if i["Helyezes"] == 1 :
            osszpont += 7
        elif i["Helyezes"] == 2 :
            osszpont += 5
        elif i["Helyezes"] == 3 :
            osszpont += 4
        elif i["Helyezes"] == 4 :
            osszpont += 3
        elif i["Helyezes"] == 5 :
            osszpont += 2
        elif i["Helyezes"] == 6 :
            osszpont += 1
    
    print(f"Olimpikai pontok száma : {osszpont}")
    return osszpont

def sportagerm(tomb):
    torna = 0
    uszas = 0

    for i in tomb:
        if i["Sportag"] == "torna" :
            torna += i["Helyezes"]
        elif i["Sportag"] == "uszas" :
            uszas += i["Helyezes"]

    for i in tomb:
        if torna > uszas:
            print("Torna sportágban szereztek több érmet.")
            break
        elif torna > uszas:
            print("Uszás sportágban szereztek több érmet.")
            break
        else:
            print("Egyenlő volt az érmek száma")
            break




tomb = beolvas()
print(tomb)

pontszamolas(tomb)

helyezesek(tomb)

pontszámok(tomb)

sportagerm(tomb)

