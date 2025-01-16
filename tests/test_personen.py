from aufgaben_package.personen import Person

def test_personen_init():
    test = Person("Jon Doe", 31)
    assert test.name == "Jon Doe"
    assert test.alter == 31

def test_personen_str():
    test = Person("Jon Doe", 31)
    assert str(test) == "Jon Doe (31)"