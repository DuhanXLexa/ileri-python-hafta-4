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


# ==========================================
# Görev 3 – Seyir defteri boru hattı testleri
# ==========================================

def test_boru_hatti_toplam_yakit():
    """Odev dokumanindaki toplam yakit (88) boru hatti testi."""
    from uzay_oyunu.akis import satirlari_oku, ayristir
    from pathlib import Path

    yol = Path(__file__).parent.parent / "veri" / "seyir.txt"
    toplam = sum(y for _, _, y in ayristir(satirlari_oku(str(yol))))
    assert toplam == 88


def test_boru_hatti_uzun_yolculuklar():
    """Odev dokumanindaki 10'dan buyuk uzun yolculuklar testi."""
    from uzay_oyunu.akis import satirlari_oku, ayristir, uzun_yolculuklar
    from pathlib import Path

    yol = Path(__file__).parent.parent / "veri" / "seyir.txt"
    kayitlar = ayristir(satirlari_oku(str(yol)))
    hedefler = [h for _, h, _ in uzun_yolculuklar(kayitlar, 10)]
    assert hedefler == ["sirius", "centauri", "orion", "kara_delik"]


def test_boru_hatti_tembel_degerlendirme():
    """Boru hatti asamalarinin listeye okumayip generator dondurdugunu dogrular."""
    import types
    from uzay_oyunu.akis import satirlari_oku, ayristir, uzun_yolculuklar
    from pathlib import Path

    yol = Path(__file__).parent.parent / "veri" / "seyir.txt"
    g_satir = satirlari_oku(str(yol))
    assert isinstance(g_satir, types.GeneratorType)

    g_ayristir = ayristir(g_satir)
    assert isinstance(g_ayristir, types.GeneratorType)

    g_uzun = uzun_yolculuklar(g_ayristir, 10)
    assert isinstance(g_uzun, types.GeneratorType)


# ==========================================
# Görev 4 – Önbellekli rota sayacı testleri
# ==========================================

def test_rota_sayaci_ornek_galaksi():
    """Odev dokumanindaki 10 baglantili ornek galaksi ciktilari testi:
    say("dünya", 3) -> 9, say("dünya", 10) -> 2185, say("dünya", 40) -> 16832258606399
    """
    from uzay_oyunu.akis import rota_sayaci

    baglantilar = {
        "dünya": ["centauri", "sirius"],
        "centauri": ["dünya", "orion"],
        "sirius": ["dünya", "orion", "kara_delik"],
        "orion": ["centauri", "sirius"],
        "kara_delik": ["sirius"],
    }
    say = rota_sayaci(baglantilar)
    assert say("dünya", 3) == 9
    assert say("dünya", 10) == 2185
    assert say("dünya", 40) == 16832258606399


def test_rota_sayaci_galaksi_json():
    """Projedeki galaksi.json ile onbellekli rota sayaci calisma ve cache_info testi."""
    import json
    from pathlib import Path
    from uzay_oyunu.akis import rota_sayaci

    yol = Path(__file__).parent.parent / "uzay_oyunu" / "galaksi.json"
    with open(yol, encoding="utf-8") as f:
        galaksi = json.load(f)

    say = rota_sayaci(galaksi["baglantilar"])
    assert say("dünya", 0) == 1
    sonuc_3 = say("dünya", 3)
    assert sonuc_3 == 16

    info = say.cache_info()
    assert info.hits > 0
    assert info.currsize > 0


# ==========================================
# Görev 5 – map, filter, reduce ve partial testleri
# ==========================================

@pytest.fixture
def ornek_galaksi_verisi():
    """Odev dokumanindaki 10 baglantili ornek galaksi verisi."""
    return {
        "gezegenler": ["dünya", "centauri", "sirius", "orion", "kara_delik"],
        "baglantilar": {
            "dünya": ["centauri", "sirius"],
            "centauri": ["dünya", "orion"],
            "sirius": ["dünya", "orion", "kara_delik"],
            "orion": ["centauri", "sirius"],
            "kara_delik": ["sirius"],
        },
    }


