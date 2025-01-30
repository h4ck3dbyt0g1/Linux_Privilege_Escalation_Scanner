# 🚀 Linux Privilege Escalation Scanner
**Linux Privilege Escalation Scanner**, Linux sistemlerindeki yetki yükseltme güvenlik açıklarını tespit etmek için tasarlanmış güçlü bir araçtır. SUID dosyalar, dosya yetenekleri (capabilities) ve yanlış yapılandırmalar gibi güvenlik risklerini otomatik olarak tarar ve raporlar.  

## 🌟 Özellikler
***🔍 SUID Binaries:*** SUID bit ayarlı dosyaları tespit eder.  

***🔒 Capabilities:*** Dosyaların sahip olduğu yetenekleri analiz eder.  

***⚙️ Misconfigurations:*** SSH yapılandırma hataları, sudoers izin sorunları gibi yanlış yapılandırmaları tespit eder.

## 🛠️ Kullanım
Bu araç, komut satırından kolayca çalıştırılabilir ve esnek parametrelerle konfigüre edilebilir.

## 🎯 Parametreler  


--suid	SUID bit ayarlı dosyaları tarar.  

--capabilities	Dosyaların yeteneklerini kontrol eder.  

--misconfig	Yanlış yapılandırmaları tespit eder.  

## 📤 Çıktı Formatı
Araç, sonuçlarını JSON formatında döndürür:


    {
    "sonuç": {  

        "durum": "başarılı/başarısız",  

        "veri": {},  

        "hata_mesajı": "varsa hata açıklaması"
    }  

## ⚙️ Kurulum
### 1️⃣ Gereksinimler
- Python 3.x  

- Aşağıdaki kütüphaneler:  

        rich  

        psutil  
  


### 2️⃣ Bağımlılıkları Yükleme
Gerekli bağımlılıkları yüklemek için:

    
    pip install -r requirements.txt
    Eğer "externally-managed-environment" hatası alırsanız, sanal ortam kullanabilirsiniz:
    
    python3 -m venv myenv
    source myenv/bin/activate
    pip install -r requirements.txt  
    
Sanal ortamdan çıkmak için:

    deactivate  

### 3️⃣ Sistem Genelinde Kurulum (Opsiyonel)
Sistem genelinde bağımlılıkları yüklemek için:

    sudo apt install python3-rich python3-psutil  

### ▶️ Çalıştırma
Aşağıdaki komutlarla aracı çalıştırabilirsiniz:

***SUID Taraması:***


    python3 main.py --suid  

***Capabilities Kontrolü:***

    python3 main.py --capabilities  

***Yanlış Yapılandırma Analizi:***

    python3 main.py --misconfig  

Parametresiz çalıştırıldığında yardım mesajı görüntülenir.  

## 📊 Çıktı Örnekleri
### --suid Parametresi ile Çıktı:

    {
        "sonuç": {
            "durum": "başarılı",
            "veri": {
                "suid": {
                    "suid_files": [
                        "/usr/lib/chromium/chrome-sandbox",
                        "/usr/bin/sudo"
                    ]
                }
            },
            "hata_mesajı": ""
    }

### --misconfig Parametresi ile Çıktı:  

    {
        "sonuç": {
            "durum": "başarılı",
            "veri": {
                "misconfig": {
                    "misconfigurations": []
                }
            },
            "hata_mesajı": ""
        }
    }

### Proje Videosu

[Demo Videosunu İzle](https://github.com/h4ck3dbyt0g1/Linux_Privilege_Escalation_Scanner/releases/tag/release-01)


    
### 🤝 Katkıda Bulunma
Bu projeye katkıda bulunmak ister misiniz? İşte adımlar:

Bu depoyu fork edin.  

Yeni bir dal (branch) oluşturun.  

Değişikliklerinizi commit edin.  

Pull Request göndererek katkıda bulunun.

