from domain.pachet import egal_pachete, set_datainceput_pachet, set_datasfarsit_pachet, set_destinatie_pachet, \
    set_pret_pachet


def adauga_pachet_lista(l,undo, pachet):
    """
    adauga la dictionarul l de pachete unice pachetul pachet daca pachet nu apare deja in dictionarul l
    :param l: dictionar de pachete unice
    :param pachet: pachet
    :return: - ( l' = l U {pachet} , daca pachetul pachet nu apare in dictionarul l
    :raise: ValueError cu mesajul string "pachet invalid!\n" daca pachetul pachet apare deja in dictionarul l
    """
    for key in l:
        if egal_pachete(l[key], pachet):
            raise ValueError("pachet invalid!\n")
    nr = numar_pachete_lista(l)+1
    if nr in l:
        nr +=1
    l[nr] = pachet
    undo.append(lambda:stergere_pachet_index(l,nr))


def adauga_pachet_lista_faraundo(l, pachet):
    """
    adauga la dictionarul l de pachete unice pachetul pachet daca pachet nu apare deja in dictionarul l
    :param l: dictionar de pachete unice
    :param pachet: pachet
    :return: - ( l' = l U {pachet} , daca pachetul pachet nu apare in dictionarul l
    :raise: ValueError cu mesajul string "pachet invalid!\n" daca pachetul pachet apare deja in dictionarul l
    """
    nr = numar_pachete_lista(l)+1
    l[nr] = pachet

def numar_pachete_lista(l):
    """
    returneaza numarul de pachete pachet unice din dictionarul l
    :param l: dictionar de pachete pachet unice
    :return: rez - int : numarul de pachete pachet unice din dictionarul l
    """
    return len(l)

def get_all_pachete(l):
    """
    returneaza dictionarul l' a tuturor pachetelor pachet unice din dictionarul l
    :param l: dictionar de pachete pachet unice
    :return: l' = l[:]
    """
    return l

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
    sterge pachetul cu index index din dictionarul de pachete pachete
    :param pachete: dictionar de pachete unice
    :param index: int
    :return: - ( sterge pachetul de index index din dictionarul de pachete )
    """
    pachete.pop(index)