#kod musi być z tabowanay inaczej nie bedzie go wliczał do funkcjiu 
def powitanie(nazwa, wiek):
    print("Witaj "+nazwa+" twoja gwarancja na życie wygasła w wieku: "+wiek)

powitanie("Janusz Korwin Mikke","Za stary")
powitanie("Ndrej DUDU","45")

#-------------return--------------
def cube(num):
    return num*num*num
wynik=cube(3)
print(wynik)

#------------if statmants---------------
is_male= True
is_tall= False
if is_male or is_tall:
    print("you are a male, tall or both")
else:
    print("u r samll fat femoid")

if is_male and is_tall:
    print("you are a male and tall")
else:
    print("u r not meeting the crtiteria")

if is_male and is_tall:
    print("you are a male and tall")
elif is_male and not(is_tall):
    print("you are a male and short")
else:
    print("u r not meeting the crtiteria")

#---------------porównanie-----------------------

def max_num(num1,num2,num3):
    if num1 >= num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3

print(max_num(69,88,420))

#kontynuj od 2:00:37