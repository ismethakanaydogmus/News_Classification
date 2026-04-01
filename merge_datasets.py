import pandas as pd
import os

def merge_news_data():
    # Dosya isimleri
    files = [
        "bbc_news_raw.csv",
        "hurriyet_astroloji_raw.csv",
        "haberturk_spor_raw.csv"
    ]
    
    dataframes = []
    
    print("Veri birleştirme işlemi başlatıldı...\n")
    
    for file in files:
        if os.path.exists(file):
            # Dosyayı oku
            df = pd.read_csv(file, encoding="utf-8-sig")
            print(f"{file} yüklendi: {len(df)} satır.")
            dataframes.append(df)
        else:
            print(f"Uyarı: {file} bulunamadı, atlanıyor.")
            
    if not dataframes:
        print("Hata: Birleştirilecek dosya bulunamadı!")
        return

    # Tüm verileri alt alta birleştir
    master_df = pd.concat(dataframes, ignore_index=True)
    
    # 1. Adım: Tekrarlanan verileri tekrar kontrol et ve temizle
    initial_count = len(master_df)
    master_df = master_df.drop_duplicates(subset=['headline'])
    
    # 2. Adım: Verileri karıştır (Shuffle)
    # ML modelinin belirli bir sırayla (hep spor, sonra hep ekonomi) öğrenmesini engellemek için kritik.
    master_df = master_df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # 3. Adım: Kaydetme
    output_file = "master_news_dataset.csv"
    master_df.to_csv(output_file, index=False, encoding="utf-8-sig")
    
    print("-" * 30)
    print(f"BİRLEŞTİRME ÖZETİ:")
    print(f"Toplam ham veri: {initial_count}")
    print(f"Temizlenmiş benzersiz veri: {len(master_df)}")
    print(f"Kategori dağılımı:\n{master_df['category'].value_counts()}")
    print("-" * 30)
    print(f"'{output_file}' başarıyla oluşturuldu.")

if __name__ == "__main__":
    merge_news_data()