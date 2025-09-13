import random

choices = ["kő" , "papír" , "olló"]


print("Kő / Papír / Olló")

playerChoice = input("Kérlek válassz (kő/papír/olló): ").lower()

if playerChoice not in choices:
    print("⚠️ Hibás választás! Csak 'kő', 'papír' vagy 'olló' lehet.")
else:
    computerChoice = random.choice(choices)
    print(f"Te: {playerChoice} \nGép: {computerChoice}")

if playerChoice == computerChoice:
    print(f"Döntetlen\nTe:{playerChoice}\nGép:{computerChoice}")
else:
    match computerChoice:
        case "kő":
            match playerChoice:
                case "papír":
                    print("Nyertél")
                case "olló":
                    print("Vesztettél")
        case "papír":
            match playerChoice:
                case "olló":
                    print("Nyertél")
                case "kő":
                    print("Vesztettél")
        case "olló":
            match playerChoice:
                case "papír":
                    print("Vesztettél")
                case "kő":
                    print("Nyertél")
