from domain.pachet import egal_pachete, set_datainceput_pachet, set_datasfarsit_pachet, set_destinatie_pachet, \
    set_pret_pachet


def adauga_pachet_lista(l,pachet):
    """
    adauga la lista l de pachete unice pachetul pachet daca pachet nu apare deja in lista l
    :param l: lista de pachete unice
    :param pachet: pachet
    :return: - ( l' = l U {pachet} , daca pachetul pachet nu apare in lista l
    :raise: ValueError cu mesajul string "pachet invalid!\n" daca pachetul pachet apare deja in lista l
    """
    for _pachet in l:
        if egal_pachete(_pachet,pachet):
            raise ValueError("pachet invalid!\n")
    l.append(pachet)

def numar_pachete_lista(l):
    """
    returneaza numarul de pachete pachet unice din lista l
    :param l: lista l de pachete pachet unice
    :return: rez - int : numarul de pachete pachet unice din lista l
    """
    return len(l)

def get_all_pachete(l):
    """
    returneaza lista l' a tuturor pachetelor pachet unice din lista l
    :param l: lista l de pachete pachet unice
    :return: l' = l[:]
    """
    return l[:]

def modificare_pachet(pachet, data_inceput, data_sfarsit, destinatie, pret):
    """
    modifica valorile pachetului pachet cu noile valori data_inceput, data_sfarsit, destinatie, pret
    :param pachet: pachet
    :param data_inceput: date
    :param data_sfarsit: date
    :param destinatie: string
    :param pret: int
    :return: - ( modifica valorile unui pachet )
    """
    set_datainceput_pachet(pachet, data_inceput)
    set_datasfarsit_pachet(pachet, data_sfarsit)
    set_destinatie_pachet(pachet, destinatie)
    set_pret_pachet(pachet, pret)

def stergere_pachet_index(pachete,index):
    """
    sterge pachetul cu index index din lista de pachete pachete
    :param pachete: list de pachete unice
    :param index: int
    :return: - ( sterge pachetul de index index din lista de pachete )
    """
    del pachete[index]