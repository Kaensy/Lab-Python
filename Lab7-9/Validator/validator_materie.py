from Erori.validation_error import ValidError


class ValidatorMaterie:

    def __init__(self):
        self

    def valideaza(self, materie):
        erori = ""
        if materie.get_id_materie()<0:
            erori += "id invalid!\n"
        if materie.get_nume_materie()=="":
            erori += "nume materie invalid!\n"
        if materie.get_nume_profesor()=="":
            erori += "nume profesor invalid!\n"
        if len(erori)>0:
            raise ValidError(erori)