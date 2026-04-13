# 📰 Turkish News Classification Project (V3.0 - Deep Learning)

Bu proje, Türkiye'nin popüler haber kaynaklarından çekilen başlıkları 10 farklı kategoride sınıflandıran, Naive Bayes'ten BERT'e uzanan evrimsel bir Doğal Dil İşleme (NLP) çalışmasıdır.

This project is an evolutionary NLP study that classifies Turkish news headlines into 10 categories, evolving from Naive Bayes to State-of-the-Art BERT models.

---

## 🚀 Proje Evrimi / Project Evolution

Proje üç ana aşamada geliştirilmiş ve her aşamada başarı oranı (Accuracy) ciddi oranda artırılmıştır.

| Versiyon | Teknoloji / Tech Stack | Başarı (Accuracy) | Temel Fark / Key Difference |
| :--- | :--- | :--- | :--- |
| **V1.0** | Naive Bayes / TF-IDF | **%61** | Baseline (Temel) Model. |
| **V2.0** | LinearSVC / Zeyrek Lemm. | **%74** | Gelişmiş Ön İşleme (Kök bulma). |
| **V3.0** | **BERTurk (Transformers)** | **%82.3** | **Bağlamsal Analiz (Deep Learning).** |

---

## 🧠 V3.0 Teknik Detaylar / Technical Insights

V3.0 aşamasında klasik makine öğrenmesi yöntemleri terk edilerek derin öğrenme mimarisine geçilmiştir.

* **Model:** `dbmdz/bert-base-turkish-cased` (BERTurk)
* **Yöntem:** Fine-tuning (İnce Ayar)
* **Veri Seti:** 5,700+ Benzersiz Haber Başlığı (BBC Türkçe & Sabah Roza)
* **Donanım:** Tesla T4 GPU (Google Colab)

### 📊 Neden BERT?
Klasik modeller kelimelere tekil olarak bakarken, BERT kelimelerin cümle içindeki sağ ve sol bağlamlarını eşzamanlı olarak analiz eder. Bu sayede "Arkeoloji" haberlerini "Bilim" kategorisiyle eşleştirebilecek kadar derin bir semantik anlayış geliştirir.

---

## 🛠️ Kurulum ve Kullanım / Setup

1. Repoyu klonlayın: `git clone https://github.com/ismethakanaydogmus/News_Classification.git`
2. Bağımlılıkları yükleyin: `pip install transformers datasets accelerate torch`
3. V3 Not defterini (Notebook) GPU modunda çalıştırın.

---

## 🔮 Gelecek Vizyonu / Roadmap
- [ ] **Model Deployment:** Hugging Face Spaces veya Streamlit ile canlı demo.
- [ ] **Quantization:** Modelin boyutunu küçülterek mobil cihazlarda (React Native) çalışabilir hale getirmek.

**Hazırlayan / Developed by:** [İsmet Hakan Aydoğmuş](https://github.com/ismethakanaydogmus)
