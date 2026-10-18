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


# ==========================================
# Görev 2 – Yakıt göstergesi testleri
# ==========================================

def test_yakit_gostergesi_ornek_cikti():
    """Odev dokumanindaki list(yakit_gostergesi(100, 30)) ciktisi testi."""
    from uzay_oyunu.akis import yakit_gostergesi
    assert list(yakit_gostergesi(100, 30)) == [70, 40, 10, 0]


def test_yakit_gostergesi_stop_iteration():
    """Yakit 0'a ulasinca sonraki cagrilista StopIteration firlatildigini test eder."""
    from uzay_oyunu.akis import yakit_gostergesi
    gosterge = yakit_gostergesi(20, 10)
    assert next(gosterge) == 10
    assert next(gosterge) == 0
    with pytest.raises(StopIteration):
        next(gosterge)


def test_yakit_gostergesi_sifir_baslangic():
    """Yakit bastan 0 ise hicbir deger uretilmeden durmalidir."""
    from uzay_oyunu.akis import yakit_gostergesi
    assert list(yakit_gostergesi(0, 10)) == []


def test_yakit_gostergesi_tek_adimda_tukenme():
    """Tuketim yakittan buyukse dogrudan 0 uretmeli ve bitmelidir."""
    from uzay_oyunu.akis import yakit_gostergesi
    assert list(yakit_gostergesi(15, 25)) == [0]

