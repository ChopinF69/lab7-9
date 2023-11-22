class Film:
    def __init__(self, _film_id, _titlu, _descriere, _gen):
        '''
        @param film_id : INT
        @param titlu : STRING
        @param descreire : STRING
        @param gen : STRING
        @returns a new object FILM initialized 
        '''
        self.film_id = _film_id
        self.titlu = _titlu
        self.descriere = _descriere
        self.gen = _gen
        print("FILM")
    def get_film_id(self):
        return self.film_id
    def get_titlu(self):
        return self.titlu
    def get_descriere(self):
        return self.descriere
    def get_gen(self):
        return self.gen
    
    def set_film_id(self , value):
        self.film_id = value
    def set_titlu(self, value):
        self.titlu = value
    def set_descriere(self, value):
        self.descriere = value
    def set_gen(self, value):
        self.gen = value

class Client:
    def __init__(self, _client_id, _nume, _cnp):
        '''
        @param client_id : INT
        @param nume : STRING
        @param cnp : INT
        @returns : a new object CLIENT initialized
        '''
        
        self.client_id = _client_id
        self.nume = _nume
        self.cnp = _cnp
        print("CLIENT")
    def get_client_id(self):
        return self.client_id
    def get_nume(self):
        return self.nume
    def get_cnp(self):
        return self.cnp
    
    def set_client_id(self , value):
        self.client_id = value
    def set_nume(self, value):
        self.nume = value
    def set_cnp(self , value):
        self.cnp = value
