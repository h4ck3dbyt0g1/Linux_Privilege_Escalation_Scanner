import subprocess

def check_capabilities():
    try:
        result = subprocess.run(["getcap", "-r", "/"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        if result.stdout:
            return {"capabilities": result.stdout.strip().split("\n")}
        else:
            return {"capabilities": []}
    except FileNotFoundError:
        return {"error": "'getcap' komutu sistemde bulunamadı. Lütfen gerekli paketi yükleyin."}