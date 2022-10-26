# 14. oricare doua elemente consecutive au cel putin 2 cifre distincte comune
# 1. x[i] < x[i+1] < ... < x[i+p]


def verificare_vectori_char(a,b):
    # Functia verifica daca elementele a si b au cel putin 2 cifre distincte comune
    # input     : integer a , b
    # output    : True - daca au cel putin 2 cifre distincte comune
    #           : False - daca nu au cel putin 2 cifre distincte comune
    c_a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # vectorul caracteristic al nr a
    c_b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # vectorul caracteristic al nr b
    if a<0:
        a=int(a*-1)
    if b<0:
        b=int(b*-1)
    while a > 0:
        c_a[int(a%10)] = 1
        a = int(a/10)
    while b > 0:
        c_b[int(b%10)] = 1
        b = int(b/10)
    nr_cifre_comune=0
    for el in range(0,9):
        if c_a[el]==1 and c_b[el]==1:
            nr_cifre_comune=nr_cifre_comune+1
    if nr_cifre_comune>1:
        return True
    return False

def verificare_prop_1(a,b):
    # Functia verifica daca nr b este mai mare decat a
    # input     : integer a , b
    # output    : True - a < b
    #           : False - a > b
    if a<b:
        return True
    return False

def verificare_prop_12(a,b):
    # Functia verifica daca nr a si b sunt de semn contrar
    # input     : integer a , b
    # output    : True - a < 0 and b>=0 or a>=0 and b<0
    #           : False - a>=0 and b>=0 or a<0 and b<0
    if  a < 0 and b >= 0  or  a>= 0 and b < 0 :
        return True
    return False

def secventa_proprietatea_14(lista):
    # Functia primeste o lista si returneaza cea mai mare secventa(lista) cu proprietatea p
    # input     : list lista
    # output    : list secventa
    lungime_lista=int(len(lista))
    lungime_secventa_max = 0
    index_stang_salvat = 0
    index_drept_salvat = 0
    for i in range(lungime_lista - 1):
        lungime_secventa = 0
        index_stang = i
        index_drept = i + 1
        while verificare_vectori_char(int(lista[index_stang]),int(lista[index_drept])) and index_drept < lungime_lista - 1:
            index_stang = index_stang + 1
            index_drept = index_drept + 1
            lungime_secventa = lungime_secventa + 1
        if verificare_vectori_char(int(lista[index_stang]), int(lista[index_drept])):
            index_stang = index_stang + 1
            index_drept = index_drept + 1
            lungime_secventa = lungime_secventa + 1
        if lungime_secventa > lungime_secventa_max:
            lungime_secventa_max = lungime_secventa
            index_stang_salvat = i
            index_drept_salvat = index_drept
    if lungime_secventa_max > 0:
        return lista[index_stang_salvat:index_drept_salvat]
    else:
        return []

def secventa_proprietatea_1(lista):
    # Functia primeste o lista si returneaza secventa de lungime max cu proprietatea 1
    # input     : list lista
    # output    : list secventa
    lungime_lista=int(len(lista))
    lungime_secventa_max = 0
    index_stang_salvat = 0
    index_drept_salvat = 0
    for i in range(lungime_lista - 1):
        lungime_secventa = 0
        index_stang = i
        index_drept = i + 1
        while verificare_prop_1(int(lista[index_stang]), int(lista[index_drept])) and index_drept < lungime_lista - 1:
            lungime_secventa = lungime_secventa + 1
            index_stang = index_stang + 1
            index_drept = index_drept + 1
        if verificare_prop_1(int(lista[index_stang]), int(lista[index_drept])):
            index_stang = index_stang + 1
            index_drept = index_drept + 1
            lungime_secventa = lungime_secventa + 1
        if lungime_secventa > lungime_secventa_max:
            lungime_secventa_max = lungime_secventa
            index_stang_salvat = i
            index_drept_salvat = index_drept
    if lungime_secventa_max > 0:
        return lista[index_stang_salvat:index_drept_salvat]
    else:
        return []
def secventa_proprietatea_12(lista):
    lungime_secventa_max = 0
    index_stang_salvat = 0
    index_drept_salvat = 0
    for i in range(lungime_lista - 1):
        lungime_secventa = 0
        index_stang = i
        index_drept = i + 1
        while verificare_prop_12(int(lista[index_stang]), int(lista[index_drept])) and index_drept < lungime_lista - 1:
            lungime_secventa = lungime_secventa + 1
            index_stang = index_stang + 1
            index_drept = index_drept + 1
        if verificare_prop_1(int(lista[index_stang]), int(lista[index_drept])):
            index_stang = index_stang + 1
            index_drept = index_drept + 1
            lungime_secventa = lungime_secventa + 1
        if lungime_secventa > lungime_secventa_max:
            lungime_secventa_max = lungime_secventa
            index_stang_salvat = i
            index_drept_salvat = index_drept
    if lungime_secventa_max > 0:
        return lista[index_stang_salvat:index_drept_salvat]
    else:
        return []

def test_secventa_proprietatea_14():
    assert secventa_proprietatea_14([12,21,33]) == [12,21]
    assert secventa_proprietatea_14([12,23,34]) == []
    assert secventa_proprietatea_14([0,-12,213,-331,0]) == [-12,213,-331]
    assert secventa_proprietatea_14([12,21,12]) == []

afisare="""
1.Citire lista nr intregi ( Numere despartite prin spatiu )
2.(14) Secventa de lungime maxima cu proprietatea ca oricare doua elemente consecutive au cel putin 2 cifre distincte comune
3.(1) Secventa de lungime maxima cu proprietatea x[i] < x[i+1] < ... < x[i+p]
4.(12) Secventa de lungime maxima cu proprietatea ca oricare doua elemente consecutive sunt de semne contrare
5.Exit
"""

# test_secventa_proprietatea_14()

choice=int(input(afisare))
lista_declarata=False
while choice!=5:
    if choice==1:
        lista=input("Lista : ")
        lista=lista.split(" ")
        lungime_lista=int(len(lista))
        lista_declarata=True
    elif choice==2 and lista_declarata:
        secventa=secventa_proprietatea_14(lista)
        print(secventa)
    elif choice==3 and lista_declarata:
        secventa=secventa_proprietatea_1(lista)
        print(secventa)
    elif choice==4 and lista_declarata:
        secventa=secventa_proprietatea_12(lista)
        print(secventa)
    elif lista_declarata==False:
        print("Cititi lista")
    choice=int(input(afisare))

