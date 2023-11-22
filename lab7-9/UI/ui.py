from service.service import ServiceUtils

class UI(ServiceUtils):
    def __init__():
        pass
    #filme: <id>,<titlu>,<descriere>,<gen>
    @staticmethod
    def get_film_ui():
        titlu = (input)("Ce titlu are filmul ?")
        descriere = (input)("Ce descriere are filmul ? ")
        gen = (input)("Ce gen are filmul ? ")
        return (titlu , descriere , gen)
    
    #clienți: <id>, <nume>, <CNP>
    @staticmethod
    def get_client_ui():
        nume = (input)("Ce nume are clientul ? ")
        cnp = (input)("Ce cnp are clientul ? ")
        cnp = (int)(cnp)
        return(nume , cnp)
    
    @staticmethod
    def get_optiune_ui():
        optiune = (input)("Ce optiune alegi ? ")
        return (int)(optiune)
    @staticmethod
    def afiseza_meniu_ui():
        print("1 . Afiseaza lista clienti ")
        print("2 . Afiseaza lista filme ")
        print("3 . Adauga Client")
        print("4 . Adauga Film ")
        print("5 . Sterge Client")
        print("6 . Sterge Film")
        print("7 . Modifica Client")
        print("8 . Modifica Film")

    @staticmethod
    def get_client_id_ui():
        id = (input)("La ce id vrei sa faci operatie la un client ? ")
        id = (int)(id)
        return id
    @staticmethod
    def get_film_id_ui():
        id = (input)("La ce id vrei sa faci operatie la un film ? ")
        id = (int)(id)
        return id
    @staticmethod
    def print_client_ui(client):
        id = client.get_client_id()
        nume = client.get_nume()
        cnp = client.get_cnp()
        print(id , nume , cnp)
    @staticmethod
    def print_film_ui(film):
        id = film.get_film_id()
        titlu = film.get_titlu()
        descriere = film.get_descriere()
        gen = film.get_gen()
        print(f"Id-ul fillmului este = {id}")
        print(f"Titlul filmului este = {titlu}")
        print(f"Descrierea filmului este = {descriere}")
        print(f"Genul filmului este = {gen}")