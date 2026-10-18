# ad soyad duhan goksal
# ogrenci numarasi 20253004040
# tarih 18 10 2026
# akis modulu birim testleri

import itertools
import pytest
from uzay_oyunu.akis import fibonacci


# ==========================================
# Görev 1 – Fibonacci üreteci testleri
# ==========================================

def test_fibonacci_next_ilk_uc():
    """next() ile ilk 3 degeri alma testi (0, 1, 1)."""
    g = fibonacci()
    assert (next(g), next(g), next(g)) == (0, 1, 1)


def test_fibonacci_islice_ilk_oniki():
    """itertools.islice ile ilk 12 degeri alma testi."""
    beklenen = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    sonuc = list(itertools.islice(fibonacci(), 12))
    assert sonuc == beklenen


def test_fibonacci_takewhile_yuzden_kucuk():
    """itertools.takewhile ile 100'den kucuk degerleri alma testi."""
    beklenen = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    sonuc = list(itertools.takewhile(lambda x: x < 100, fibonacci()))
    assert sonuc == beklenen


def test_fibonacci_tek_kullanimlik():
    """Uretecin tek kullanimlik (durumunu tuketen) oldugunu gosteren test.
    Ayni uretecten ikinci list(islice(...)) cagrisi farkli sonuc vermelidir.
    """
    g = fibonacci()
    ilk_bes = list(itertools.islice(g, 5))
    ikinci_bes = list(itertools.islice(g, 5))

    assert ilk_bes == [0, 1, 1, 2, 3]
    assert ikinci_bes == [5, 8, 13, 21, 34]
    assert ilk_bes != ikinci_bes
