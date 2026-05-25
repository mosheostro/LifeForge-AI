from pathlib import Path

# Папка, где лежит скрипт
folder = Path(__file__).parent

# Название итогового файла
output_file = folder / "master_coach.md"

# Все markdown-файлы
md_files = sorted(folder.glob("*.md"))

with open(output_file, "w", encoding="utf-8") as outfile:
    for md_file in md_files:

        # Чтобы итоговый файл не добавлялся сам в себя
        if md_file.name == "master_coach.md":
            continue

        print(f"Добавляется: {md_file.name}")

        # Заголовок файла
        outfile.write(f"\n\n# {md_file.stem}\n\n")

        # Содержимое
        outfile.write(md_file.read_text(encoding="utf-8"))

        # Разделитель
        outfile.write("\n\n---\n\n")

print("\nГотово!")
print(f"Создан файл: {output_file}")
