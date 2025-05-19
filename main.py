from datetime import date


def moje_imie():
  imie = "Beata"
  print("Mam na imie", imie)
  print("---------------------------")

def twoje_imie():
  twoje_imie = input("Jak masz na imię?")
  print("Cześć", twoje_imie)
                     
if twoje_imie == moje_imie:
  print("Mamy takie same imiona")
else: 
  print("cześć", twoje_imie)

moje_imie ()
twoje_imie ()