import os

def print_tree(start_path, exclude_dirs=None, prefix=""):
    if exclude_dirs is None:
        exclude_dirs = {'.git', 'venv', 'pycache'}

    # Получаем список всех элементов, исключая указанные папки
    entries = sorted(os.listdir(start_path))
    entries = [entry for entry in entries if entry not in exclude_dirs]

    # Разделяем на папки и файлы
    dirs = [entry for entry in entries if os.path.isdir(os.path.join(start_path, entry))]
    files = [entry for entry in entries if not os.path.isdir(os.path.join(start_path, entry))]


# Укажите путь к проекту
project_path = "C:\\Programs\\audio_test"
print(f"Дерево проекта для: {project_path}")
print_tree(project_path)