import os

folder_path = "yaml_list"

# print(os.listdir(folder_path))

files = os.listdir(folder_path)
files_dir = [f for f in files if os.path.isdir(os.path.join(folder_path, f))]
print(files_dir)    # ['dir1', 'dir2']

folder_path =
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        file_paths.append(file_path)
