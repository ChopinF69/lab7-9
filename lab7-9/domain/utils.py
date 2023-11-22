from repository import *

class gestiuneClienti():
    def __init__(self):
        pass
    def adauga_client(self , client , arr):
        '''
        @param CLIENT : _client_id, _nume, _cnp
                        INT         STRING  INT
        @returns : the new list modified 
        ! ! ! Client_id will be generated , only need to pas a tuple (_nume , _cnp)
        '''
        id = client.get_client_id()
        nume = client.get_nume()
        cnp = client.get_cnp()
        c = Client(id , nume , cnp)
        arr.append(c)
    
    def adauga_film(self , film , arr):
        '''
        @param FILM : _film_id, _titlu, _descriere, _gen
                        INT      STRING  STRING     STRING
        @returns : the new list modified
        ! ! ! film_id will be generated , only need to pas (titlu , descriere , gen)

        '''
        id = film.get_film_id()
        titlu =film.get_titlu()
        descriere = film.get_descriere()
        gen = film.get_gen()
        f = Film(id , titlu , descriere , gen)
        arr.append(f)
    
    def get_lista_filme(self):
        return self.lista_filme
    def get_lista_clienti(self):
        return self.lista_clienti
    
    def sterge_client(self , client_id):
        '''
        Sterge un client din baza de date dupa id-ul sau
        @param client_id : ID-ul clientului ce va fi sters
        @returns : True daca a fost element , else False
        '''

        for client in self.lista_clienti:
            # client e un obiect deci putem realiza metodele pe el
            #get_client_id
            Cl_id = client.get_client_id()
            if client_id == Cl_id:
                self.lista_clienti.remove(client)
                
        
    
    def sterge_film(self, film_id):
        '''
        Șterge un film din listă bazat pe film_id.
        @param film_id: ID-ul filmului de șters
        @returns: True dacă filmul a fost șters, False altfel
        '''
        for film in self.lista_filme:
            #get_film_id , pt ca film face face parte fin clasa Film
            Fl_id = film.get_film_id()
            if Fl_id == film_id:
                self.lista_filme.remove(film)
                
        

    def modifica_client(self, clientObj):
        '''
        Modifică detaliile unui client bazat pe client_id.
        @param clientObj : un obiect de tip Client cu id-ul ce vrei sa fie modificat , nume_nou , cnp_nou
        @returns: True dacă modificarea a avut succes, False altfel
        '''
        client_id = clientObj.get_client_id()
        nume_nou = clientObj.get_nume()
        cnp_nou = clientObj.get_cnp()

        for client in self.lista_clienti:
            if client.get_client_id() == client_id:
                client.set_nume(nume_nou)
                client.set_cnp(cnp_nou)
                
        
    def modifica_film(self, filmObj):
        '''
        Modifică detaliile unui film bazat pe film_id.
        @param filmObj : un obiect de tip Film ce va fi modificat 
        @returns: True dacă modificarea a avut succes, False altfel
        '''
        film_id = filmObj.get_film_id()
        titlu_nou = filmObj.get_titlu()
        descriere_noua = filmObj.get_descriere()
        gen_nou = filmObj.get_gen()

        for film in self.lista_filme:
            if film.get_film_id() == film_id:
                film.set_titlu(titlu_nou)
                film.set_descriere(descriere_noua)
                film.set_gen(gen_nou)

    
                
        
    
    