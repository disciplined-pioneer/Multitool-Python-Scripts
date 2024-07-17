import os

def find_python_files(base_path, exclude_folders):
    python_files = []

    for root, dirs, files in os.walk(base_path):
        # Исключаем нежелательные папки
        dirs[:] = [d for d in dirs if d not in exclude_folders]

        # Проверяем файлы в текущей директории
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))

    return python_files

def count_lines(filename):
    with open(filename, encoding='utf-8') as f:
        cnt = sum(1 for line in f)
    return int(cnt)

# Основной путь проекта
base_path = r"C:\Programs\Dex_project\SharshovMaksim_Very_Hight"
# Папки для исключения
exclude_folders = {".git", "venv"}

# Поиск Python файлов
python_files = find_python_files(base_path, exclude_folders)

# Вывод результата
s = 0
print("Найденные файлы:")
for file in python_files:
    if file != 'C:\\Programs\\StudyBoost\\database\\convert_csv.py':
        result = count_lines(file.replace("\\", "\\\\"))
        print(file.replace("\\", "\\\\"))
        s += result
print(f'\n\nОбщее количество строчек: {s}')
