Linux Privilege Escalation Scanner
Bu proje, Linux sistemlerinde yetki yükseltme güvenlik açıklarını tespit etmeye yönelik bir tarayıcıdır. SUID bit ayarlı dosyalar, capability ayarları ve yanlış yapılandırmalar gibi potansiyel güvenlik açıklarını kontrol eder.

Özellikler
SUID Binaries: SUID bit ayarlı dosyaları tarar.
Capabilities: Dosyaların sahip olduğu capabilities'leri kontrol eder.
Misconfigurations: Yanlış yapılandırmaları (örneğin, SSH yapılandırma dosyasındaki hatalar, sudoers dosyası izin hataları) tespit eder.
Kullanım
Proje, komut satırında çalıştırılabilir ve belirli parametrelerle konfigüre edilebilir. Aşağıdaki parametreler kullanılabilir:

Zorunlu Parametreler
json
Kopyala
Düzenle
{
    "parametre_adi": {
        "tip": "veri_tipi",
        "açıklama": "parametre açıklaması"
    }
}
Opsiyonel Parametreler
json
Kopyala
Düzenle
{
    "parametre_adi": {
        "tip": "veri_tipi",
        "varsayılan": "değer",
        "açıklama": "parametre açıklaması"
    }
}
Çıktı Formatı
Çıktı JSON formatında döner:

json
Kopyala
Düzenle
{
    "sonuç": {
        "durum": "başarılı/başarısız",
        "veri": {},
        "hata_mesajı": "varsa hata açıklaması"
    }
}
Parametreler
--suid: SUID bit ayarlı dosyaların taranmasını sağlar.
--capabilities: Dosyaların capabilities'lerini kontrol eder.
--misconfig: Yanlış yapılandırmaları tespit eder.
Kurulum
1. Gereksinimler
Proje Python 3.x gerektirir. Ayrıca, aşağıdaki Python kütüphaneleri de gereklidir:

rich
psutil
2. Bağımlılıkları Yükleme
Projenin gereksinimlerini yüklemek için:

bash
Kopyala
Düzenle
pip install -r requirements.txt
Eğer sisteminize bağımlılıkları kurarken externally-managed-environment hatası alırsanız, sanal ortam kullanmanızı öneririz. Bunun için şu adımları takip edebilirsiniz:

bash
Kopyala
Düzenle
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
3. Sanal Ortamı Kullanma
Sanal ortamda projeyi çalıştırabilirsiniz:

bash
Kopyala
Düzenle
source myenv/bin/activate
python3 main.py --suid
Sanal ortamdan çıkmak için:

bash
Kopyala
Düzenle
deactivate
4. Sistem Genelinde Kurulum
Sistem genelinde Python paketlerini yüklemek için, aşağıdaki komutu kullanabilirsiniz (ancak bu durumda sanal ortama gerek olmayacaktır):

bash
Kopyala
Düzenle
sudo apt install python3-rich python3-psutil
5. Çalıştırma
Proje şu şekilde çalıştırılabilir:

bash
Kopyala
Düzenle
python3 main.py --suid
Ve ya:

bash
Kopyala
Düzenle
python3 main.py --capabilities
Ya da:

bash
Kopyala
Düzenle
python3 main.py --misconfig
Herhangi bir parametre verilmezse, yardım mesajı görüntülenir.

Çıktı Örnekleri
--suid Parametresi ile Çıktı:
json
Kopyala
Düzenle
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
}
--misconfig Parametresi ile Çıktı:
json
Kopyala
Düzenle
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
Katkıda Bulunma
Projeye katkıda bulunmak isterseniz, aşağıdaki adımları takip edebilirsiniz:

Projeyi fork edin.
Yeni bir özellik dalı (branch) oluşturun.
Yaptığınız değişiklikleri commit edin.
Değişikliklerinizi ana dala (main branch) pull request olarak gönderin.