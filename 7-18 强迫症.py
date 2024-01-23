date=input()
if len(date)==6:
    a=int(date)//100
    b=int(date)%100
    if b>9:
        print("%d-%d"%(a,b))
    else:
        print("%d-0%d"%(a,b))
else:
    a=int(date)//100
    b=int(date)%100
    if b>9:
        if a>21:
            print("19%d-%d"%(a,b))
        elif a<10:
            print("200%d-%d"%(a,b))
        else:
            print("20%d-%d"%(a,b))
    else:
        if a>21:
            print("19%d-0%d"%(a,b))
        elif a<10:
            print("200%d-0%d"%(a,b))
        else:
            print("20%d-0%d"%(a,b))