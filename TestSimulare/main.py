from Repository.file_repo_costume import FileRepoCostume
from Business.service_costume import ServiceCostume
from Teste.teste import Teste
from Prezentare.ui import UI


def main():
    cale_fisier = "costume.txt"
    repo = FileRepoCostume(cale_fisier)
    service = ServiceCostume(repo)
    ui = UI(service)
    test = Teste()
    test.run()
    ui.run()


main()