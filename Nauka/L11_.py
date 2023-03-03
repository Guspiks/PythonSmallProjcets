#-----------listy 2d i zagnmieżdżanie pętl----------
number_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[2][1])

for row in number_grid:
    for col in row:
        print(col)

#----------Translator-----------

def translate(phrase):
    translation=""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation=translation+"g"
        else:
            translation=translation+letter
    return translation

print(translate(input("podaj słowo: ")))

#---------------wyjątki------------------
try:
    number=int(input("wprowadź liczbę"))
    print(number)
except:
    print("Zła wartość")
#kontunuj od 3:12:41