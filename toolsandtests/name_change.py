#lumen becomes acumenimport os

import os


def refactor_project(root_dir):
    print(f"[*] Début de la transformation morphologique du projet à partir de : {root_dir}")
    
    # 1. Mutation des noms de fichiers et de dossiers (parcours bottom-up pour les dossiers)
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # Traitement des fichiers
        for filename in filenames:
            if "lumen" in filename.lower():
                old_path = os.path.join(dirpath, filename)
                new_filename = (
                    filename.replace("lumen", "acumen")
                            .replace("Lumen", "Acumen")
                            .replace("LUMEN", "ACUMEN")
                )
                new_path = os.path.join(dirpath, new_filename)
                os.rename(old_path, new_path)
                print(f"[FICHIER] {filename} -> {new_filename}")
        
        # Traitement des dossiers
        for dirname in dirnames:
            if "lumen" in dirname.lower():
                old_path = os.path.join(dirpath, dirname)
                new_dirname = (
                    dirname.replace("lumen", "acumen")
                           .replace("Lumen", "Acumen")
                           .replace("LUMEN", "ACUMEN")
                )
                new_path = os.path.join(dirpath, new_dirname)
                os.rename(old_path, new_path)
                print(f"[DOSSIER] {dirname} -> {new_dirname}")

    # 2. Mutation du contenu textuel interne des fichiers
    # On relance un parcours pour cibler les nouveaux chemins mis à jour
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            
            # Éviter de s'auto-modifier en plein vol pour prévenir les interférences d'E/S
            if filename == "name_change.py":
                continue
            
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                if "lumen" in content.lower():
                    new_content = (
                        content.replace("lumen", "acumen")
                               .replace("Lumen", "Acumen")
                               .replace("LUMEN", "ACUMEN")
                    )
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"[CONTENU] Actualisé : {file_path}")
            except (UnicodeDecodeError, PermissionError):
                # Ignore les fichiers binaires ou non-textuels
                pass

    print("[*] Transformation achevée avec succès. Lumen est devenu Acumen.")

if __name__ == "__main__":
    # Déduction de la racine du projet (remonte d'un niveau depuis 'toolsandtests')
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    refactor_project(project_root)