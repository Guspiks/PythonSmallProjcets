wart=10.0;
x=-75.0;
y=-75.0;

 
for index in range(16):
    for indox in range(15):
        print("indox="+str(indox))
        x=x+wart
        print("x="+str(x))
    print("index="+str(index))
    print("y="+str(y))
    y=y+10
    wart=-1*wart

