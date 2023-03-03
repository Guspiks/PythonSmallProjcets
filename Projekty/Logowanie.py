login=""
haslo=""
w_login=""
w_haslo=""
zalogowany=False
while zalogowany==False:
    if login=="" or haslo=="":
        print("Nie zgodność w danych proszę zresetować login oraz hasło")
        login=input("proszę założyć login: ")
        haslo=input("proszę założyć hasło: ")
    elif login!="" and haslo!="":
        w_login=input("proszę podać login: ")
        w_haslo=input("prosze podać hasło: ")
        if w_login==login and w_haslo==haslo:
            print("witaj "+login+" twoje hasło to "+haslo)
            zalogowany=True
        else:
            print("Prosze podać odpowiednie dane")
    else:
        print("Prosze podać odpowiednie dane")