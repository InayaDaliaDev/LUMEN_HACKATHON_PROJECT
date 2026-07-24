import os

OUTPUT_FILE = "full_code.txt"
# Détecte le nom de ce script pour ne pas s'auto-inclure
CURRENT_SCRIPT = os.path.basename(__file__)

with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:
    for root, dirs, files in os.walk("."):
        # Ignorer les dossiers cachés (.git, .vscode...) et les envs virtuels
        dirs[:] = [
            d for d in dirs 
            if not d.startswith(".") and d not in ("venv", "env", ".venv", "__pycache__")
        ]
        
        for file in files:
            if file.endswith(".py") and file != CURRENT_SCRIPT:
                # Normalise le chemin d'accès
                path = os.path.normpath(os.path.join(root, file))
                
                outfile.write(f"\n{'='*50}\nFILE: {path}\n{'='*50}\n\n")
                
                with open(path, "r", encoding="utf-8", errors="ignore") as infile:
                    outfile.write(infile.read())

print(f"✅ Terminé ! Le fichier '{OUTPUT_FILE}' a été créé à la racine de ton projet.")