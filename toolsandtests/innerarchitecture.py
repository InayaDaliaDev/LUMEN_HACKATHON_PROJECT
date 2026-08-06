from pathlib import Path

# ==============================================================================
# CONFIGURATION DES FILTRES
# ==============================================================================
IGNORE_DIRS = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    "env",
    ".streamlit",
    ".pytest_cache",
    ".vscode",
}

IGNORE_FILES = {
    ".DS_Store",
    ".gitignore",
    "print_tree.py",  # On ignore le script lui-même dans l'affichage
}


def generate_tree(dir_path: Path, prefix: str = "") -> None:
    """Parcourt l'espace de travail et projette une arborescence ASCII propre et triée."""
    try:
        # Tri déterministe : dossiers d'abord, puis fichiers, par ordre alphabétique
        entries = sorted(
            dir_path.iterdir(), key=lambda e: (not e.is_dir(), e.name.lower())
        )
    except PermissionError:
        return

    # Filtrage des éléments non pertinents
    entries = [
        e
        for e in entries
        if e.name not in IGNORE_DIRS
        and e.name not in IGNORE_FILES
        and not e.name.startswith(".")
    ]

    count = len(entries)
    for i, entry in enumerate(entries):
        is_last = i == (count - 1)
        connector = "└── " if is_last else "├── "

        print(f"{prefix}{connector}{entry.name}")

        if entry.is_dir():
            extension = "    " if is_last else "│   "
            generate_tree(entry, prefix + extension)


if __name__ == "__main__":
    root_dir = Path(".")
    print(f"\n📁 {root_dir.resolve().name}/")
    generate_tree(root_dir)
    print()