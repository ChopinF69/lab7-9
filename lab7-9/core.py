from service.service import ServiceUtils
from UI.ui import UI
from repository.repo import Film , Client
from domain.utils import gestiuneClienti
def main():
    print("Salut aste sunt optiunile : ")
    UI.afiseza_meniu_ui()

    indexFilm = 0
    indexClient = 0
    lista1 = []
    lista2 = []
    gestiuneaMea = ServiceUtils(lista1 , lista2)
    while True:
        optiune = UI.get_optiune_ui()
        if (optiune == 0):
            return 0
        if(optiune == 1):
            for client in gestiuneaMea.lista_clienti:
                UI.print_client_ui(client)
                print()
            pass
            #afisare clienti
        elif (optiune == 2):
            for film in gestiuneaMea.lista_filme:
                UI.print_film_ui(film)
                print()
            pass
            #afisare filme
        if (optiune == 3):
            indexClient += 1
            client = UI.get_client_ui()
            nume = client[0]
            cnp = client[1]

            lista1 = gestiuneaMea.service_adauga_client(indexClient, nume, cnp)
            #lista = ServiceUtils().service_lista_clienti()
            
            print(gestiuneaMea.lista_clienti)
            pass
        elif (optiune == 4):
            indexFilm += 1
            film = UI.get_film_ui()
            titlu = film[0]
            descriere = film[1]
            gen = film[2]
            
            lista2 = gestiuneaMea.service_adauga_film(indexFilm , titlu , descriere , gen)
            print(gestiuneaMea.lista_filme)
            pass
        elif (optiune == 5):
            id = UI.get_client_id_ui()
            #ServiceUtils().lista_clienti = ServiceUtils.service_sterge_client(id)
            lista1 = gestiuneaMea.service_sterge_client(id)
            print(lista1)
        
        elif (optiune == 6):
            id = UI.get_film_id_ui()
           # ServiceUtils().lista_filme = ServiceUtils.service_sterge_film()
            lista2 = gestiuneaMea.service_sterge_film(id)
            print(lista2)

        elif (optiune == 7):
            id = UI.get_client_id_ui()
            client = UI.get_client_ui()
            #clientObj = Client(id , client[0] , client[1])
            lista1 = gestiuneaMea.service_modifica_client(id , nume_nou=client[0] , cnp_nou=client[1])
            #ServiceUtils.modifica_client(clientObj)
            print(lista1)

        elif (optiune == 8):
            id = UI.get_film_id_ui()
            film = UI.get_film_ui()
            #filmObj = Film(id , film[0] , film[1] , film[2])
            lista2 = gestiuneaMea.service_modifica_film(id , titlu_nou=film[0] , descriere_noua=film[1] , gen_nou=film[2])

            #ServiceUtils.modifica_film(filmObj)
            print(lista2)

if __name__ == "__main__":
    main()