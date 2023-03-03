friends=["Kyle", "Karen", "Dżejsonek"]
lucky_numbers=[1,4,53,69,88]
friends[1]="Jesika" #aktualizuje wartości w liscie
print(friends[1])
# można użyć l;iczb ujemnych do wybierania z listy od końca
# liczba i znaczek: np. 2: wydaje wartość z 2 pozycji i wszystko co jest po niej
#można też użyć zakresów czyli np. 1:3 nie uwzględniając 3
#----------------------funkcje list--------------------
friends.append("marek") #dodaje wartość na koniec listy
friends.insert(1, "Kelly FUNK") # wstawia wartość do listy w podane miejsce
friends.remove("Jesika") #usuwa wskazane wartości
friends.pop() #usuwa oistatni element listy
friends.sort() #sortuje alfabetycznie
print(friends.index("Kyle")) # wyrzuca miejsce elementu
print(friends.count("Kyle")) # wyrzuca ilość elementów
print(friends)
friends.clear()
friends.extend(lucky_numbers) # dodaje liste lucky numbers do friends
friends.reverse() #zmienia kolejność od najwiekszej do najmniejszej
friends2=friends.copy()
print(friends)
print(friends2)
#kontynuj od 1:19:00
#----------------krotki------------
kordynacje=(4,5)
print(kordynacje)
#krotki to listy których nie można edytować