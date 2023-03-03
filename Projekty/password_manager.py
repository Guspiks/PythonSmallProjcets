from asyncore import write
from cryptography.fernet import Fernet

def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("key.key","rb")
    key=file.read()
    file.close()
    return key

master_pwd=input("Podaj master-pasword? ")
key=load_key()+master_pwd.encode()
fer=Fernet(key)

def view():
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            data=line.rstrip()
            user, passw=data.split("|")
            print("User:", user, ", Password:", fer.decrypt(passw.encode()).decode())


def add():
    name=input("Account name: ")
    pwd=input("Password: ")

    with open("passwords.txt","a") as f:
        f.write(name+"|"+fer.encrypt(pwd.encode()).decode()+"\n")


while True:
    mode=input("Chcesz dodać nowe hasło czy wyświetlić wszystkie(add, view)?, by wyjść wpisz q: ").lower()

    if mode=="q":
        break

    if mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("Nieprawidłowy tryb.")
        continue