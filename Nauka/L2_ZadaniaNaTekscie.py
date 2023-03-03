print("Zmiana\nlini") # \n schodzi na linijkę niżej


zdanie="dodawanie"
print(zdanie +" tekstu") # żeby łaczyc w princie trzeba użyc +


Duze="ZMIANA liter NA MaŁe"
print(Duze.lower()) # nazwazmienej.lower() zmienia litery na małe w danej zmiennej


Duze="ZMIANA liter NA dUżE"
print(Duze.upper()) # nazwazmienej.upper() zmienia litery na duże w danej zmiennej


czyDuze="ZMIANA liter NA dUżE"
print(czyDuze.isupper()) # nazwazmienej.isupper() sprawdza czy wszystkie litery są duże jesli tak to oddaje wartość true

print(czyDuze.upper().isupper()) # można łaczyć funkcje ze soba ale tylko w ramach jednego printa to działa

print(Duze.islower()) # nazwazmienej.islower() sprawdza czy wszystkie litery są małe jesli tak to oddaje wartość true

print(Duze.lower().islower()) # można łaczyć funkcje ze soba ale tylko w ramach jednego printa to działa


print(len(Duze))    # len() sprawdza długość textu

print(Duze[4]+Duze[2]+Duze[18]+Duze[18]+Duze[3])    # [] w princie po zmiennej wydaje liczbe z miejsca ktore wpisalismy

print(Duze.index("N"))     # Wydaje pierwsze miejsce na którym się znajduje dany znak 
print(Duze.index("liter"))     # Wydaje pierwsze miejsce na którym się znajduje ten ciąg znaków 
#Gdy nie ma znaku w zmiennej python wyrzuca błąd

print(Duze.replace("dUżE", "MaŁe")) # nazwazmienej.replace() zmienia pierwsza wartośc na drugą

#KONTUNUJ KURS OD 38.18 MIN