# Aufgabe:
# Erstellen Sie eine Klasse 'Ebike', die die Eigenschaften 'marke', 'modell' und 'reichweite' hat.
# - Implementieren Sie eine Methode 'tanken', die die Reichweite um einen gegebenen Wert erhöht.
# - Stellen Sie sicher, dass der Tankinhalt privat ist und nur über eine Methode abgefragt werden kann.
# - Instanzieren Sie ein Elektrofahrrad und testen Sie die Methoden.

class Ebike:
    """Eine Klasse zur Repersentation eines Ebikes"""

    def __init__(self, marke:str, modell:str):
        """Initialisiert eine Ebike mit Marke und Modell"""
        self.marke = marke
        self.modell = modell
        self._reichweite = 0

    def tanken(self, ladung:int):
        """Erhöht die Reichweite des Ebikes um den angegeben Wert"""
        self._reichweite = self._reichweite + ladung

    def get_reichweite(self):
        return self._reichweite

# Instanzieren eienes Ebikes
bike1 = Ebike("Cube", "Explorer C63")

bike1.tanken(30)
print(f"Das Ebike '{bike1.modell}' hat nur eine Reichweite von {bike1.get_reichweite()}")
bike1.tanken(30)
print(f"Das Ebike '{bike1.modell}' hat nur eine Reichweite von {bike1.get_reichweite()}")

