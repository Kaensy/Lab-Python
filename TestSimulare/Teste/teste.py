from Domain.costum import Costum
from Repository.repo_costume import RepoCostume
from Business.service_costume import ServiceCostume
from Erori.repo_error import RepoError


class Teste:

    def __init__(self):
        pass

    def run(self):
        self.ruleaza_teste_domain()
        print("Teste Domain trecute cu succes")
        self.ruleaza_teste_repo()
        print("Teste Repo trecute cu succes")
        self.ruleaza_teste_service()
        print("Teste Service rulate cu succes")

    def ruleaza_teste_domain(self):
        costum = Costum(1, "Rochie Vrajitoare Rosie", "Halloween", 300, "False")
        costum_acelasi = Costum(1, "Rochie", "Iarna", 250, "True")
        costum_altul = Costum(2, "Costum", "Vara", 100, "True")
        assert costum_altul < costum
        assert costum.get_id_costum() == 1
        assert costum.get_denumire_costum() == "Rochie Vrajitoare Rosie"
        assert costum.get_tematica_costum() == "Halloween"
        assert costum.get_pret_costum() == 300
        assert costum.get_disponibilitate_costum() == "False"

        assert costum == costum_acelasi
        assert not costum == costum_altul

        costum.set_denumire_costum("Asta")
        costum.set_tematica_costum("BD")
        costum.set_pret_costum(200)
        costum.set_disponibilitate_costum("True")

        assert costum.get_denumire_costum() == "Asta"
        assert costum.get_tematica_costum() == "BD"
        assert costum.get_pret_costum() == 200
        assert costum.get_disponibilitate_costum() == "True"

        assert str(costum) == "1,Asta,BD,200,True"

    def ruleaza_teste_repo(self):
        repo_costume = RepoCostume()
        costum = Costum(1, "Rochie Vrajitoare Rosie", "Halloween", 300, "False")
        costum_acelasi = Costum(1, "Rochie  Rosie", "Hallo", 300, "False")

        assert len(repo_costume) == 0
        repo_costume.adauga_costum(costum)
        assert len(repo_costume) == 1

        try:
            repo_costume.adauga_costum(costum_acelasi)
            assert False
        except RepoError as re:
            assert str(re) == "costum existent!"

        assert str(repo_costume.get_all()[0]) == "1,Rochie Vrajitoare Rosie,Halloween,300,False"

        assert repo_costume.cauta_costum_dupa_id(1).get_denumire_costum() == costum.get_denumire_costum()

    def ruleaza_teste_service(self):
        repo_costume = RepoCostume()
        service_costume = ServiceCostume(repo_costume)
        assert len(service_costume.get_all_costume()) == 0
        service_costume.adauga_costum_service(1, "Rochie Vrajitoare Rosie", "Halloween", 300, "True")
        assert len(service_costume.get_all_costume()) == 1

        service_costume.adauga_costum_service(2, "Rochie Vrajitoare Galbena", "Halloween", 299, "True")
        service_costume.adauga_costum_service(3, "Rochie Vrajitoare Verde", "Halloween", 350, "True")
        service_costume.adauga_costum_service(4, "Rochie Vrajitoare Albastra", "Halloween", 200, "False")

        costume_tematica_sortate = service_costume.all_costume_tematica_service("Halloween")
        assert str(costume_tematica_sortate[0]) == "2,Rochie Vrajitoare Galbena,Halloween,299,True"
        assert str(costume_tematica_sortate[1]) == "1,Rochie Vrajitoare Rosie,Halloween,300,True"
        assert str(costume_tematica_sortate[2]) == "3,Rochie Vrajitoare Verde,Halloween,350,True"


