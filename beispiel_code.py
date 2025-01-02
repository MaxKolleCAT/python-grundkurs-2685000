#!/usr/bin/env python3

# Einführung in Funktionen mit Typehints
def addiere(zahl1 : int, zahl2 : int) -> int:
    return zahl1+zahl2

# Funktion zu Begrüsung des Nutzers
def begruesung(name : str) -> str:
    return f"Hallo, {name}!"

def berechnung_flaeche(laenge: float, breite:float) -> float:
    """
    Berechnet die Fläche eines Rechtecks.
    Parameters:
      laenge (float): Die Länge des Rechtecks
      breite (float): Die Breite des Rechtecks
    Returns:
      float: Die Fläche des Rechtecks.
    """
        
    return laenge*breite

# Aufruf der Funktionen
summe = addiere(4,1023)
print("Die summe ist:", summe)

print(begruesung("Max"))

flaeche = berechnung_flaeche(15.4, 234.2)
print("Die Fläche des Rechtecks ist:", flaeche)

# Aufgabe:
# Schreiben Sie eine Funktion, die die Differenz zweier Zahlen berechnet und zurückgibt.
# Verwenden Sie Typehints, um sicherzustellen, dass beide Argumente und der Rückgabewert Integer sind.
# Was passiert, wenn Sie die Funktion mit Float-Werten aufrufen?
# Rufen Sie diese Funktion auf und geben Sie das Ergebnis aus.
def subtract(zahl1 : int, zahl2 : int) -> int:
    """
      Funktion berechent die Differenz zwischen zahl1 und zahl2.
      
      Parameters:
        zahl1 (int): Erste Zahl
        zahl2 (int): Zwiete Zahl
      Returns:
        (int): zahl1-zahl2
    """
    return zahl1-zahl2

dif = subtract(134, 21)
print("Die Differenz ist", dif)

dif = subtract(134.2, 21.1)
print("Die Differenz mit floats ist", dif)