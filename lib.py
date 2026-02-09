import os
import subprocess

def get_shortcuts():
    shortcuts = os.system(f"osascript -e 'tell application \"Shortcuts\" to get name of every shortcut'")
    return shortcuts

def use_model(texte, shortcut: str="use_a_model"):
    try:
        processus = subprocess.run(
            ["shortcuts", "run", shortcut],
            input=str(texte),
            text=True,
            capture_output=True
        )
        if processus.returncode == 0:
            if processus.stdout.startswith("{\\rtf"):
                nettoyage = subprocess.run(
                    ["textutil", "-convert", "txt", "-stdin", "-stdout"],
                    input=processus.stdout,
                    text=True,
                    capture_output=True
                )
                return nettoyage.stdout.strip()
            return processus.stdout.strip()
    except Exception as e:
        print(e)