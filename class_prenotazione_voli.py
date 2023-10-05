
class Passeggero:
    '''Represents a passenger with first name, last name and ID.'''
    def __init__(self, nome: str, cognome: str, id: int):
        self.nome = nome
        self.cognome = cognome
        self.id = id

class Volo:
    '''Represents a flight with departure, destination, flight code and available seats.'''
    
    def __init__(self, partenza: str, destinazione: str, codice_volo: str, posti_disponibili: int = 50):
        self.partenza = partenza
        self.destinazione = destinazione
        self.codice_volo = codice_volo
        self.posti_disponibili = posti_disponibili
        self.passeggeri = []

    def aggiungi_passeggero(self,passeggero):
        if self.posti_disponibili > 0:
            self.passeggeri.append(passeggero)
            self.posti_disponibili -= 1
            return True
        else:
            print('Il volo è completo, prenotazione non riuscita.')
            return False

    
    def rimuovi_passeggero(self,passeggero):
        if passeggero in self.passeggeri:
            self.passeggeri.remove(passeggero)
            self.posti_disponibili += 1
            return True
        else:
            print('passeggero non trovato nella prenotazione.')
        
    @property
    def mostra_passeggeri(self):
        N = len(self.passeggeri)
        print(f'Lista Passeggeri: {N}/50\n')
        print(f'Passeggeri del volo {self.codice_volo} \n diretto a {self.destinazione}')
        for passeggero in self.passeggeri:    
            print(f' Nome: {passeggero.nome}  / Id: {passeggero.id}')
            
    @property
    def visualizza_posti_disponibili(self):
        print(f'restano {self.posti_disponibili} posti disponibili per il volo {self.codice_volo.upper()}')

class Gestisci_voli:
    '''Manages flight bookings.'''
    def __init__(self):
        self.prenotazioni = []

    def effettua_prenotazione(self,passeggero,volo):
        if volo.aggiungi_passeggero(passeggero):
            prenotazione = (passeggero, volo)
            self.prenotazioni.append(prenotazione)
            print(f'Prenotazione effettuata per {passeggero.nome} su {volo.codice_volo} \n')

    def cancella_prenotazione(self,passeggero,volo):
        prenotazione = (passeggero,volo)
        if prenotazione in self.prenotazioni:
            self.prenotazioni.remove(prenotazione)
            volo.rimuovi_passeggero(passeggero)
            print(f'Prenotazione cancellata per {passeggero.nome} da {volo.codice_volo} \n')
        else:
            print('Prenotazione non trovata.')

    @property
    def mostra_tabella_prenotazioni(self):
        print('Tabella Prenotazioni: ')
        for passeggero, volo in self.prenotazioni:
            print(f'Passeggero: {passeggero.nome} / Volo: {volo.codice_volo} \n')




