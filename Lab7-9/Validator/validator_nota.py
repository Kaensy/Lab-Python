from Erori.validation_error import ValidError


class ValidatorNota:

    def __init__(self):
        self

    def valideaza(self, nota):
        erori = ""
        if nota.get_id_nota()<0:
            erori += "id invalid!\n"
        if not (0 < nota.get_nota() < 10):
            erori += "nota invalida!\n"
        if len(erori)>0:
            raise ValidError(erori)