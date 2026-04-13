# 📰 Turkish News Classification Project (V2.0)

Bu proje, Türkiye'nin popüler haber kaynaklarından (BBC Türkçe, Sabah Roza) çekilen haber başlıklarını 10 farklı kategoride sınıflandıran uçtan uca bir Doğal Dil İşleme (NLP) çalışmasıdır.

This is an end-to-end NLP project that classifies news headlines from popular Turkish sources (BBC Turkish, Sabah Roza) into 10 distinct categories.

---

## 🚀 Proje Gelişimi / Project Evolution (V1.0 vs V2.0)

Projenin V2.0 sürümü, ilk versiyonda karşılaşılan sınıf dengesizliği ve düşük doğruluk sorunlarını çözmek amacıyla geliştirilmiştir.

| Özellik / Feature | V1.0 (Baseline) | V2.0 (Advanced) |
| :--- | :--- | :--- |
| **Veri Hacmi / Data Volume** | ~1,200 Rows | **~5,700 Unique Rows** |
| **Kategoriler / Categories** | 6 | **10** (Added: Politics, World, etc.) |
| **Ön İşleme / Preprocessing** | Basic Tokenization | **Zeyrek Lemmatization (Morphological Analysis)** |
| **Doğruluk / Accuracy** | 0.61 | **0.74** |

---

## 🛠️ Teknik Altyapı / Technical Stack

* **Veri Kazıma (Scraping):** Python, Selenium, BeautifulSoup (BBC Türkçe & Sabah Roza).
* **Doğal Dil İşleme (NLP):** Zeyrek (Morphological Analyzer for Turkish), NLTK.
* **Makine Öğrenmesi (ML):** Scikit-learn, LinearSVC (Balanced class weights), TF-IDF (1,3 N-Gram).
* **Görselleştirme:** Seaborn, Matplotlib.

---

## 📊 V2.0 Performans Özeti / Performance Summary

V2.0 ile birlikte özellikle "Astroloji" ve "Spor" kategorilerinde **%90+** F1-skoruna ulaşılmıştır. Zeyrek kütüphanesi ile kelime köklerine (Lemmatization) inilmesi, modelin anlamsal başarısını ciddi oranda artırmıştır.

With V2.0, the F1-score for "Astrology" and "Sports" reached **90%+**. Reducing words to their roots using the Zeyrek library significantly improved the model's semantic accuracy.

---

## 🔮 Gelecek Planı / Future Roadmap (V3.0)

* [ ] **Deep Learning:** HuggingFace üzerinden `BERTurk` modeli ile ince ayar (Fine-tuning).
* [ ] **Deployment:** Modelin bir API (FastAPI) üzerinden servis edilmesi.
* [ ] **Real-time Scraping:** Canlı haber akışının otomatik sınıflandırılması.

---

**Hazırlayan / Developed by:** [İsmet Hakan Aydoğmuş](https://github.com/ismethakanaydogmus)