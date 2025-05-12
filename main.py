#dupa dupa dupa


def pole_kwadratu(bok):
  return bok * bok


def pole_prostokąta(a, b):
  return a * b


def pole_koła(promień):
  return 3.14159 * promień * promień


while True:
  print("Wybierz figurę, której pole chcesz obliczyć:")
  odpowiedz = input("1 - kwadrat, 2 - prostokąt, 3 - koło, 4 - wyjście: ")

  if odpowiedz == "1":
    bok_string = input("Podaj długość boku: ")
    bok = float(bok_string)
    pole = pole_kwadratu(bok)
    print("Pole kwadratu wynosi " + str(pole))

  elif odpowiedz == "2":
    a_string = input("Podaj długość pierwszego boku: ")
    a = float(a_string)
    b_string = input("Podaj długość drugiego boku: ")
    b = float(b_string)
    pole = pole_prostokąta(a, b)
    print("Pole prostokąta wynosi " + str(pole))

  elif odpowiedz == "3":
    promień_string = input("Podaj promień: ")
    promień = float(promień_string)
    pole = pole_koła(promień)
    print("Promień koła wynosi " + str(pole))
  elif odpowiedz == "4":
    print("Koniec programu.")
    break

#----------------------------------------------

mowic_dalej = True
while (mowic_dalej):
  if input("Opowiedzieć ci irytujący żart?") != "tak":
    mowic_dalej = False
