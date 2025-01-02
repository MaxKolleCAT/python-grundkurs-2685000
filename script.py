#!/usr/bin/env python3

import argparse

# Aufgabe: Erstellen Sie ein Skript, das einfache mathematische Operationen basierend auf Befehlszeilenargumenten durchführt.

# 1. Das Skript soll zwei Pflichtargumente akzeptieren, die als ganze Zahlen eingegeben werden.
#    - 'zahl1': Die erste Zahl, die verwendet wird.
#    - 'zahl2': Die zweite Zahl, die verwendet wird.

# 2. Es soll ein optionales Argument '--operation' geben, das die gewünschte mathematische Operation festlegt:
#    - Mögliche Optionen: 'add' (Addition), 'sub' (Subtraktion), 'mul' (Multiplikation), 'div' (Division).
#    - Wenn keine Operation angegeben wird, soll standardmäßig die Addition ausgeführt werden.

# 3. Implementieren Sie die Berechnungslogik für die oben genannten Operationen:
#    - Bei der Division soll eine Fehlerbehandlung implementiert werden, um eine Division durch Null zu vermeiden.

# 4. Geben Sie das Ergebnis der Berechnung aus.

print("Python Taschenrechner mit argparse")
print("(C) Max Kolletzki, 2025")

# Parsen der CLI-Argumente
parser = argparse.ArgumentParser(description="Argumente für Taschenrechner")
parser.add_argument("zahl1", help="Erste Zahl für Taschenrechner", type=int)
parser.add_argument("zahl2", help="Zweite Zahl für Taschenrechner", type=int)
parser.add_argument("--operation", help="Operation für den Taschenrechner", choices=["add", "sub", "mul", "div"], default="add")
args = parser.parse_args()

# Default argument für Operation
#if args.operation == None:
#    args.operation = "add"

# Durchführung der Berechnung
if args.operation == 'add':
    print("Ergebnis der Addition: ", (args.zahl1+args.zahl2))
elif args.operation == 'sub':
    print("Ergebnis der Subtraktion: ", (args.zahl1-args.zahl2))
elif args.operation == 'mul':
    print("Ergebnis der Multiplikation: ", (args.zahl1*args.zahl2))
elif args.operation == 'div':
    if args.zahl2!=0:
        print("Ergebnis der Division: ", (args.zahl1/args.zahl2))
    else:
        print("Fehler: Division durch 0.")

print("")