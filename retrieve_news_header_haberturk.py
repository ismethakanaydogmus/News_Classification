from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def scrape_haberturk_spor():
    url = "https://www.haberturk.com/spor"
    
    chrome_options = Options()
    # chrome_options.add_argument("--headless") # İstersen görünmez yapabilirsin
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    all_headlines = []
    
    try:
        print(f"\n--- Habertürk Spor Başlatıldı ---")
        driver.get(url)
        time.sleep(5) 
        
        # Scroll sayısı 5'e düşürüldü
        scroll_count = 5 
        for i in range(scroll_count):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print(f"Kaydırılıyor... ({i+1}/{scroll_count})")
            time.sleep(3) # İçeriklerin yüklenmesi için zaman tanıyalım
            
        # Hedeflediğin spesifik class yapısı (CSS Selector formatında)
        # Not: CSS selector içinde boşluklar '.' ile değiştirilir.
        target_css = "span.font-bold.text-ellipsis.line-clamp-2.text-sm.md\\:text-base.lg\\:text-xl"
        
        elements = driver.find_elements(By.CSS_SELECTOR, target_css)
        print(f"Eşleşen toplam element bulundu: {len(elements)}")
        
        for elem in elements:
            text = elem.get_attribute("textContent").strip()
            
            # Sınıflandırma için anlamlı uzunluk
            if len(text) > 20:
                all_headlines.append({
                    "headline": text,
                    "category": "Spor",
                    "source": "Haberturk"
                })
        
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        
    finally:
        driver.quit()

    # Verileri Kaydetme
    df = pd.DataFrame(all_headlines)
    if not df.empty:
        df = df.drop_duplicates(subset=['headline'])
        df.to_csv("haberturk_spor_raw.csv", index=False, encoding="utf-8-sig")
        print(f"\nİşlem Tamamlandı! {len(df)} adet benzersiz spor haberi kaydedildi.")
    else:
        print("\nVeri çekilemedi. Belirttiğin class yapısı sayfada o an bulunamamış olabilir.")

if __name__ == "__main__":
    scrape_haberturk_spor()