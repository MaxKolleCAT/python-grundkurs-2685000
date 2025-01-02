#!/usr/bin/env python3

# Aufgabe: Erstellen Sie ein Skript, das die Länge eines Textes analysiert und Informationen darüber liefert.

# Das Skript soll folgende Funktionalität bieten:
# 1. Ein Pflichtargument (positional argument), das einen Text entgegennimmt.
# 2. Ein optionales Argument --details, das zusätzliche Informationen liefert:
#    - Anzahl der Wörter
# 3. Wenn das Argument --details nicht angegeben wird, soll nur die Anzahl der Zeichen ausgegeben werden.

# Beispiel:
# python3 script.py "Dies ist ein Beispieltext." --details
# Ausgabe:
# Zeichen: 27
# Wörter: 5

# Optional: Erweitern Sie das Skript, um auch die Anzahl der Vokale und Konsonanten zu zählen.

import argparse

descrpiton_str = "Das Skript untersucht den eigegeben String und gibt die Anzahl der Zeichen und weitere Details aus."

# Argumente verarbeiten
parser = argparse.ArgumentParser(description=descrpiton_str)
parser.add_argument("input_str", type=str, help="String der analysiert werden soll")
parser.add_argument("--details", action='store_true', help="Ausgabe von mehr Details zum eingegeben String")
args = parser.parse_args()

num_chars = len(args.input_str)

print("Ausgabe:")
print("Anzahl der Zeichen: ", num_chars)

if args.details==True:
    # Leerzeichen zählen -> Wörter
    num_words = str.count(args.input_str, " ")+1
    print("Anzahl Wörter: ", num_words)
    
    # Anzahl der Konsuanten bestimmen
    key_str = "aeiou"
    count_int = 0
    for char in args.input_str:
        if char.lower() in key_str:
            count_int = count_int+1
    print("Anzahl Konsunaten: ", count_int)

    # Anzahl der Vokale bestimmen
    key_str = "bcdfghjklmnpqrstvwxyz"
    count_int = 0
    for char in args.input_str:
        if char.lower() in key_str:
            count_int = count_int+1
    print("Anzahl Vokale: ", count_int)