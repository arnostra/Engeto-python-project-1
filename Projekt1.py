'''
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Arnošt Razima
email: razima.ar@seznam.cz
discord: Arnošt R. #3251
"""
import ...
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

###############################################################
cara = "-" * 40
uzivatele_hesla_tabulka = """
+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+
"""

uzivatele_hesla = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}
#prihlaseni uzivatele
username = input("Enter your username: ")
password = input("Enter your password: ")
print(cara)#-------------------------------------------------------------------
if username in uzivatele_hesla and uzivatele_hesla[username] == password:
    print("Welcome to app,", username)
else:
    print("Pristup zamitnut")
    exit()
print('We have 3 texts to be analyzed. ')
print(cara)#-------------------------------------------------------------------


vyber_textu = input("Enter a number btw. 1 and 3 to select: ")
print(cara)#-------------------------------------------------------------------

if vyber_textu.isnumeric():
    vyber_textu = int(vyber_textu)
    if 1 <= vyber_textu <= 3:
        text = TEXTS[vyber_textu-1]
        slova = text.split()
        slova_pocet = len(slova)

        slova_s_velkym_pismenem = 0
        for slovo in slova:
            if slovo[0].isupper():
                slova_s_velkym_pismenem += 1

        VELKA_slova = []
        mala_slova = []
        for slovo in slova:
            if slovo.isalpha() and slovo.isupper():
                VELKA_slova.append(slovo)
            elif slovo.isalpha() and slovo.islower():
                mala_slova.append(slovo)

        #spocitat slova
        cisla_pocet = 0
        cisla_suma = 0
        for slovo in slova:
            if slovo.isnumeric():
                cisla_pocet += 1
                cisla_suma += int(slovo)

        #print poctu
        print(f"Pocet slov: {slova_pocet}")
        print(f"Pocet slov zacinajicich valkym pismenem: {slova_s_velkym_pismenem}")
        print(f"Pocet slov psanych velkymi pismeny: {len(VELKA_slova)}")
        print(f"Pocet slov psanych malymi pismeny: {len(mala_slova)}")
        print(f"Pocet cisel: {cisla_pocet}")
        print(f"Pocet cisel suma: {cisla_suma}")
    else:
        print("Invalid selection. Please enter a number between 1 and 3.")
else:
    print("Invalid input. Please enter a number between 1 and 3.")   
print(cara)#------------------------------------------------------------------- 

print("LEN|  OCCURENCES  |NR.")
print(cara)#-------------------------------------------------------------------


# Rozdělení textu na slova
# Spočítání délky jednotlivých slov a uložení do slovníku
delky_slov = {}
for slovo in slova:
    delka = len(slovo)
    if delka in delky_slov:
        delky_slov[delka] += 1
    else:
        delky_slov[delka] = 1
    

lst = sorted(delky_slov.items())
for i in range(len(lst)):
    print(lst[i][0], end="| ")
    for _ in range(lst[i][1]):
        print("*", end="")
    print(end=" ")
    print(lst[i][1])