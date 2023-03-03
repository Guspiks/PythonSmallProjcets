import random

male_litery="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,r,s,q,t,u,v,w,x,y,z,"
duze_litery="A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,R,S,Q,T,U,V,W,X,Y,Z,"
liczby="1,2,3,4,5,6,7,8,9,0,"
symbole="!,@,#,$,%,^,&,*,(,)"
znaki=male_litery+duze_litery+liczby+symbole
roz=znaki.split(",")    

n=int(input("Podaj długość hasła jakie potrzebujesz?: "))

def generator(lenght):
    haslo=""
    for _ in range(lenght):
        miejsce=random.randint(0,71)
        haslo=str(haslo+roz[miejsce])
    print(haslo)

generator(n)