import os
import time
from time import gmtime, strftime

localTime = strftime("%A, %Y.%m.%d, %H:%M:%S", time.localtime())

print("Kérlek add meg a szöveget: ")

text = ""

while(True):
    textSample = input()
    if textSample == "end":
        break
    else:
        text += textSample + "\n"

fileName = input("Kérlek add meg a fájl nevét: ")

Path = os.path.join(os.environ["USERPROFILE"],"Desktop","Progprog")
if not os.path.exists(Path):
    os.makedirs(Path)

completeName = os.path.join(Path, fileName+".txt")

with open(completeName, "w", encoding="utf-8") as f:
    f.write(localTime + " Bejegyzés:\n" + text)

print(f"✅ A bejegyzés elmentve ide: {completeName}")