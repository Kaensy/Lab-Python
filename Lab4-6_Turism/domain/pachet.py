def creeaza_pachet(data_inceput,data_sfarsit,destinatie,pret):
    """
    creeaza un pachet pe baza unei date date data_inceput, a unei date date data_sfarsit, a unui string destinatie si a unui integer pret
    :param data_inceput: date
    :param data_sfarsit: date
    :param destinatie: string
    :param pret: integer
    :return: rez - un pachet cu data data data_inceput, data data data_sfarsit, destinatia string destinatie si pretul integer pret
    """
    return[data_inceput,data_sfarsit,destinatie,pret]

def get_datainceput_pachet(pachet):
    """
    returneaza data date data_inceput a pachetului pachet
    :param pachet: pachet
    :return: rez : date - data_inceput a pachetului pachet
    """
    return pachet[0]

def get_datasfarsit_pachet(pachet):
    """
    returneaza data date data_sfarsit a pachetului pachet
    :param pachet: pachet
    :return: rez : date - data_sfarsit a pachetului pachet
    """
    return pachet[1]

def get_destinatie_pachet(pachet):
    """
    returneaza destinatia string destinatie a pachetului pachet
    :param pachet: pachet
    :return: rez : string - destinatie a pachetului pachet
    """
    return pachet[2]

def get_pret_pachet(pachet):
    """
    returneaza pretul int pret a pachetului pachet
    :param pachet: pachet
    :return: rez : int - pret a pachetului pachet
    """
    return pachet[3]

def set_datainceput_pachet(pachet,data_inceput_noua):
    """
    seteaza data_inceput date a pachetului pachet la noul date data_inceput_noua
    :param pachet: pachet
    :param data_inceput: date
    :return: - ( data_inceput date are data data_inceput_noua ) 
    """
    pachet[0]=data_inceput_noua

def set_datasfarsit_pachet(pachet,data_sfarsit_noua):
    """
    seteaza data_sfarsit date a pachetului pachet la noul date data_sfarsit noua
    :param pachet: pachet
    :param data_sfarsit_noua: date 
    :return: - ( data_sfarsit date are data data_sfarsit_noua )
    """
    pachet[1]=data_sfarsit_noua

def set_destinatie_pachet(pachet,destinatie_noua):
    """
    seteaza destinatia string a pachetului pachet la noul string destinatie_noua
    :param pachet: pachet
    :param destinatie_noua: string 
    :return: - ( destinatie string are destinatia string destinatie_noua )
    """
    pachet[2]=destinatie_noua

def set_pret_pachet(pachet,pret_nou):
    """
    seteaza pretul intreg pret a pachetului pachet la noul intreg pret_nou
    :param pachet: pachet
    :param pret_nou: integer
    :return: - ( pretul intreg pret primeste valoarea intreaga pret_nou )
    """
    pachet[3]=pret_nou

def egal_pachete(pachet_a,pachet_b):
    """
    verifica daca pachetul pachet_a si pachetul pachet_b sunt acelasi prin verificarea fiecarei valori
    :param pachet_a: pachet
    :param pachet_b: pachet
    :return: rez - bool : True daca pachetele sunt identice
                          False daca pachetele nu sunt identice
    """
    return pachet_a == pachet_b

def to_string_pachet(pachet):
    """
    returneaza valorile pachetului intr-un string
    :param pachet: pachet
    :return:
    """
    return f"{pachet[0]} -> {pachet[1]}, {pachet[2]} {pachet[3]} lei"