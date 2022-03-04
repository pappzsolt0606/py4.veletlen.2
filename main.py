'''
2. Feladat
A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását (fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e!
'''
import random

a = "fej"
b = "írás"

szam = random.randint(1, 2)

if szam == 1:
    szam = a
if szam == 2:
    szam = b

szó = input("fej vagy írás ")

if szó == szam:
    print("jól válaszoltál")
if szó != szam:
    print("nem jó válasz")
if szó != a or szó != b:
    print(f"fejet vagy írást kértem ")
    
