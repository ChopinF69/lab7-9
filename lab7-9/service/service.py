from controller.validare import validareGestiuni
from domain.utils import gestiuneClienti
from repository.repo import Client , Film
class ServiceUtils(gestiuneClienti , validareGestiuni):
    def __init__(self , lista1 , lista2) -> None:
        self.lista_clienti = lista1
        self.lista_filme = lista2
        pass

    def service_adauga_client(self , client_id : int, nume : str, cnp : int) -> list:
        '''
        Functia va prealua datele despre un client , va crea un obiect de tip Client
        si il va adauga in baza de date

        @param client_id : INT
        @param nume : STRING
        @param cnp : INT
        @returns : LIST modified
        '''
        client = Client(client_id , nume , cnp)
        ok = self.validare_client(client)
        if(ok):
            self.adauga_client(client , self.lista_clienti)
        lista = self.lista_clienti
            
        return lista
        
    
    def service_adauga_film(self , film_id : int , titlu : str , descriere : str , gen : str) -> list:
        '''
        Functia preia date despre un film , initializeaza obiectul Film si
        il va adauga in baza de date
        @param film_id : INT 
        @param titlu : STRING
        @param descreire : STRING
        @param gen : STRING
        @returns : LIST modified
        '''
        film = Film(film_id , titlu , descriere , gen)
        ok = self.validare_film(film)
        if(ok):
            self.adauga_film(film , self.lista_filme)
            lista = self.lista_filme
        return lista
    
    def service_sterge_client(self , client_id : int) -> list:
        '''
        Functia va sterge un client pe baza id-ului
        @param client_id : INT
        @returns : LIST modified
        '''
        self.sterge_client(client_id)
        return self.lista_clienti

    def service_sterge_film(self , film_id : int) -> list:
        '''
        Functia va prelua id-ul filmului ce va urma sa fie eliminat
        @param film_id : INT
        @returns : LIST modified
        '''
        self.sterge_film(film_id)
        return self.lista_filme

    def service_modifica_client(self, client_id : int, nume_nou : str, cnp_nou : int) -> list:
        '''
        Functia va prealua id-ul clientului ce urmeaza sa fie modificat si datele noului client
        se va crea un nou Client cu datele preluate si se va modifica lista
        @param client_id : INT
        @param nume_nou : STRING
        @param cnp_nou : INT
        @returns : LIST modified
        '''
        client = Client(client_id , nume_nou , cnp_nou)
        ok = self.validare_client(client)
        if(ok):
            self.modifica_client(client)
            lista = self.lista_clienti
        return lista
    
    def service_modifica_film(self , film_id : int , titlu_nou : str , descriere_noua : str, gen_nou : str) -> list:
        '''
        Functia va prelua id-ul filmului si datele noi despre film
        se crea un nou obiect de tip Client si se va modifica lista
        @param film_id : INT
        @param titlu_nou : STRING
        @param descriere_noua : STRING
        @param gen_nou : STRING
        @returns : LIST modified 
        '''
        film = Film(film_id , titlu_nou , descriere_noua , gen_nou)
        ok = self.validare_film(film)
        if(ok):
            self.modifica_film(film)
            lista = self.lista_filme
        return lista
    
    def get_client_id_based_on_nume(self , nume:str) -> int:
        '''
        Functia va returna numele clientului cu id-ul preluat
        @param nume : STRING
        @returns : INT and it represents the id of the client , and 0 if it doesn t exista
        '''
        for client in self.lista_clienti:
            id = client.get_client_id()
            numeClient = client.get_nume()
            if(nume == numeClient):
                return id
        return 0
    def get_client_id_based_on_cnp(self , cnp : int) -> int:
        '''
        Functia va prelua cnp-ul si va returna id-ul clientului repspectiv
        @param cnp : INT
        @returns : INT and it is the id of the client with the cnp taken
        '''
        for client in self.lista_clienti:
            id = client.get_client_id()
            cnpClient = client.get_cnp()
            if(cnp == cnpClient):
                return id
        return 0
    def get_film_id_based_on_titlu(self , titlu : str) -> int:
        '''
        Functia va returna id-ul pe baza titlului ales al filmului
        @param titlu :
        '''
        for film in self.lista_filme:
            id = film.get_film_id()
            titluFilm = film.get_titlu()
            if (titlu == titluFilm):
                return id
        return 0
    def get_film_id_based_on_descriere(self , descriere):
        for film in self.lista_filme:
            id = film.get_film_id()
            descriereFilm = film.get_descriere()
            if (descriere == descriereFilm):
                return id
        return 0
    def get_film_id_based_on_gen(self ,gen):
        for film in self.lista_filme:
            id = film.get_film_id()
            genFilm = film.get_gen()
            if (gen == genFilm):
                return id
        return 0