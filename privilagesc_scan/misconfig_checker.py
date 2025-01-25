import os

def check_misconfig():
    try:
        misconfig = []
        
        # SSH yapılandırması kontrolü
        ssh_config_path = "/etc/ssh/sshd_config"
        if os.path.exists(ssh_config_path):
            with open(ssh_config_path, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if "PermitRootLogin yes" in line:
                        misconfig.append("Root kullanıcı girişi SSH ile izinli!")
        
        # Diğer yanlış yapılandırma örneği: Sudoers dosyasının izinleri
        sudoers_path = "/etc/sudoers"
        if os.path.exists(sudoers_path):
            sudoers_stat = os.stat(sudoers_path)
            if sudoers_stat.st_mode & 0o022:  # 022 -> world-writable kontrolü
                misconfig.append("Sudoers dosyası yanlış izinlere sahip!")

        if misconfig:
            return {"misconfigurations": misconfig}
        else:
            return {"misconfigurations": []}

    except Exception as e:
        return {"error": str(e)}