import os
import shutil
import chardet

# Predefiniowana ścieżka do folderu
FOLDER_PATH = r"C:\Users\Admin\Desktop\TestTask\Assets"
# Lista podfolderów do pominięcia (nazwy relatywne do FOLDER_PATH)
FOLDERS_TO_SKIP = ['']

def find_files(folder_path, extension, folders_to_skip):
    found_files = []
    for root, dirs, files in os.walk(folder_path):
        dirs[:] = [d for d in dirs if d not in folders_to_skip]
        for file in files:
            if file.endswith(extension):
                found_files.append(os.path.join(root, file))
    return found_files

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
    result = chardet.detect(raw_data)
    return result['encoding']

def open_and_copy_files(files, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for file in files:
            outfile.write(f"\n\n--- Zawartość pliku: {file} ---\n\n")
            try:
                encoding = detect_encoding(file)
                with open(file, 'r', encoding=encoding) as infile:
                    content = infile.read()
                outfile.write(content)
            except Exception as e:
                outfile.write(f"Nie można otworzyć pliku. Błąd: {str(e)}\n")

# Główna część programu
print(f"Przeszukiwany folder: {FOLDER_PATH}")
print(f"Pomijane podfoldery: {', '.join(FOLDERS_TO_SKIP)}")

# Zmieniamy domyślne rozszerzenie na .gradle
extension = ".gradle"
files = find_files(FOLDER_PATH, extension, FOLDERS_TO_SKIP)

print(f"\nZnalezione pliki z rozszerzeniem {extension}:")
for file in files:
    print(file)

# Zawsze wykonujemy kopiowanie dla plików .gradle
output_file = input("Podaj nazwę pliku wyjściowego (np. output.txt): ")
open_and_copy_files(files, output_file)
print(f"Zawartość plików .gradle została skopiowana do {output_file}")