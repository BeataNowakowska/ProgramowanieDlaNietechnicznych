from datetime import date


def moje_imie():
  imie = "Beata"
  print("Mam na imie", imie)
  print("---------------------------")


def moj_wiek():
  wiek = 18
  print("Mam", wiek, "lat")


def dzisiaj():
  dzisiaj = date.today()
  print("Dzisiaj jest", dzisiaj)


def moje_urodziny():
  dzisiaj = date.today()
  moje_urodziny = date(1982, 2, 27)

  print("Moje urodziny sa", moje_urodziny)
  print("Od moich urodzi minęło", dzisiaj - moje_urodziny)


def twoje_imie():
  twoje_imie = input("Jak masz na imie? ")
  print("Twoje imie to", twoje_imie)
