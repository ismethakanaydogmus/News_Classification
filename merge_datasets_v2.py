import pandas as pd
import os

def merge_datasets_v2():
    # Dosya isimleri
    files = [
        "bbc_news_v2_raw.csv",
        "sabah_roza_astroloji_v2_raw.csv"
    ]
    
    dataframes = []
    
    print("V2.0 Veri Birleştirme İşlemi Başlatıldı...\n")
    
    for file in files:
        if os.path.exists(file):
            df = pd.read_csv(file, encoding="utf-8-sig")
            print(f"{file} yüklendi: {len(df)} satır.")
            dataframes.append(df)
        else:
            print(f"Uyarı: {file} bulunamadı!")

    if not dataframes:
        print("Hata: Birleştirilecek dosya yok.")
        return

    # Birleştirme
    master_df_v2 = pd.concat(dataframes, ignore_index=True)
    
    # Mükerrer kontrolü (Headline üzerinden)
    initial_count = len(master_df_v2)
    master_df_v2 = master_df_v2.drop_duplicates(subset=['headline'])
    
    # Shuffle (Verileri Karıştır)
    master_df_v2 = master_df_v2.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # Kaydet
    output_name = "master_news_dataset_v2.csv"
    master_df_v2.to_csv(output_name, index=False, encoding="utf-8-sig")
    
    print("-" * 30)
    print(f"V2.0 MASTER VERİ SETİ ÖZETİ:")
    print(f"Toplam Ham Veri: {initial_count}")
    print(f"Benzersiz Veri Sayısı: {len(master_df_v2)}")
    print("\nKategori Dağılımı:")
    print(master_df_v2['category'].value_counts())
    print("-" * 30)
    print(f"'{output_name}' dosyası oluşturuldu. GitHub'a pushlamaya hazır.")

if __name__ == "__main__":
    merge_datasets_v2()