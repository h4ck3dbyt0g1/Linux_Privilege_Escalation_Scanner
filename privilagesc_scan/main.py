import argparse
import json
from suid_checker import check_suid
from capability_checker import check_capabilities
from misconfig_checker import check_misconfig

def main():
    parser = argparse.ArgumentParser(description="Linux Privilege Escalation Scanner")
    
    # Zorunlu parametreler
    parser.add_argument("--suid", action="store_true", help="SUID binary analizi yap")
    parser.add_argument("--capabilities", action="store_true", help="Capability kontrolü yap")
    parser.add_argument("--misconfig", action="store_true", help="Yanlış yapılandırmaları kontrol et")

    # Opsiyonel parametreler (varsayılan değerleri ile)
    parser.add_argument("--output", default="json", choices=["json", "text"], help="Çıktı formatı (varsayılan: json)")

    args = parser.parse_args()

    result = {"sonuç": {"durum": "başarısız", "veri": {}, "hata_mesajı": ""}}

    try:
        if args.suid:
            result["sonuç"]["veri"]["suid"] = check_suid()
        if args.capabilities:
            result["sonuç"]["veri"]["capabilities"] = check_capabilities()
        if args.misconfig:
            result["sonuç"]["veri"]["misconfig"] = check_misconfig()

        result["sonuç"]["durum"] = "başarılı"
    
    except Exception as e:
        result["sonuç"]["hata_mesajı"] = str(e)

    # Çıktıyı istenilen formatta yazdır
    if args.output == "json":
        print(json.dumps(result, indent=4))
    else:
        # Eğer "text" formatı istendiyse, çıktıyı metin formatında yazdır
        print("Çıktı (JSON olarak alındı):")
        print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()