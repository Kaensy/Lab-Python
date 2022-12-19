from Validator.validator_student import ValidatorStudent
from Validator.validator_materie import ValidatorMaterie
from Validator.validator_nota import ValidatorNota
from Repository.file_repo_studenti import FileRepoStudenti
from Repository.file_repo_materii import FileRepoMaterii
from Repository.file_repo_note import FileRepoNote
from Business.service_studenti import ServiceStudenti
from Business.service_materii import ServiceMaterii
from Business.service_note import ServiceNote
from Teste.teste import Teste
from Prezentare.ui import UI

if __name__ == '__main__':
    validator_student = ValidatorStudent()
    validator_materie = ValidatorMaterie()
    validator_nota = ValidatorNota()
    cale_fisier_studenti = "studenti.txt"
    cale_fisier_materii = "materii.txt"
    cale_fisier_note = "note.txt"
    repo_studenti = FileRepoStudenti(cale_fisier_studenti)
    repo_materii = FileRepoMaterii(cale_fisier_materii)
    repo_note = FileRepoNote(cale_fisier_note)
    service_studenti = ServiceStudenti(validator_student, repo_studenti)
    service_materii = ServiceMaterii(validator_materie, repo_materii)
    service_note = ServiceNote(validator_nota, repo_note, repo_studenti, repo_materii)
    ui = UI(service_studenti, service_materii, service_note)
    test = Teste()
    test.run()
    ui.run()
