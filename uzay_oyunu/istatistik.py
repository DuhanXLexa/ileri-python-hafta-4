# ad soyad duhan goksal
# ogrenci numarasi 20253004040
# tarih 18 10 2026
# istatistik modulu - map, filter, reduce ve functools.partial

import functools
from functools import partial, reduce


# ============================================================================
# OKUNAKLILIK KARSILASTIRMASI (YORUM):
# Python felsefesine (Zen of Python - "Readability counts") gore, liste uretecleri
# (list comprehensions) ve yerlesik sum() fonksiyonu; map(), filter() ve reduce()
# fonksiyonlarina kiyasla cok daha okunakli, acik ve Pythonic (dile ozgu) bir yazimdir.
#
# Nedenleri:
# 1. map() ve filter() cagrilari genellikle isimsiz lambda ifadeleri gerektirir ve
#    sonucun tekrar list() ile sarmalanmasi gerekir; bu da kod kalabaligi yaratir.
# 2. Liste uretecleri matematikteki kume tanimina benzer [ifade for oge in liste if kosul],
#    bu sayede tek bakista donusum ve filtreleme rahatlikla anlasilir.
# 3. reduce() karmasik akislar olusturabildigi icin Python 3'te yerlesik olmaktan cikarilmis,
#    yerine acik sum() fonksiyonunun veya anlasilir dongulerin kullanilmasi onerilmistir.
# ============================================================================


# Soru 1: Gezegen adlarının büyük harfli listesi
def buyuk_harfli_gezegenler_map(galaksi: dict) -> list[str]:
    """map kullanarak gezegen adlarini buyuk harfli liste olarak dondurur."""
    return list(map(str.upper, galaksi["gezegenler"]))


def buyuk_harfli_gezegenler_comp(galaksi: dict) -> list[str]:
    """Liste ureteci kullanarak gezegen adlarini buyuk harfli liste olarak dondurur."""
    return [g.upper() for g in galaksi["gezegenler"]]


def buyuk_harfli_gezegenler(galaksi: dict) -> list[str]:
    """Gezegen adlarinin buyuk harfli listesini dondurur."""
    return buyuk_harfli_gezegenler_comp(galaksi)


# Soru 2: En az iki bağlantısı olan gezegenler
def cok_baglantili_gezegenler_filter(galaksi: dict, min_baglanti: int = 2) -> list[str]:
    """filter kullanarak en az min_baglanti kadar komsusu olan gezegenleri dondurur."""
    baglantilar = galaksi["baglantilar"]
    return list(filter(lambda g: len(baglantilar.get(g, [])) >= min_baglanti, galaksi["gezegenler"]))


def cok_baglantili_gezegenler_comp(galaksi: dict, min_baglanti: int = 2) -> list[str]:
    """Liste ureteci ile en az min_baglanti kadar komsusu olan gezegenleri dondurur."""
    baglantilar = galaksi["baglantilar"]
    return [g for g in galaksi["gezegenler"] if len(baglantilar.get(g, [])) >= min_baglanti]


def cok_baglantili_gezegenler(galaksi: dict, min_baglanti: int = 2) -> list[str]:
    """En az iki baglantisi olan gezegenleri dondurur."""
    return cok_baglantili_gezegenler_comp(galaksi, min_baglanti)


# Soru 3: Toplam bağlantı sayısı
def toplam_baglanti_sayisi_reduce(galaksi: dict) -> int:
    """functools.reduce kullanarak toplam baglanti sayisini hesaplar."""
    baglantilar = galaksi["baglantilar"]
    return reduce(lambda toplam, komsular: toplam + len(komsular), baglantilar.values(), 0)


def toplam_baglanti_sayisi_sum(galaksi: dict) -> int:
    """sum() ve uretec ifadesi kullanarak toplam baglanti sayisini hesaplar."""
    baglantilar = galaksi["baglantilar"]
    return sum(len(komsular) for komsular in baglantilar.values())


def toplam_baglanti_sayisi(galaksi: dict) -> int:
    """Toplam baglanti sayisini dondurur."""
    return toplam_baglanti_sayisi_sum(galaksi)


# Yolculuk ve partial ile hizli_yolculuk
def yolculuk(mesafe: float, hiz: float = 1.0) -> float:
    """Mesafe ve hiza gore seyahat suresini (sure = mesafe / hiz) hesaplar."""
    return mesafe / hiz


# functools.partial ile hiz=3 sabitlenmis hizli_yolculuk fonksiyonu
hizli_yolculuk = partial(yolculuk, hiz=3.0)
