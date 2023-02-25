from Erori.valid_error import ValidError

class ValidatorProdus:

    def valideaza(self, produs):
        erori = ""
        if produs.get_id_produs() <0 :
            erori += "id invalid!\n"
        if produs.get_denumire_produs() == "":
            erori += "denumire invalida!\n"
        if produs.get_pret_produs() <0 :
            erori += "pret invalid!\n"
        if len(erori) >0:
            raise ValidError(erori)