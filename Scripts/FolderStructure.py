import os

DEFAULT_PATH = r"C:\Users\Admin\Desktop\TestTask"
EXCLUDED_FOLDERS = {'.git', '.plastic', '.vs', 'Library'}

def generate_structure(startpath, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(startpath):
            dirs[:] = [d for d in dirs if d not in EXCLUDED_FOLDERS]
            
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * level
            f.write(f'{indent}{os.path.basename(root)}/\n')
            subindent = ' ' * 4 * (level + 1)
            for file in files:
                f.write(f'{subindent}{file}\n')

if __name__ == "__main__":
    folder_path = input(f"Podaj ścieżkę do folderu (domyślnie {DEFAULT_PATH}): ") or DEFAULT_PATH
    output_file = input("Podaj nazwę pliku wyjściowego (np. struktura.txt): ")
    
    if os.path.exists(folder_path):
        generate_structure(folder_path, output_file)
        print(f"Struktura została zapisana do pliku {output_file}")
        print(f"Wyłączone foldery: {', '.join(EXCLUDED_FOLDERS)}")
    else:
        print("Podana ścieżka nie istnieje.")
