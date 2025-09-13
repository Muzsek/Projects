import random

print("Dobókocka szimulátor")

while(True):
    try:
        howManyDices = int(input("Kérlek add meg, hogy hány kockával szeretnél dobni (0 -> kilépés): "))
        if howManyDices <= 0:
            print("Kilépés")
            break
        elif howManyDices > 0:
            dobasok = [random.randint(1,6) for dice in range(howManyDices)]


            print(f"Összegzés:")
            for i,d in enumerate(dobasok, start = 1):
                print(f"{i}. kocka: {d}")
            print(f"Összegük: {sum(dobasok)}")
        else:
            print("Hibás számot adtál meg!")
    except ValueError:
        print("Hibás bemenet, kérlek csak számot adj meg!")
