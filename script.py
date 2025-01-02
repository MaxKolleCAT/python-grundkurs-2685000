#!/usr/bin/env python3

# Aufgabe: Programmieren Sie einen Taschenrechner mit ausgelagerten Funktionen.

# 1. Erstellen Sie für jede der Grundrechenarten (Addition, Subtraktion, Multiplikation, Division) eine separate Funktion.
#    - Jede Funktion sollte zwei Argumente (Zahlen) als Eingabe akzeptieren und das Ergebnis der Berechnung zurückgeben.
#    - Die Funktionen sollten klar benannt und gemäß PEP8 formatiert sein.

# 2. Implementieren Sie eine Hauptfunktion (main), die:
#    - Den Benutzer auffordert, zwei Zahlen einzugeben.
#    - Den Benutzer auffordert, die gewünschte Operation auszuwählen (Addition, Subtraktion, Multiplikation, Division).
#    - Die entsprechende Rechenfunktion aufruft und das Ergebnis ausgibt.
#    - Eine Fehlerbehandlung integriert, um ungültige Eingaben und Division durch Null zu vermeiden.

# 3. Stellen Sie sicher, dass Ihr Code PEP8-konform ist:
#    - Verwenden Sie vier Leerzeichen für Einrückungen.
#    - Fügen Sie Leerzeichen um Operatoren ein.
#    - Halten Sie Zeilenlängen unter 79 Zeichen.
#    - Schreiben Sie geeignete Kommentare und verwenden Sie docstrings für Funktionen.

# Beispielablauf:
# - Der Benutzer gibt die Zahlen 10 und 5 ein.
# - Der Benutzer wählt die Operation 'Multiplikation'.
# - Die Funktion zur Multiplikation wird aufgerufen und das Ergebnis (50) wird ausgegeben.

# Optional: 
# - Fügen Sie weitere Funktionen hinzu, wie z.B. Potenzierung oder Modulo.
# - Implementieren Sie eine Schleife, um mehrere Berechnungen hintereinander durchzuführen, bis der Benutzer das Programm beendet.

def add(number1:int, number2:int) -> int:
    """
    Function does add two numbers together and returns the result.
    """
    return number1+number2

def sub(number1:int, number2:int) -> int:
    """
    Function does subtract two numbers together and returns the result.
    """
    return number1-number2

def mul(number1:int, number2:int) -> int:
    """
    Function does multiply two numbers together and returns the result.
    """
    return number1*number2

def div(number1:int, number2:int) -> int:
    """
    Function does divide two numbers together and returns the result.
    """
    return number1/number2

def main():
    """
    Main function of the calculator
    """
    # Specifing the operator
    op = input("Welche Operation (+, -, *, /) möchtest du durchführen? ")
  
    # Eingabe der Zahlen
    zahl1 = int(input("Bitte gib die 1. Zahl ein: "))
    zahl2 = int(input("Bitte gib die 2. Zahl ein: "))

    # Durchführung der Berechnung
    if op == '+':
        result = add(zahl1, zahl2)
        print("Ergebnis der Addition: ", result)
    elif op == '-':
        result = sub(zahl1, zahl2)
        print("Ergebnis der Subtraktion: ", result)
    elif op == '*':
        result = mul(zahl1, zahl2)
        print("Ergebnis der Multiplikation: ", result)
    elif op == '/':
        if zahl2 != 0:
            result = div(zahl1, zahl2)
            print("Ergebnis der Division: ", result)
        else:
            print("Division durch 0 nicht erlaubt!")
    else:
        print("Operation unbekannt, bitte versuche es noch einmal.")


# Run the main function
while 1:
    main()

