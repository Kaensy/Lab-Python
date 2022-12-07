from Erori.validation_error import ValidError


class ValidatorNota:
    """
    verifica daca id-ul intreg al notei este mai mic decat 0 si daca nota int nota se afla in intervalul [0,10]
    :return: -
    :raises:ValidError daca id_nota < 0 atunci concateneaza mesajul de eroare "id invalid!\n"
                       daca nota > 10 sau nota < 0 concateneaza mesajul de eroare "nota invalida!\n
                       si seteaza mesajul erorii ValidError la concatenarea de stringuri obtinuta
    """
    def __init__(self):
        self

    def valideaza(self, nota):
        erori = ""
        if nota.get_id_nota() < 0:
            erori += "id invalid!\n"
        if not (0 <= nota.get_nota() <= 10):
            erori += "nota invalida!\n"
        if len(erori) > 0:
            raise ValidError(erori)
