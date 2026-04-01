import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_bbc_turkce():
    # Kategori listesine 'Egitim' eklendi
    categories = {
        "Ekonomi": "https://www.bbc.com/turkce/topics/cg726y2k82dt",
        "Saglik": "https://www.bbc.com/turkce/topics/cnq68n6wgzdt",
        "Bilim": "https://www.bbc.com/turkce/topics/c404v74nk56t",
        "Teknoloji": "https://www.bbc.com/turkce/topics/c2dwqnwkvnqt",
        "Egitim": "https://www.bbc.com/turkce/topics/cwr9jq9zx8kt"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    all_headlines = []

    for category_name, base_url in categories.items():
        print(f"\n--- {category_name} Kategorisi Başlatıldı ---")
        
        for page in range(1, 16): # 15 sayfa çekilecek
            url = f"{base_url}?page={page}"
            print(f"Sayfa {page} taranıyor...")
            
            try:
                response = requests.get(url, headers=headers, timeout=15)
                if response.status_code != 200:
                    print(f"Uyarı: {page}. sayfada içerik bitti veya ulaşılamadı.")
                    break 
                
                soup = BeautifulSoup(response.content, "html.parser")
                
                # BBC başlıklarını yakalamak için h2 ve içindeki metni hedefliyoruz
                headlines = soup.find_all('h2')
                
                page_count = 0
                for h in headlines:
                    text = h.get_text().strip()
                    
                    # Başlık uzunluğu kontrolü ve gereksiz metin elemeleri
                    if len(text) > 25: 
                        all_headlines.append({
                            "headline": text,
                            "category": category_name,
                            "source": "BBC Turkce"
                        })
                        page_count += 1
                
                print(f"-> {page_count} başlık eklendi.")
                time.sleep(2) # Banlanmamak için bekleme süresini biraz artırdık
                
            except Exception as e:
                print(f"Hata ({category_name} P{page}): {e}")
                continue

    # Veri setini oluştur ve temizle
    df = pd.DataFrame(all_headlines)
    if not df.empty:
        # Tekrarlanan (duplicate) başlıkları temizle
        initial_count = len(df)
        df = df.drop_duplicates(subset=['headline'])
        final_count = len(df)
        
        df.to_csv("bbc_news_raw.csv", index=False, encoding="utf-8-sig")
        print(f"\n--- ÖZET ---")
        print(f"Toplam çekilen satır: {initial_count}")
        print(f"Benzersiz başlık sayısı: {final_count}")
        print(f"Dosya 'bbc_news_raw.csv' olarak kaydedildi.")
    else:
        print("\nVeri çekme başarısız oldu.")

if __name__ == "__main__":
    scrape_bbc_turkce()