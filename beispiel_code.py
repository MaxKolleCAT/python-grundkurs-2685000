def änder_mutable_variable(liste:list):
    print(f"Ursprüngliche Liste in der Funktion: {liste}")
    print(f"      Speicheradresse: {id(liste)}")
    liste.append(100)
    print(f"Geänderte Liste in der Funktion: {liste}")
    print(f"      Speicheradresse: {id(liste)}")

def adressen_ausgeben(liste:list):
    """Funktion gibt die Speicheradresse von allen Elementen in einer Liste aus"""
    print(f"Adresse der Liste: {id(liste)}")
    for i in range(0,len(liste)):
        print(f" Adresse {i}.Element: {id(liste[i])}, Wert: {liste[i]}")
    print("")

# Testen von Änderungen an mutable variables
meine_liste = [1, 2, 3]
adressen_ausgeben(meine_liste)

print(f"Vor Funktionsaufruf: {meine_liste}")
print(f"      Speicheradresse: {id(meine_liste)}")

änder_mutable_variable(meine_liste)

print(f"Nach Funktionsaufruf: {meine_liste}")
print(f"      Speicheradresse: {id(meine_liste)}")

adressen_ausgeben(meine_liste)