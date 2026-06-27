import os
import yt_dlp


def mp3_indir(linkler):
    # İndirme ve MP3 dönüştürme ayarları
    ydl_opts = {
        "format": "bestaudio/best",  # En iyi ses kalitesini seç
        "outtmpl": "%(title)s.%(ext)s",  # Dosya adı videonun başlığı olacak
        "postprocessors": [
            {  # Ses dönüştürme ayarları
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",  # Hedef format MP3
                "preferredquality": "192",  # Kalite (192 kbps genelde idealdir)
            }
        ],
        "quiet": False,  # İlerleme durumunu terminalde göster
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for sira, link in enumerate(linkler, 1):
            print(
                f"\n[{sira}/{len(linkler)}] İndirme başlıyor: {link}\n" + "-" * 40
            )
            try:
                ydl.download([link])
                print(f"--> Başarıyla MP3'e dönüştürüldü!")
            except Exception as e:
                print(f"❌ {link} indirilirken hata oluştu: {e}")


if __name__ == "__main__":
    print("🎵 YouTube to MP3 Toplu İndirici 🎵")
    print(
        "Birden fazla link girecekseniz aralarında BİR BOŞLUK bırakarak yapıştırın.\n"
    )

    # Kullanıcıdan linkleri al
    girdi = input("YouTube Link(leri)ini girin:\n> ")

    # Boşluklara göre linkleri ayırıp listeye çevir
    youtube_linkleri = [link.strip() for link in girdi.split(" ") if link.strip()]

    if youtube_linkleri:
        print(f"\nToplam {len(youtube_linkleri)} adet video işleme alınıyor...")
        mp3_indir(youtube_linkleri)
        print("\n✨ Tüm işlemler tamamlandı!")
    else:
        print("Geçerli bir link girmediniz.")