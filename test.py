import os

with open("full_code.txt", "w", encoding="utf-8") as outfile:
    for root, dirs, files in os.walk("."):
        # Ignorer les dossiers cachés et les environnements virtuels
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ('venv', '__pycache__')]
        for file in files:
            if file.endswith(".py") and file != "export.py":
                path = os.path.join(root, file)
                outfile.write(f"\n{'='*50}\nFILE: {path}\n{'='*50}\n\n")
                with open(path, "r", encoding="utf-8", errors="ignore") as infile:
                    outfile.write(infile.read())

print("✅ Terminé ! Le fichier 'full_code.txt' a été créé à la racine de ton projet.")