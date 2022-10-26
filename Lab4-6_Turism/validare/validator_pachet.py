import datetime
from domain.pachet import get_datainceput_pachet, get_datasfarsit_pachet, get_destinatie_pachet, get_pret_pachet


def valideaza_pachet(pachet):
    """
    verifica daca data data_inceput a pachetului pachet este >=data curenta, daca data data_sfarsit a pachetului pachet este >= data data_inceput a pachetului pachet,
    daca destinatia string destinatie a pachetului pachet este nevid si pretul intreg pret al pachetului pachet >=0
    :param pachet: pachet
    :return: -
    :raises:ValueError daca data_inceput < data curenta atunci concateneaza mesajul de eroare "data_inceput invalida!\n"
                       daca data_sfarshit < data_inceput atunci concateneaza mesajul de eroare "data_sfarsit invalida!\n"
                       daca destinatia este vida concateneaza mesajul de eroare "destinatie invalida!\n"
                       daca pretul < 0 concateneaza mesajul de eroare "pret invalid!\n"
                       si seteaza mesajul erorii ValueError la concatenarea de stringuri obtinuta
    """
    erori=""
    if get_datainceput_pachet(pachet)< datetime.date.today():
        erori += "data_inceput invalida!\n"
    if get_datasfarsit_pachet(pachet)<get_datainceput_pachet(pachet):
        erori += "data_sfarsit invalida!\n"
    if get_destinatie_pachet(pachet)=="":
        erori += "destinatie invalida!\n"
    if get_pret_pachet(pachet)<0:
        erori += "pret invalid!\n"
    if len(erori)>0:
        raise ValueError(erori)

