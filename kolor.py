print("Podaj swój ulubiony kolor: ")
kolor = input()

if kolor in ("niebieski", "czerwony", "żółty"):
    print("To podstawowy kolor")
    
elif kolor in ("pomarańczowy", "fioletowy", "zielony"):
    print("To kolor dodatkowy")
    
else:
    print("Nie znam takiego koloru")
