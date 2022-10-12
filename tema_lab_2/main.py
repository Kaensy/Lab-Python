# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import date,datetime

nr =int(input("Ex Disponibile : 1 2 11 \nNr Problemei : "))

if nr==1:
    n = int(input("n="))
    gasit=False
    while gasit==False:
        n +=1
        prim=True
        for d in range(2,n):
            if n%d==0:
                prim=False
        if prim==True:
            gasit=True
            print(n)
elif nr==2:
    corect=False
    ajutor=False
    while corect==False:
        zi=input("Ziua Nasterii : ")
        luna=input("Luna Nasterii : ")
        an=input("Anul Nasterii : ")
        months=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        if luna in months:
            number=months.index(luna)%12+1
            luna=number
            ajutor=True
        elif luna.isdecimal():
            luna=int(luna)
            ajutor=True
        if luna in range(0,12) and ajutor==True:
                data_nasterii=an+"-"+str(luna)+"-"+zi
                d1 = datetime.strptime(data_nasterii, "%Y-%m-%d")
                today = str(date.today())
                d2 = datetime.strptime(today, "%Y-%m-%d")
                raspuns = d2 - d1
                print(f'Varsta Dvs in zile este de {raspuns.days} de zile')
                corect=True
        else:
            print('U suck at writing months')
elif nr==11:
    a = int(input("a = "))
    b = int(input("b = "))
    ca=[0,0,0,0,0,0,0,0,0,0]
    cb=[0,0,0,0,0,0,0,0,0,0]
    while a > 0:
        ca[int(a%10)]=1
        a=int(a/10)
    while b > 0:
        cb[int(b%10)]=1
        b=int(b/10)
    if ca==cb:
        print("Nr a si b au proprietatea P")
    else:
        print("Nr a si b nu au proprietatea P")





