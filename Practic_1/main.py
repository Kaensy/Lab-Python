from Prezentare.ui import UI
from Repository.file_repo_produse import FileRepoProduse
from Business.service_produs import ServiceProduse
from Validator.validator_produs import ValidatorProdus
from Teste.teste import teste


if __name__ == "__main__":
    validator_produs = ValidatorProdus()
    cale_fisier = "produse.txt"
    repo_produse = FileRepoProduse(cale_fisier)
    service_produse = ServiceProduse(validator_produs, repo_produse)
    ui = UI(service_produse)
    test = teste()
    #test.run()
    ui.run()