def test_buyuk_harfli_gezegenler_iki_yolla(ornek_galaksi_verisi):
    """Soru 1: map ve liste ureteci ile buyuk harf listesi testi."""
    from uzay_oyunu.istatistik import (
        buyuk_harfli_gezegenler_map,
        buyuk_harfli_gezegenler_comp,
    )
    beklenen = ["DÜNYA", "CENTAURI", "SIRIUS", "ORION", "KARA_DELIK"]
    sonuc_map = buyuk_harfli_gezegenler_map(ornek_galaksi_verisi)
    sonuc_comp = buyuk_harfli_gezegenler_comp(ornek_galaksi_verisi)

    assert sonuc_map == beklenen
    assert sonuc_comp == beklenen
    assert sonuc_map == sonuc_comp


def test_cok_baglantili_gezegenler_iki_yolla(ornek_galaksi_verisi):
    """Soru 2: filter ve liste ureteci ile en az iki baglantili gezegenler testi."""
    from uzay_oyunu.istatistik import (
        cok_baglantili_gezegenler_filter,
        cok_baglantili_gezegenler_comp,
    )
    beklenen = ["dünya", "centauri", "sirius", "orion"]
    sonuc_filter = cok_baglantili_gezegenler_filter(ornek_galaksi_verisi, 2)
    sonuc_comp = cok_baglantili_gezegenler_comp(ornek_galaksi_verisi, 2)

    assert sonuc_filter == beklenen
    assert sonuc_comp == beklenen
    assert sonuc_filter == sonuc_comp


def test_toplam_baglanti_sayisi_iki_yolla(ornek_galaksi_verisi):
    """Soru 3: reduce ve sum() ile toplam baglanti sayisi (10) testi."""
    from uzay_oyunu.istatistik import (
        toplam_baglanti_sayisi_reduce,
        toplam_baglanti_sayisi_sum,
    )
    sonuc_reduce = toplam_baglanti_sayisi_reduce(ornek_galaksi_verisi)
    sonuc_sum = toplam_baglanti_sayisi_sum(ornek_galaksi_verisi)

    assert sonuc_reduce == 10
    assert sonuc_sum == 10
    assert sonuc_reduce == sonuc_sum


def test_hizli_yolculuk_partial():
    """functools.partial ile turetilen hizli_yolculuk fonksiyonu testi."""
    from uzay_oyunu.istatistik import yolculuk, hizli_yolculuk

    assert hizli_yolculuk.func == yolculuk
    assert hizli_yolculuk.keywords == {"hiz": 3.0}

    # mesafe 30 ise 30 / 3 = 10.0 olmalidir
    assert hizli_yolculuk(30) == 10.0
    assert hizli_yolculuk(9) == 3.0
    assert yolculuk(30, 3.0) == hizli_yolculuk(30)


# ==========================================
# Bonus (+10) – zamanlayici testleri
# ==========================================

def test_zamanlayici_aralik_dolunca_true():
    """zamanlayici uretecinin aralik dolana kadar False, dolunca True urettigini test eder."""
    import time
    from uzay_oyunu.akis import zamanlayici

    g = zamanlayici(0.03)
    # Hemen cagrilinca henuz sure dolmadigi icin False donmeli
    assert next(g) is False

    # 0.03 saniyeden biraz fazla bekleyelim (mesgul bekleme ile)
    bas = time.perf_counter()
    while time.perf_counter() - bas < 0.035:
        pass

    # Sure doldugunda True donmelidir
    assert next(g) is True


def test_tik_tak_programi_calisma():
    """tik_tak_programi fonksiyonunun calismasini ve olay dondurmesini test eder (hizli test: 0.1s)."""
    from uzay_oyunu.akis import tik_tak_programi

    olaylar = tik_tak_programi(toplam_sure=0.01, yazdir=False)
    assert isinstance(olaylar, list)





