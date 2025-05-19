from datetime import date

imie = "Agata"


def moje_imie():
  print("Mam na imie", imie)
  print("---------------------------")


def twoje_imie():
  twoje_imie = input("Jak masz na imię?")
  print("Cześć", twoje_imie)


if twoje_imie == moje_imie:
  print("Mamy takie same imiona")
else:
  print("cześć", twoje_imie)

moje_imie()
twoje_imie()
