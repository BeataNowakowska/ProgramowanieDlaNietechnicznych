from datetime import date


#print("Hello, World!")
#print("testowy komunikat")
#Mój pierwszy skrypt w Pythonie 
#print("Koniec skryptu")
#print("ala ma kota")

imie = "Paweł"

print("Nazywam się:", imie)

imie_nazwisko = imie + " G"

print("Nazywam się:", imie_nazwisko)


#imie2 = input("Podaj swoje imię: ")
#print("Nazywam się: " + imie2 )

data = date.today()
moje_urodziny = date(1990, 12, 3)

print ("Od moich urodzin minęło: ", data - moje_urodziny)

boze_narodzenie = date(2025, 12, 25)

print ("Do Bożego Narodzenia pozostało: ", boze_narodzenie - data)

moje_urodziny_ten_rok = date(2025, 12, 3)


print ("Do moich urodzin pozostało: ", moje_urodziny_ten_rok - data)



twoje_imie=input("Podaj swoje imię: ")
print("Ty nazywasz się: " + twoje_imie)

