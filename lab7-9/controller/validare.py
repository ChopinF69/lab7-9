from domain import *

class validareGestiuni():
    @staticmethod
    #_client_id, _nume, _cnp
    def validare_client(client):
        '''
        Verifică dacă datele unui client sunt valide.
        @param client: Un obiect de tipul Client
        @returns: True dacă datele sunt valide, False altfel
        '''
        # Implementează verificări specifice pentru client (de exemplu, lungimea numelui, formatul CNP-ului, etc.)
        # Returnează True dacă datele sunt valide, False altfel
        '''
        @param client_id : INT
        @param nume : STRING
        @param cnp : INT
        @returns : a new object CLIENT initialized
        '''
        client_id = client.get_client_id()
        nume = client.get_nume()
        cnp = client.get_cnp()

        ok = (client_id < 10) and (len(nume) < 20) and (cnp < 1000)
        tip_1 = isinstance(client_id , int)
        tip_2 = isinstance(nume , str)
        tip_3 = isinstance(cnp , int)
        return ok and tip_1 and tip_2 and tip_3
    @staticmethod
    def validare_film(film):
        '''
        Verifică dacă datele unui film sunt valide.
        @param film: Un obiect de tipul Film
        @returns: True dacă datele sunt valide, False altfel
        '''
        # Implementează verificări specifice pentru film (de exemplu, lungimea titlului, genul valid, etc.)
        # Returnează True dacă datele sunt valide, False altfel
        '''
        FILM OBJET
        @param film_id : INT
        @param titlu : STRING
        @param descreire : STRING
        @param gen : STRING
        @returns a new object FILM initialized 
        '''

        film_id = film.get_film_id()
        titlu = film.get_titlu()
        descriere = film.get_descriere()
        gen = film.get_gen()

        ok = (film_id < 10) and (len(titlu) < 30) and (len(descriere) < 100) and (len(gen) < 20)

        tip_1 = isinstance(film_id , int)
        tip_2 = isinstance(titlu , str)
        tip_3 = isinstance(descriere , str)
        tip_4 = isinstance(gen , str)

        return ok and tip_1 and tip_2 and tip_3 and tip_4
        pass

