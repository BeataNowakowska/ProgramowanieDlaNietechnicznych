from datetime import date

imie = "Paweł"


def moje_imie():
  print("Mam na imie", imie)


def twoje_imie():

  twoje_imie = input("Jak masz na imię? ")
  print("Cześć", twoje_imie)

  moje_imie()

  if twoje_imie == imie:
    print("Masz to samo imię co ja!")
  else:
    print("Masz inne imię niż ja.")


twoje_imie()
