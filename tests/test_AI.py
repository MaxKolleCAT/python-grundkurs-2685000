# Generiert mit MS 

import pytest
from aufgaben_package.rechen_operation import erhoehe_um_zwei, multipliziere_mit_drei, subtrahiere_zehn, teile_durch_vier

# Tests für erhoehe_um_zwei
def test_erhoehe_um_zwei_int():
    assert erhoehe_um_zwei(3) == 5

def test_erhoehe_um_zwei_float():
    assert erhoehe_um_zwei(3.5) == pytest.approx(5.5)

def test_erhoehe_um_zwei_negative():
    assert erhoehe_um_zwei(-3) == -1

def test_erhoehe_um_zwei_zero():
    assert erhoehe_um_zwei(0) == 2

def test_erhoehe_um_zwei_large():
    assert erhoehe_um_zwei(1000000) == 1000002

# Tests für multipliziere_mit_drei
def test_multipliziere_mit_drei_int():
    assert multipliziere_mit_drei(3) == 9

def test_multipliziere_mit_drei_float():
    assert multipliziere_mit_drei(3.5) == pytest.approx(10.5)

def test_multipliziere_mit_drei_negative():
    assert multipliziere_mit_drei(-3) == -9

def test_multipliziere_mit_drei_zero():
    assert multipliziere_mit_drei(0) == 0

def test_multipliziere_mit_drei_large():
    assert multipliziere_mit_drei(1000000) == 3000000

# Tests für subtrahiere_zehn
def test_subtrahiere_zehn_int():
    assert subtrahiere_zehn(20) == 10

def test_subtrahiere_zehn_float():
    assert subtrahiere_zehn(20.5) == pytest.approx(10.5)

def test_subtrahiere_zehn_negative():
    assert subtrahiere_zehn(-10) == -20

def test_subtrahiere_zehn_zero():
    assert subtrahiere_zehn(0) == -10

def test_subtrahiere_zehn_large():
    assert subtrahiere_zehn(1000000) == 999990

# Tests für teile_durch_vier
def test_teile_durch_vier_int():
    assert teile_durch_vier(8) == 2

def test_teile_durch_vier_float():
    assert teile_durch_vier(8.0) == pytest.approx(2.0)

def test_teile_durch_vier_negative():
    assert teile_durch_vier(-8) == -2

def test_teile_durch_vier_zero():
    with pytest.raises(ZeroDivisionError):
        teile_durch_vier(0)

def test_teile_durch_vier_not_divisible():
    with pytest.raises(ValueError):
        teile_durch_vier(7)