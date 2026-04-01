import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_hurriyet_astroloji():
    base_url = "https://www.hurriyet.com.tr/astroloji/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    all_headlines = []

    print(f"\n--- Hürriyet Astroloji Kategorisi Başlatıldı ---")

    for page in range(1, 11):
        # İlk sayfa için farklı, diğerleri için p=n yapısı
        if page == 1:
            url = base_url
        else:
            url = f"{base_url}?p={page}"
            
        print(f"Sayfa {page} taranıyor: {url}")
        
        try:
            response = requests.get(url, headers=headers, timeout=15)
            if response.status_code != 200:
                print(f"Hata: {url} sayfasına ulaşılamadı. Kod: {response.status_code}")
                break
                
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Hürriyet astroloji sayfasında başlıklar genellikle h2 veya h3 içindedir.
            # 'category-card__title' veya 'news-title' gibi class'lar yaygındır.
            # En genel ve garanti yaklaşım:
            headlines = soup.find_all(['h2', 'h3'])
            
            page_count = 0
            for h in headlines:
                text = h.get_text().strip()
                
                # Çok kısa başlıkları ve standart menü elemanlarını elemek için
                if len(text) > 25 and "Burç" in text or "2026" in text or len(text) > 40:
                    all_headlines.append({
                        "headline": text,
                        "category": "Astroloji",
                        "source": "Hurriyet"
                    })
                    page_count += 1
            
            print(f"-> {page_count} başlık eklendi.")
            time.sleep(2) # Hürriyet'in hızı ve bot koruması için önemli
            
        except Exception as e:
            print(f"Hata oluştu (Sayfa {page}): {e}")
            continue

    # Verileri Kaydetme
    df = pd.DataFrame(all_headlines)
    if not df.empty:
        df = df.drop_duplicates(subset=['headline'])
        df.to_csv("hurriyet_astroloji_raw.csv", index=False, encoding="utf-8-sig")
        print(f"\nİşlem Tamamlandı! {len(df)} benzersiz astroloji başlığı kaydedildi.")
    else:
        print("\nVeri çekilemedi. Lütfen selector'ları kontrol edin.")

if __name__ == "__main__":
    scrape_hurriyet_astroloji()