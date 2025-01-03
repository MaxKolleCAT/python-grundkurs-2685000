

class Buch:
    """Eine einfache Klasse zur Darstellung eines Buchs im Bücherregal."""

    def __init__(self, title:str, autor:str):
        """Inistialisert das Buch mit einem Titel und einem Autor"""
        self.titel=title 
        self.autor=autor
        self._status = "verfügbar" # nicht öffentliches Attribut

    def ausleihen(self):
        """ Markiert das Buch als ausgeliehen wenn es verfügbar ist."""
        if self._status == "verfügbar":
            self._status = "ausgeliehen"
            print(f"Das Buch '{self.titel}' wurde ausgeliehen.")
        else:
            print(f"Das Buch '{self.titel}' ist bereits ausgeliehen.")

    def zurückgeben(self):
        """ Markiert das Buch als verfügbar."""
        if self._status == "ausgeliehen":
            self._status = "verfügbar"
            print(f"Das Buch '{self.titel}' wurde zurückgegeben.")
        else:
            print(f"Das Buch '{self.titel}' ist bereits verfügbar")   

    def get_status(self):
        """Gibt den Status des Buchs zurück"""
        return self._status
    
class Bücherregal:
    """Eine Klasse zur Verwaltung eines Bücherregals"""

    def __init__(self):
        """Initalisert das Bücherregals."""
        self._bücher = [] # Privates Attribut, das eine Liste von Büchern speichert

    def buch_hinzufügen(self, buch:Buch):
        """Fügt ein Buch zum Bücherregal hinzu."""
        self._bücher.append(buch)
        print(f"Das Buch '{buch.titel}' wurde dem Regal hinzugefügt.")

    def buch_entfernen(self, buch:Buch):
        """Entfernt ein Buch aus dem Bücherregal"""
        if buch in self._bücher:
            self._bücher.remove(buch)
            print(f"Das Buch '{buch.titel}' wurde aus dem Regal entfernt.")
        else:
            print(f"Das Buch '{buch.titel}' ist nicht im Regal.")

    def alle_bücher_anzeigen(self):
        """Zeigt alle Bücher an."""
        if self._bücher:
            print("Bücher im Regal:")
            for buch in self._bücher:
                status = buch.get_status()
                print(f" - {buch.titel} von {buch.autor} (Status: {status})")
        else:
            print("Das Bücherregal ist leer.")

# Erstellung von Büchern
buch1 = Buch("Der Hobbit", "J.R.R. Tolkien")
print("Titel lautet", buch1.titel)

buch2 = Buch("1984", "George Orwell")
print("Titel lautet", buch2.autor)
print("Status lautet", buch2.get_status())

# Erstellung Bücherregal
regal = Bücherregal()
regal.buch_hinzufügen(buch1)
regal.buch_hinzufügen(buch2)

regal.alle_bücher_anzeigen()
buch1.ausleihen()
regal.alle_bücher_anzeigen()
