# İleri Python Programlama – Hafta 4 Lab Ödevi: Üreteçler ve functools

**Öğrenci Adı Soyadı:** Duhan Göksal  
**Öğrenci Numarası:** 20253004040  
**Tarih:** 18.10.2026  
**Ders:** İleri Python Programlama  
**Öğretim Üyesi:** Dr. Öğr. Üyesi Murat Emeç  
**Dönem:** 2026–2027 Güz  

---

## Görev 4 – Önbellekli Rota Sayacı Performans Ölçümleri

`rota_sayaci(baglantilar)` fonksiyonu, içinde `@lru_cache(maxsize=None)` ile süslenmiş özyinelemeli `rota_sayisi(gezegen, adim)` fonksiyonunu döndürür. Verilen gezegenden başlayarak tam `adim` uzunluğundaki farklı yolculuk rotalarının sayısını hesaplar.

`time.perf_counter()` ile `adim=20` için yapılan önbelleksiz ve önbellekli ölçüm sonuçları:

### 1. Örnek Galaksi Haritası (10 Bağlantılı Referans Galaksi)
* `dünya`: ['centauri', 'sirius']
* `centauri`: ['dünya', 'orion']
* `sirius`: ['dünya', 'orion', 'kara_delik']
* `orion`: ['centauri', 'sirius']
* `kara_delik`: ['sirius']

* **Önbelleksiz Sürüm Süresi (`adim=20`):** `2.003494 saniye`
* **Önbellekli Sürüm Süresi (`adim=20`):** `0.000094 saniye`
* **`cache_info()` Çıktısı:** `CacheInfo(hits=47, misses=51, maxsize=None, currsize=51)`
* **Hızlanma Oranı:** Yaklaşık **21.291 kat** daha hızlı

---

### 2. Projedeki `galaksi.json` Haritası
* `dünya`: ['centauri', 'sirius']
* `centauri`: ['dünya', 'sirius', 'orion']
* `sirius`: ['centauri', 'dünya', 'orion', 'kara_delik']
* `orion`: ['sirius', 'centauri']
* `kara_delik`: ['sirius']

* **Önbelleksiz Sürüm Süresi (`adim=20`):** `110.478884 saniye` (~1.84 dakika)
* **Önbellekli Sürüm Süresi (`adim=20`):** `0.000117 saniye`
* **`cache_info()` Çıktısı:** `CacheInfo(hits=128, misses=98, maxsize=None, currsize=98)`
* **Hızlanma Oranı:** Yaklaşık **944.264 kat** daha hızlı

> **Değerlendirme:** Önbelleksiz özyinelemede dallanma faktörü nedeniyle işlem karmaşıklığı $O(b^{\text{adim}})$ mertebesinde üstel olarak büyür. `@lru_cache` sayesinde daha önce hesaplanan `(gezegen, kalan_adim)` durumları hafızada tutularak tekrar hesaplanmaz ve karmaşıklık $O(V \times \text{adim})$ mertebesine (doğrusal zamana) iner.
