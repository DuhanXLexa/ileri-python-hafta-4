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
