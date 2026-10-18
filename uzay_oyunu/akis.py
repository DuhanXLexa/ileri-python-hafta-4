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

