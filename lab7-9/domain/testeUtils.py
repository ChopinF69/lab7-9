from utils import gestiuneClienti
from repository import *


class Teste():
    def test_adauga_client():
        g = gestiuneClienti()
        expRezultat = [Client(1, 'Alex', 504), Client(2, 'Andrei', 505)]
        client1 = [1 , 'Alex' , 504]
        client2 = [2 , 'Andrei' , 505]
        g.adauga_client(client1)
        g.adauga_client(client2)
        
        #expRezultat = [Client(1, 'Alex', 504), Client(2, 'Andrei', 505), Client(3, 'Adelin', 506)]

        # Comparam listele rezultatului cu listele așteptate
        #assert  g.get_lista_clienti ()== expRezultat
        #print(g.get_lista_clienti())
        lista = g.get_lista_clienti()
        #for element in lista:
            #print(element.get_client_id())
        
        for i in range(0 , len(lista)):
            id1 = lista[i].get_client_id()
            id2 = expRezultat[i].get_client_id()
            assert (id1 == id2)

            nume1 = lista[i].get_nume()
            nume2 = expRezultat[i].get_nume()

            assert (nume1 == nume2)

            cnp1 = lista[i].get_cnp()
            cnp2 = expRezultat[i].get_cnp()

            assert(cnp1 == cnp2)

    def test_modifica_client():
        g = gestiuneClienti()
        expRezultat = [Client(1, 'Andrei', 506), Client(2, 'Andrei', 505)]
        client1 = [1 , 'Alex' , 504]
        client2 = [2 , 'Andrei' , 505]
        g.adauga_client(client1)
        g.adauga_client(client2)

        lista = g.get_lista_clienti()

        g.modifica_client(1 , 'Andrei', 506)

        for i in range(0 , len(lista)):
            id1 = lista[i].get_client_id()
            id2 = expRezultat[i].get_client_id()
            assert (id1 == id2)

            nume1 = lista[i].get_nume()
            nume2 = expRezultat[i].get_nume()

            assert (nume1 == nume2)

            cnp1 = lista[i].get_cnp()
            cnp2 = expRezultat[i].get_cnp()

            assert(cnp1 == cnp2)

    def test_sterge_client():
        g = gestiuneClienti()
        expRezultat = [Client(1, 'Andrei', 506)]
        client1 = [1 , 'Alex' , 504]
        client2 = [2 , 'Andrei' , 505]
        g.adauga_client(client1)
        g.adauga_client(client2)

        lista = g.get_lista_filme()

        g.sterge_client(2)


        for i in range(0 , len(lista)):
            id1 = lista[i].get_client_id()
            id2 = expRezultat[i].get_client_id()
            assert (id1 == id2)

            nume1 = lista[i].get_nume()
            nume2 = expRezultat[i].get_nume()

            assert (nume1 == nume2)

            cnp1 = lista[i].get_cnp()
            cnp2 = expRezultat[i].get_cnp()

            assert(cnp1 == cnp2)

    def test_adauga_film():
        g = gestiuneClienti()
        #_film_id, _titlu, _descriere, _gen
        film1 = [1 , 'Sponge' , 'Sponge Bob' , 'Copii']
        film2 = [2 , 'Bruce Lee' , 'Bruce lee se bate' , 'Bataie']

        g.adauga_film(film1)
        g.adauga_film(film2)

        expResult = [Film(1 , 'Sponge' , 'Sponge Bob' , 'Copii') , Film(2 , 'Bruce Lee' , 'Bruce lee se bate' , 'Bataie')]
        lista = g.get_lista_filme()

        for i in range(0 , len(expResult)):
            film_id_1 = expResult[i].get_film_id()
            film_id_2 = lista[i].get_film_id()

            assert (film_id_1 == film_id_2)

            titlu_1 = expResult[i].get_titlu()
            titlu_2 = lista[i].get_titlu()

            assert (titlu_1 == titlu_2)

            descriere_1 = expResult[i].get_descriere()
            descriere_2 = lista[i].get_descriere()

            assert (descriere_1 == descriere_2)

    def test_sterge_film():
        g = gestiuneClienti()
            #_film_id, _titlu, _descriere, _gen
        film1 = [1 , 'Sponge' , 'Sponge Bob' , 'Copii']
        film2 = [2 , 'Bruce Lee' , 'Bruce lee se bate' , 'Bataie']

        g.adauga_film(film1)
        g.adauga_film(film2)

        expResult = [Film(1 , 'Sponge' , 'Sponge Bob' , 'Copii')]

        g.sterge_film(2)
        lista = g.get_lista_filme()

        for i in range(0 , len(expResult)):
            film_id_1 = expResult[i].get_film_id()
            film_id_2 = lista[i].get_film_id()

            assert (film_id_1 == film_id_2)

            titlu_1 = expResult[i].get_titlu()
            titlu_2 = lista[i].get_titlu()

            assert (titlu_1 == titlu_2)

            descriere_1 = expResult[i].get_descriere()
            descriere_2 = lista[i].get_descriere()

            assert (descriere_1 == descriere_2)

    def test_modifica_film():
        g = gestiuneClienti()
            #_film_id, _titlu, _descriere, _gen
        film1 = [1 , 'Sponge' , 'Sponge Bob' , 'Copii']
        film2 = [2 , 'Bruce Lee' , 'Bruce lee se bate' , 'Bataie']

        g.adauga_film(film1)
        g.adauga_film(film2)

        expResult = [Film(1 , 'Sponge' , 'Sponge Bob' , 'Adulti') , Film(2 , 'Bruce Lee' , 'Bruce lee se bate' , 'Bataie')]
        lista = g.get_lista_filme()
        for i in range(0 , len(expResult)):
            film_id_1 = expResult[i].get_film_id()
            film_id_2 = lista[i].get_film_id()

            assert (film_id_1 == film_id_2)

            titlu_1 = expResult[i].get_titlu()
            titlu_2 = lista[i].get_titlu()

            assert (titlu_1 == titlu_2)

            descriere_1 = expResult[i].get_descriere()
            descriere_2 = lista[i].get_descriere()

            assert (descriere_1 == descriere_2)
Teste.test_adauga_client()
Teste.test_modifica_client()
Teste.test_sterge_client()
Teste.test_adauga_film()
Teste.test_sterge_film()
Teste.test_modifica_film()