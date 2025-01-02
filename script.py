#!/usr/bin/env python3

# Aufgabe: Programmieren Sie einen einfachen Taschenrechner

# Ihr Taschenrechner soll folgende Funktionen unterstützen:
# - Addition (+)
# - Subtraktion (-)
# - Multiplikation (*)
# - Division (/)

# Der Benutzer sollte aufgefordert werden, zwei Zahlen einzugeben.
# Anschließend sollte der Benutzer die gewünschte Operation wählen können.

# Beispielablauf:
# 1. Benutzer gibt die erste Zahl ein.
# 2. Benutzer gibt die zweite Zahl ein.
# 3. Benutzer wählt die Operation (+, -, *, /).
# 4. Das Programm führt die Berechnung durch und gibt das Ergebnis aus.

# Optional: Erweitern Sie den Taschenrechner um weitere Funktionen wie Potenzierung oder Modulo.

print("Python Taschenrechner")
print("(C) Max Kolletzki, 2025")

while 1:
  op = input("Welche Operation (+, -, *, /) möchtest du durchführen? ")
  
  # Eingabe der ersten Zahl
  zahl1 = input("Bitte gib die 1. Zahl ein: ")
  try:
    zahl1 = float(zahl1)
  except:
    print("Problem bei der Konvertierung der 1. Zahl. Bitte versuche es erneut\n")
    continue
  
  # Eingabe der zweiten Zahl
  zahl2 = input("Bitte gib die 2. Zahl ein: ")
  try:
    zahl1 = float(zahl2)
  except:
    print("Problem bei der Konvertierung der 2. Zahl. Bitte versuche es erneut\n")
    continue

  # Durchführung der Berechnung
  if op == '+':
    print("Ergebnis der Addition: ", (zahl1+zahl2))
  elif op == '-':
    print("Ergebnis der Subtraktion: ", (zahl1-zahl2))
  elif op == '*':
    print("Ergebnis der Multiplikation: ", (zahl1*zahl2))
  elif op == '/':
    print("Ergebnis der Division: ", (zahl1/zahl2))
  else:
    print("Operation unbekannt, bitte versuche es noch einmal.")

  print("")