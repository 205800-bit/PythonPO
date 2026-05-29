
#Spiderman villan Quiz

""""De 10 vragen die in de quiz gaan komen"""

vragen = [
    "Welke motivatie past het meest bij jou?",
    "Hoe pak jij een probleem aan?",
    "Hoe ga je om met vijanden?",
    "Welke kracht past het beste bij jou?",
    "Hoe reageer je als iemand je onderschat?",
    "Wat is jouw grootste zwakte?",
    "Hoe werk je het liefst?",
    "Wat zou je doen als je nieuwe krachten krijgt?",
    "Hoe ga je om met verlies?",
    "Wat vind je het belangrijkst in een gevecht?"
]


antwoorden = [
    [
        "Ik wil controle en kennis uitbreiden",
        "Ik wil chaos creëren en macht tonen",
        "Ik wil wraak en brute kracht gebruiken",
        "Ik wil pure energie en kracht voelen"
    ],
    [
        "Ik analyseer het en maak een plan",
        "Ik ga impulsief te werk en vertrouw op instinct",
        "Ik ga er vol in met brute kracht",
        "Ik reageer explosief en snel"
    ],
    [
        "Ik manipuleer en overdenk elke stap",
        "Ik speel met hun angst en creëer chaos",
        "Ik val direct aan zonder twijfel",
        "Ik overlaad ze met pure energie"
    ],
    [
        "Mechanische armen en superintelligentie",
        "Glider‑technologie en bommen",
        "Symbioot‑kracht en brute agressie",
        "Elektriciteit beheersen"
    ],
    [
        "Ik bewijs mijn superioriteit met strategie",
        "Ik word onvoorspelbaar en gevaarlijk",
        "Ik word woedend en ga in de aanval",
        "Ik knal door het dak van frustratie"
    ],
    [
        "Mijn ego en drang naar controle",
        "Mijn paranoia en wantrouwen",
        "Mijn woede en agressie",
        "Mijn instabiliteit en impulsiviteit"
    ],
    [
        "Met een plan en technologie",
        "Alleen, zodat ik alles zelf kan bepalen",
        "Als lone wolf, niemand komt dichtbij",
        "Chaotisch en snel, zonder regels"
    ],
    [
        "Ik test ze uitgebreid en onderzoek alles",
        "Ik gebruik ze om chaos te verspreiden",
        "Ik gebruik ze direct in een gevecht",
        "Ik laat ze meteen los op alles om me heen"
    ],
    [
        "Ik analyseer wat misging en verbeter mezelf",
        "Ik zoek wraak en laat chaos achter",
        "Ik word agressief en ga harder vechten",
        "Ik verlies controle en ontplof"
    ],
    [
        "Strategie en controle",
        "Onvoorspelbaarheid en intimidatie",
        "Pure kracht en agressie",
        "Snelheid en overweldigende energie"
    ]
]
def vragen_quiz(vragen, antwoordopties):
    teller = 0
    antwoord = []

    while teller < len(vragen):
        print("----------------------------------")
        print(vragen[teller])
        print(f"A) {antwoordopties[teller][0]}")
        print(f"B) {antwoordopties[teller][1]}")
        print(f"C) {antwoordopties[teller][2]}")
        print(f"D) {antwoordopties[teller][3]}")

        answer = input("Kies A/B/C/D: ").lower()

        if answer in ["a", "b", "c", "d"]:
            antwoord.append(answer)
            teller += 1
        else:
            print("Ongeldige invoer")

    puntentelling(antwoord)
    return antwoord



def puntentelling(uitslag_lijst):
    Doctor_octopus = 0
    Green_goblin = 0
    Venom = 0
    Electro = 0
   


    for punt in uitslag_lijst:
        if punt == "a":
            Doctor_octopus += 1
        elif punt == "b":
            Green_goblin += 1
        elif punt == "c":
            Venom += 1
        elif punt == "d":
            Electro +=1


    villains  = [Doctor_octopus, Green_goblin, Venom, Electro]
    winnaar = max(villains)
    print("-------------------")
    print("De Spiderman villain die het best bij jou past is:\n"
          "")
    if villains[0] == winnaar:
        print("Doctor Octopus \n"
              "Strategisch, slim en altijd drie stappen vooruit. Jij houdt van controle, plannen en domineren met je intelligentie.")
    elif villains[1] == winnaar:
        print("Green Goblin \n"
              " Chaotisch, onvoorspelbaar en intens. Jij leeft voor spanning, risico’s en het doorbreken van regels.")
    elif villains[2] == winnaar:
        print("Venom \n"
              "Gedreven door emotie, kracht en instinct. Jij bent loyaal, maar je woede maakt je gevaarlijk en onstuitbaar.")
    elif villains[3] == winnaar:
        print("Electro \n"
              "Snel, explosief en impulsief. Jij reageert direct, vol energie, en laat je niet tegenhouden zodra je op gang komt.")
        

    
    print("Leuk dat je mee deed!!, wil je het nog een keer proberen??")
    terug = int(input("1. Ja\n" \
    "2. Nee"))

    if terug == 1:
        main()
    elif terug == 2:
        print("Okee, tot ziens")
        


def main():
    i = 0
    while i == 0:
        print("-------------------------------")
        print("heyy Welkom bij de spider man villain quiz")
        print("Vandaag ga je er achter komen welke spider man villain het beste bij jou past")
        klaar_voor = int(input("Als je er klaar voor bent typ 1 in, veel succes!!\n"))
        if klaar_voor == 1:
            i += 1
            vragen_quiz(vragen, antwoorden)
        else:
            i += 0

if __name__ == '__main__':
    main()