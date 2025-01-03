#!/usr/bin/env python3

# Aufgabe: Erstellen Sie eine Klasse 'BankAccount', die ein einfaches Bankkonto repräsentiert.

# 1. Die Klasse soll die folgenden Attribute (Member-Variablen) haben:
#    - Inhaber: Der Name des Kontoinhabers (öffentlich).
#    - Kontonummer: Eine eindeutige Kontonummer (öffentlich).
#    - __kontostand: Der aktuelle Kontostand (nicht öffentlich).

# 2. Implementieren Sie die folgenden Methoden:
#    - __init__: Initialisiert den Kontoinhaber, die Kontonummer und den anfänglichen Kontostand.
#    - einzahlen: Erhöht den Kontostand um einen bestimmten Betrag.
#    - abheben: Verringert den Kontostand um einen bestimmten Betrag, wenn genügend Guthaben vorhanden ist.
#    - get_kontostand: Gibt den aktuellen Kontostand zurück.

# 3. Implementieren Sie außerdem eine Methode __str__, die eine benutzerfreundliche Darstellung des Kontos zurückgibt.

# Optional:
# - Erstellen Sie eine Methode, die Transaktionen protokolliert und eine Liste von Ein- und Auszahlungen ausgibt.

class BankAccount:
    """Die Klasse repräsentiert ein einfaches Bankkonto"""

    def __init__(self, Inhaber:str, Kontonummer:str, Kontostand:int):
        """Insanziert das Bankkonto mit Inhaber, Kontonummer und dem anfänglichen Kontostand"""
        self.Inhaber = Inhaber
        self.Kontonummer = Kontonummer
        self._Kontostand = Kontostand
        self._Transaktionen = []

    def einzahlen(self, betrag:int):
        """Erhöht den Kontostand um den eingezahlten Betrag"""
        self._Kontostand = self._Kontostand + betrag
        self._Transaktionen.append( ("Einzahlung", betrag) )
        print(f"Der Kontostand wurde um {betrag:.2f} EUR erhöht")

    def auszahlen(self, betrag:int):
        """Verringert den Kontostand um den ausgezahlten Betrag"""
        neuer_Kontostand = self._Kontostand - betrag
        if neuer_Kontostand>0:
            self._Kontostand = neuer_Kontostand
            self._Transaktionen.append( ("Auszahlung", betrag) )
            print(f"Es wurden {betrag:.2f} EUR von Konto ausgezahlt.")
        else:
            print("Das Guthaben ist nicht ausreichend. Transaktion abgebrochen.")

    def get_Kontostand(self):
        """Gibt den aktuellen Kontostand zurück"""
        return self._Kontostand
    
    def __str__(self):
        """Gibt eine benutzerfreudnliche Repräsentation des Kontos zurück"""
        return f"Inhaber: {self.Inhaber}, Kontonummer: {self.Kontonummer}, Kontostand: {self._Kontostand:.2f} EUR"
    
    def Transaktion_anzeigen(self):
        for trans in self._Transaktionen:
            print(trans[0], ", Betrag: ", trans[1])


# Test der Klasse:
konto1 = BankAccount("Marius Müller", "DE540515648744", 18.15)
print(konto1)

konto1.auszahlen(15)
print(f"Neuer Kontostand: {konto1.get_Kontostand():.2f} EUR")
konto1.auszahlen(18)

konto1.einzahlen(100)
print(f"Neuer Kontostand: {konto1.get_Kontostand():.2f} EUR")

print("")
konto1.Transaktion_anzeigen()

test = (11, "y", 7.4)
print(test[1])