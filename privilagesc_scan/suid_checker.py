import os

def check_suid():
    try:
        suid_files = []
        for root, dirs, files in os.walk("/"):
            for file in files:
                filepath = os.path.join(root, file)
                if os.path.isfile(filepath) and (os.stat(filepath).st_mode & 0o4000):
                    suid_files.append(filepath)

        if suid_files:
            return {"suid_files": suid_files}
        else:
            return {"suid_files": []}

    except Exception as e:
        return {"error": str(e)}