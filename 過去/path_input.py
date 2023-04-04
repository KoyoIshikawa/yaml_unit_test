import os

# フォルダパス
folder_path = "過去"

# フォルダ内のファイルパスをリストに格納
file_paths = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        file_paths.append(file_path)

print(file_paths)
