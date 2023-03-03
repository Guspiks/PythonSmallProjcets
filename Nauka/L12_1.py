#-----------------czytanie z pliku-----------------------
abc_plik=open("abc.txt", "r+")
print(abc_plik.read())
abc_plik.close()

abc_plik=open("abc.txt", "r+")
print(abc_plik.readline())
abc_plik.close()

abc_plik=open("abc.txt", "r+")
print(abc_plik.readlines()[1])
abc_plik.close()

abc_plik=open("abc.txt", "r+")
for employee in abc_plik.readlines():
    print(employee)
abc_plik.close()
#----------------wpisywanie do pliku----------------------
abc_plik=open("abc.txt", "a")  # a dodaje tekst na koniec
abc_plik.write("\nMicheal - Manager")
abc_plik.close()

abc_plik=open("abc1.txt", "w") # w nadpisuje i może stworzyć nowy plik
abc_plik.write("\nMicheal - Manager")
abc_plik.close()
