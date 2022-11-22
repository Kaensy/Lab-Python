from Erori.validation_error import ValidError


class ValidatorMaterie:
    """
    verifica daca id-ul intreg al materiei este mai mic decat 0, daca numele string al materiei este vid, daca numele string al profesorului este vid
    :return: -
    :raises:ValidError daca id_materie < 0 atunci concateneaza mesajul de eroare "id invalid!\n"
                       daca nume_materie == "" atunci concateneaza mesajul de eroare "nume materie invalid!\n"
                       daca nume_profesor == "" atunci concateneaza mesajul de eroare "nume profesor invalid!\n"
                       si seteaza mesajul erorii ValidError la concatenarea de stringuri obtinuta
    """
    def __init__(self):
        self

    def valideaza(self, materie):
        erori = ""
        if materie.get_id_materie() < 0:
            erori += "id invalid!\n"
        if materie.get_nume_materie() == "":
            erori += "nume materie invalid!\n"
        if materie.get_nume_profesor() == "":
            erori += "nume profesor invalid!\n"
        if len(erori) > 0:
            raise ValidError(erori)

    def valideaza_id_materie(self, id_materie):
        erori = ""
        if id_materie < 0:
            erori += "id invalid!\n"
        if len(erori) > 0 :
            raise ValidError(erori)
