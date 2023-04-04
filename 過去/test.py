import os

folder_path = '/Users/koyoishikawa/Desktop/python_yaml/過去'  # フォルダのパス
file_paths = []  # ファイルの相対パスを格納するリスト

for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_paths.append(os.path.relpath(
            os.path.join(root, file), folder_path))

print(file_paths)
