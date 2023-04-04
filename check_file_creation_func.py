
import jinja2
import yaml
import os


def print_yaml_keys(obj, elements, element):
    if isinstance(obj, dict):
        for k, v in obj.items():
            element = element + [k]
            print_yaml_keys(v, elements, element)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            element = element + [i]
            print_yaml_keys(v, elements, element)
    else:
        if element:
            elements.append(element)


def create_tool(obj, file_path, file_name):
    # テンプレートファイルの読み込み
    with open('template.txt', 'r') as f:
        template = jinja2.Template(f.read())

        # 変数の定義 出力ファイル名を定義
        filename = 'check_{}.py'.format(file_name)

        # テンプレートに変数を渡してレンダリング
        element = []
        elements = []
        print_yaml_keys(obj, elements, element)
        output = template.render(elements=elements, path=file_path)

        # レンダリング結果をファイルに書き込み
        with open(filename, 'w') as f:
            f.write(output)


# フォルダパス
folder_path = "yaml_list"

# フォルダ内のファイルパスをリストに格納
file_paths = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        file_paths.append(file_path)

for file_path in file_paths:
    with open(file_path) as f:
        obj = yaml.safe_load(f)
        file_name = os.path.basename(file_path)
        create_tool(obj, file_path, file_name)
