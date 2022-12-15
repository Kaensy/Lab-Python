from Validator.validator_student import ValidatorStudent
from Validator.validator_materie import ValidatorMaterie
from Validator.validator_nota import ValidatorNota
from Repository.file_repo_studenti import FileRepoStudenti
from Repository.repo_materii import RepoMaterii
from Repository.repo_note import RepoNote
from Business.service_studenti import ServiceStudenti
from Business.service_materii import ServiceMaterii
from Business.service_note import ServiceNote
from Teste.teste import Teste
from Teste.teste_filerepo import TesteFileRepo
from Prezentare.ui import UI

if __name__ == '__main__':
    validator_student = ValidatorStudent()
    validator_materie = ValidatorMaterie()
    validator_nota = ValidatorNota()
    cale_fisier = "studenti.txt"
    repo_studenti = FileRepoStudenti(cale_fisier)
    repo_materii = RepoMaterii()
    repo_note = RepoNote()
    service_studenti = ServiceStudenti(validator_student, repo_studenti)
    service_materii = ServiceMaterii(validator_materie, repo_materii)
    service_note = ServiceNote(validator_nota, repo_note, repo_studenti, repo_materii)
    ui = UI(service_studenti, service_materii, service_note)
    test = Teste()
    test.run()
    test_fisier = TesteFileRepo()
    test_fisier.run_all_tests()
    ui.run()
