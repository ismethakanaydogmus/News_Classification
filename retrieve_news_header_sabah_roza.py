from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def scrape_sabah_roza_astroloji():
    url = "https://www.sabah.com.tr/roza/astroloji"
    
    chrome_options = Options()
    # chrome_options.add_argument("--headless") # Arka planda çalışsın istersen aktif et
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    target_count = 560
    all_headlines = []
    
    try:
        print(f"\n--- Sabah Roza Astroloji Başlatıldı ---")
        driver.get(url)
        time.sleep(3) # İlk yükleme için bekle
        
        # Infinite Scroll Döngüsü
        while True:
            # Belirttiğin yapıdaki elementleri sayıyoruz
            # figcaption içindeki h3'ün içindeki a etiketi
            current_elements = driver.find_elements(By.CSS_SELECTOR, "figcaption.lg-font-size h3 a")
            current_count = len(current_elements)
            
            print(f"Şu an toplanan haber sayısı: {current_count} / {target_count}", end="\r")
            
            if current_count >= target_count:
                print(f"\n✅ Hedefe ulaşıldı: {current_count} haber bulundu.")
                break
            
            # Sayfayı en aşağı kaydır
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) # Yeni haberlerin yüklenmesi için bekle
            
            # Eğer sayfa artık daha fazla haber yüklemiyorsa (sona gelindiyse) döngüden çık
            # (Güvenlik önlemi olarak eklendi)
            # if last_height == new_height: break
            
        # Verileri çekme aşaması
        # Sadece o an DOM'da olan en güncel listeyi alıyoruz
        final_elements = driver.find_elements(By.CSS_SELECTOR, "figcaption.lg-font-size h3 a")
        
        for elem in final_elements:
            text = elem.text.strip()
            # Senin istediğin "Eylül’ün en şanslı burçları..." gibi başlık metni
            if len(text) > 20:
                all_headlines.append({
                    "headline": text,
                    "category": "Astroloji",
                    "source": "Sabah Roza"
                })
        
    except Exception as e:
        print(f"\nBir hata oluştu: {e}")
        
    finally:
        driver.quit()

    # Kayıt İşlemi
    df = pd.DataFrame(all_headlines)
    if not df.empty:
        df = df.drop_duplicates(subset=['headline'])
        # V1.0 verileriyle karışmaması için v2 olarak kaydediyoruz
        df.to_csv("sabah_roza_astroloji_v2_raw.csv", index=False, encoding="utf-8-sig")
        print(f"\nİşlem Tamamlandı! {len(df)} adet benzersiz başlık kaydedildi.")
    else:
        print("\nVeri çekilemedi. CSS Selector'ı kontrol edin.")

if __name__ == "__main__":
    scrape_sabah_roza_astroloji()