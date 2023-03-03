# #---------------------------while_loop---------------------------------
i=1
while i<=10:
    print(i)
    i += 1

# print("Koniec")
# #------------------------przykład---------------------
ukryte_słowo="JP2"
odpowiedz=""
guess_count=0
guess_limit=3
out_of_guesses=False
while odpowiedz!=ukryte_słowo and not(out_of_guesses):
    if guess_count<guess_limit:
        odpowiedz=input("Wprowadź odpowiedź:")
        guess_count+=1
    else:
        out_of_guesses=True
if out_of_guesses==False:
    print("Udało ci się!")
else:
    print("nie udało sie nie masz juz prób")
# #-----------------------For_Loop-----------------------------
for letter in "Jan Paweł 2":
    print(letter) 
friends=["jim","kevin","maciek"]
for friend in friends:
    print(friend)
for index in range(10):
    print(index)
for indox in range(2,9):
    print(indox)
for indax in range(len(friends)):
    print(friends[indax])
#--------------------------Zadanie-----------------------
def raise_to_power(base_num, pow_num):
    result=1
    for index in range(pow_num):
        result=result*base_num
    return result

print(raise_to_power(3,8))