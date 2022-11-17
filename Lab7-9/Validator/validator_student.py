from Erori.validation_error import ValidError


class ValidatorStudent:

    def __init__(self):
        self

    def valideaza(self, student):
        erori = ""
        if student.getID_student()<0:
            erori += "id invalid!\n"
        if student.getNume()=="":
            erori += "nume invalid!\n"
        if len(erori)>0:
            raise ValidError(erori)