#-----------------------------kalkulator-------------------------------
num1=float(input("podaj pierwsza liczbe: "))
op=input("Wpisz operator: ")
num2=float(input("podaj drugą liczbe: "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    if num2 == 0:
        print("nie dziel przez zero cholero")
    else:
        print(num1/num2)
else:
    print("podałeś nieprawidłowe dane")
#-----------------------------Słowniki--------------------------------
monthConversions={
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
print(monthConversions.get("Kun", "Brak poprawnej wartości"))