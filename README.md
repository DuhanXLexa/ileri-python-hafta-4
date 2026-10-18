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

---

## Görev 5 – Okunaklılık Karşılaştırması (`map/filter/reduce` vs Liste Üreteçleri)

Python'un tasarım felsefesi (The Zen of Python - PEP 20) *"Readability counts"* (Okunabilirlik önemlidir) ve *"Simple is better than complex"* ilkelerini temel alır.

* **`map` ve `filter`:** Genellikle `lambda` ifadelerine ihtiyaç duyarlar ve sonuçları bir üreteç olduğu için doğrudan okunabilir bir çıktı elde etmek adına tekrar `list(...)` ile sarmalanmaları gerekir. Bu da parantez karmaşasına ve görsel gürültüye yol açar.
* **`reduce`:** İşlevsel programlamadan gelen güçlü bir araç olmasına rağmen, akümülatör ve eleman ilişkisi karmaşıklaştıkça kodun tek bakışta anlaşılmasını zorlaştırır. Bu nedenle Python 3'te yerleşik fonksiyonlar arasından çıkarılıp `functools` modülüne taşınmıştır.
* **Liste Üreteçleri (List Comprehensions) ve `sum()`:** Matematikteki küme gösterimine benzer bir söz dizimine sahiptir (`[ifade for oge in koleksiyon if kosul]`). Ne yapıldığı (dönüşüm, filtreleme) doğrudan ve açıkça okunur. Bu nedenle Python topluluğunda liste üreteçleri ve yerleşik `sum()` fonksiyonu çok daha **okunaklı, temiz ve Pythonic** kabul edilir.

---

## Bonus (+10 Puan) – Meşgul Bekleme (Busy Waiting) ve `time.sleep` Farkı

`tik_tak_programi`, `zamanlayici(aralik)` üretecini kullanarak 10 saniye boyunca her 2 saniyede "tik", her 5 saniyede "tak" yazdırır.

### Neden "Meşgul Bekleme" (Busy Waiting)?
Bu programda zamanın dolup dolmadığı, CPU'nun kesintisiz bir `while` döngüsü içinde sürekli olarak `time.perf_counter()` değerini sorgulaması (polling) ile kontrol edilir. İşlemci bu süreçte hiçbir zaman boşta kalmaz; çekirdek sürekli döngü komutlarını çalıştırarak **%100 CPU kullanımına** ve gereksiz güç/enerji tüketimine yol açar.

### `time.sleep()` ile Farkı:
1. **İşletim Sistemi Seviyesinde Durum:**
   * `time.sleep(sure)` çağrıldığında, Python süreci işletim sistemi çekirdeğine (OS kernel) bir sistem çağrısı yapar.
   * İşletim sistemi bu iş parçacığını (thread) **UYKU / BEKLEME (BLOCKED)** durumuna geçirir ve CPU zamanlayıcısı bu çekirdeği diğer çalışan programlara devreder.
   * Süre dolana kadar işlemci bu iş parçacığı için **%0 CPU harcar**. Süre dolduğunda donanım zamanlayıcı kesmesi (timer interrupt) ile iş parçacığı tekrar **HAZIR (READY)** durumuna getirilir.
2. **Kullanım Alanları:**
   * **`time.sleep()`**: Standart gecikmeler, arka plan görevleri ve enerji verimliliği için tercih edilir.
   * **Meşgul Bekleme (Busy Waiting)**: Ancak donanım seviyesinde mikrosaniyelik/nanosaniyelik ultra düşük gecikme gereken durumlarda (işletim sistemi bağlam değişim [context switch] maliyetini ortadan kaldırmak için) veya kütüphanelerin işbirlikçi döngülerinde (cooperative multitasking) kullanılır.

---

## Testleri Çalıştırma

Tüm testleri çalıştırmak için:
```bash
uv run pytest
```

