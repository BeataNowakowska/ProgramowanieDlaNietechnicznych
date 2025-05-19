from datetime import date

imie = "Agata"


def moje_imie():
  print("Mam na imie", imie)
  print("---------------------------")


def twoje_imie():
  twoje_imie = input("Jak masz na imie? ")
  print("Masz na imie", twoje_imie)

  if twoje_imie == imie:
    print("O masz na imie tak jak ja", imie)
  else:
    print("Twoje imie jest różne niż moje", imie)


print("Bla bla bla")

moje_imie()
twoje_imie()
