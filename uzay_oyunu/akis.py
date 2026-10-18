# ad soyad duhan goksal
# ogrenci numarasi 20253004040
# tarih 18 10 2026
# akis modulu - uretecler, veri boru hatti ve onbellek

from collections.abc import Generator
import itertools


def fibonacci() -> Generator[int, None, None]:
    """Sonsuz Fibonacci sayi dizisi ureten bir uretec (generator).

    0 ve 1 ile baslar, her cagrilista bir sonraki Fibonacci sayisini uretir.

    Yields:
        int: Siradaki Fibonacci sayisi.
    """
    a: int = 0
    b: int = 1
    while True:
        yield a
        a, b = b, a + b


def yakit_gostergesi(yakit: int, tuketim: int) -> Generator[int, None, None]:
    """Her next() cagrisinda yakiti tuketim kadar azaltip kalan yakiti uretir.

    Kalan yakit 0'in altina inemez (en az 0 olur). Yakit 0'a ulasinca durur
    ve bir sonraki cagrilista StopIteration firlatir.

    Args:
        yakit: Baslangic yakit miktari.
        tuketim: Her adimdaki yakit tuketimi.

    Yields:
        int: Kalan yakit miktari.
    """
    kalan: int = yakit
    while kalan > 0:
        kalan = max(0, kalan - tuketim)
        yield kalan


def satirlari_oku(yol: str) -> Generator[str, None, None]:
    """Dosyayi satir satir okuyan ve gereksiz satirlari suzen uretec.

    Dosyanin tamamini tek seferde bellege almaz (tembel degerlendirme).
    Bos satirlari ve '#' ile baslayan yorum satirlarini atlar.

    Args:
        yol: Okunacak dosyanin dosya yolu.

    Yields:
        str: Bosluklari temizlenmis gecerli satir metni.
    """
    with open(yol, mode="r", encoding="utf-8") as dosya:
        for satir in dosya:
            temiz = satir.strip()
            if not temiz or temiz.startswith("#"):
                continue
            yield temiz


def ayristir(satirlar: Generator[str, None, None]) -> Generator[tuple[str, str, int], None, None]:
    """Seyir defteri satirlarini kaynak, hedef ve yakit demetlerine donusturen uretec.

    Her satir 'kaynak -> hedef yakit' formatindadir.

    Args:
        satirlar: Satir ureteci veya yinelenebilir satir dizisi.

    Yields:
        tuple[str, str, int]: (kaynak, hedef, yakit) demeti.
    """
    for satir in satirlar:
        sol, sag = satir.split("->")
        kaynak = sol.strip()
        hedef, yakit_str = sag.strip().rsplit(maxsplit=1)
        yield kaynak, hedef, int(yakit_str)


def uzun_yolculuklar(
    kayitlar: Generator[tuple[str, str, int], None, None],
    esik: int,
) -> Generator[tuple[str, str, int], None, None]:
    """Yakiti verilen esikten buyuk olan kayitlari suzen uretec.

    Verileri bellekte listeye donusturmeden akis halinde suzer.

    Args:
        kayitlar: (kaynak, hedef, yakit) demeti ureteci.
        esik: Minimum yakit esik degeri (esikten buyuk olanlar gecer).

    Yields:
        tuple[str, str, int]: Esigi asan (kaynak, hedef, yakit) kaydi.
    """
    for kayit in kayitlar:
        if kayit[2] > esik:
            yield kayit


def rota_sayaci(baglantilar: dict[str, list[str]]):
    """Verilen baglantilar uzerinde rota sayimi yapan onbellekli fonksiyon dondurur.

    Icinde @lru_cache ile suslenmis rota_sayisi(gezegen, adim) fonksiyonunu
    tanimlayip dondurur.

    Args:
        baglantilar: Gezegenlerin komsuluk baglantilarini tutan sozluk.

    Returns:
        Callable[[str, int], int]: rota_sayisi fonksiyonu.
    """
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen: str, adim: int) -> int:
        """Verilen gezegenden baslayip tam 'adim' kadar yolculuk yapan farkli rotalarin sayisi.

        Args:
            gezegen: Baslangic gezegeni.
            adim: Atilacak adim sayisi.

        Returns:
            int: Farkli rotalarin toplam sayisi.
        """
        if adim == 0:
            return 1
        komsular = baglantilar.get(gezegen, [])
        return sum(rota_sayisi(komsu, adim - 1) for komsu in komsular)

    return rota_sayisi



