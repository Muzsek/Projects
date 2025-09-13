import random

def firstChoice(min : int,max : int):
    minNum = min
    maxNum = max
    answer = ''
    while(answer != 'y'):
        computerGuess = (maxNum + minNum) / 2
        answer = input(f"A gondolt számom a {int(computerGuess)}\nEltaláltam: (y)\nNagyobb: (n)\nKisebb: (k)\n")
        match answer:
            case 'n':
                minNum = computerGuess
            case 'k':
                maxNum = computerGuess
    
    print(f"A tippelt szám a(z) {int(computerGuess)} volt\nKöszönöm a játékot")
    return 0

def secondChoice(min : int,max : int):
    computerGuess = random.randint(min,max)
    ownGuess = 0
    while(computerGuess != ownGuess):
        ownGuess = int(input("Kérlek tippelj: "))
        
        match (computerGuess, ownGuess):
            case (c,o) if c > o:
                print("Nagyobb")
            case (c,o) if c < o:
                print("Kisebb")
            case (c,o) if c == o:
                print(f"Gratulálok, a(z) {computerGuess} számra gondoltam!")
                return 0

while(True):
    minInt = int(input("Kérlek adj meg egy alsó intervallumot: "))
    maxInt = int(input("Kérlek adj meg egy felső intervallumot: "))
    print(f"Hogyan szeretnél játszani ({minInt}-{maxInt})?")
    print("1. Te találsz ki egy számot és én találok ki:")
    print("2. Én találok egyet és te találod ki:")
    try:
        choice = int(input("Válasz: "))
        if choice not in (1,2):
            print("Hibás bemenet")
        else:
            print(f"Válaszott szám: {choice}")
            if choice == 1:
                firstChoice(min = minInt, max = maxInt)
            elif choice == 2:
                secondChoice(min = minInt, max = maxInt)
        answer = input("Szeretnél újra játszani (i/n)?")
        match answer:
            case 'i':
                continue
            case 'n':
                print("Kilépés, köszönöm, hogy velem játszottál!")
                break
            
    except ValueError:
        print("Csak számot adj meg")