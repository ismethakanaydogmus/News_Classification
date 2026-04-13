import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_bbc_v2():
    # Yeni eklenenlerle birlikte güncel kategori listesi
    categories = {
        "Ekonomi": "https://www.bbc.com/turkce/topics/cg726y2k82dt",
        "Saglik": "https://www.bbc.com/turkce/topics/cnq68n6wgzdt",
        "Bilim": "https://www.bbc.com/turkce/topics/c404v74nk56t",
        "Teknoloji": "https://www.bbc.com/turkce/topics/c2dwqnwkvnqt",
        "Egitim": "https://www.bbc.com/turkce/topics/cwr9jq9zx8kt",
        "Spor": "https://www.bbc.com/turkce/topics/c340qx04vwwt",
        "Siyaset": "https://www.bbc.com/turkce/topics/c8y94d98rqzt",
        "Dunya": "https://www.bbc.com/turkce/topics/cmn3xd0epypt",
        "Kultur-Sanat": "https://www.bbc.com/turkce/topics/c340qx03vwpt"
    }

    all_data = []
    page_limit = 30 # Sayfa sayısını 30'a çıkardık

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    for category, url in categories.items():
        print(f"\n--- {category} Kategorisi Başlatıldı ---")
        
        for page in range(1, page_limit + 1):
            target_url = f"{url}?page={page}"
            try:
                response = requests.get(target_url, headers=headers)
                if response.status_code != 200:
                    print(f"Sayfa {page} alınamadı. (Status: {response.status_code})")
                    break
                
                soup = BeautifulSoup(response.content, "html.parser")
                
                # BBC'nin başlıkları genellikle promo-heading veya h2/h3 içindedir
                headlines = soup.find_all(['h2', 'h3'])
                
                count = 0
                for h in headlines:
                    text = h.get_text().strip()
                    if len(text) > 25: # Çok kısa başlıkları (Navigasyon vb.) eleyelim
                        all_data.append({
                            "headline": text,
                            "category": category,
                            "source": "BBC Turkce"
                        })
                        count += 1
                
                print(f"Sayfa {page}: {count} başlık toplandı.")
                time.sleep(1.5) # BBC'yi yormayalım, bloklanmayalım
                
            except Exception as e:
                print(f"Hata: {e}")
                break

    # Verileri Kaydetme
    df = pd.DataFrame(all_data)
    df = df.drop_duplicates(subset=['headline']) # Mükerrerleri temizle
    df.to_csv("bbc_news_v2_raw.csv", index=False, encoding="utf-8-sig")
    
    print("\n" + "="*30)
    print(f"İŞLEM TAMAMLANDI!")
    print(f"Toplam Benzersiz Veri: {len(df)}")
    print(df['category'].value_counts())
    print("="*30)

if __name__ == "__main__":
    scrape_bbc_v2()