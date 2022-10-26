from domain.pachet import creeaza_pachet
from infrastructura.repository_persoane import adauga_pachet_lista
from validare.validator_pachet import valideaza_pachet


def adauga_pachet_service(l,data_inceput,data_sfarsit,destinatie,pret):
    """
    creaza un pachet pe baza date-ului data_inceput, a date-ului data_sfarsit, a string-ului destinatie si a intregului pret
    valideaza pachetul creat si daca e valid il adauga in lista de pachete unice l doar daca pachetul nu apare deja in lista l
    :param l: lista
    :param data_inceput: date
    :param data_sfarsit: date
    :param destinatie: string
    :param pret: int
    :return: - ( l' = l U pachet - daca validarea si adaugarea pachetului se face cu success )
    :raises: ValueError cu mesajele de validare daca pachetul creat e invalid
                        cu mesajul "pachet invalid!\n" daca pachetul exista deja in lista l
    """
    pachet = creeaza_pachet(data_inceput,data_sfarsit,destinatie,pret)
    valideaza_pachet(pachet)
    adauga_pachet_lista(l,pachet)

def numar_pachete_service(l):
    """
    returneaza numarul de pachete pachet din lista l de pachete unice
    :param l: lista
    :return: rez - int : nr de pachete unice din lista l
    """
    return len(l)
