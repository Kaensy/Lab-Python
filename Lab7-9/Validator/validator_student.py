from Erori.validation_error import ValidError


class ValidatorStudent:
    """
    verifica daca id-ul intreg al studentului este mai mic decat 0 si daca numele string al studentului este vid
    :return: -
    :raises:ValidError daca id_student < 0 atunci concateneaza mesajul de eroare "id invalid!\n"
                       daca nume == "" atunci concateneaza mesajul de eroare "nume invalid!\n"
                       si seteaza mesajul erorii ValidError la concatenarea de stringuri obtinuta
    """
    def __init__(self):
        self

    def valideaza(self, student):
        erori = ""
        if student.getID_student() < 0:
            erori += "id invalid!\n"
        if student.getNume() == "":
            erori += "nume invalid!\n"
        if len(erori) > 0:
            raise ValidError(erori)

    def valideaza_id_student(self, id_student):
        erori = ""
        if id_student < 0:
            erori += "id invalid!\n"
        if len(erori) > 0 :
            raise ValidError(erori)
