
import jinja2
import yaml
import os


def print_yaml_keys(obj, elements, elements_list):
    if isinstance(obj, dict):
        for k, v in obj.items():
            elements = elements + ["'{}'".format(k)]
            print_yaml_keys(v, elements, elements_list)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            elements = elements + [i]
            print_yaml_keys(v, elements, elements_list)
    else:
        if elements:
            elements_list.append(elements)


def create_check_file(contents, file_name):
    # テンプレートファイルの読み込み
    with open('template.txt', 'r') as f:
        template = jinja2.Template(f.read())

        # 変数の定義 出力ファイル名を定義
        aws_service_name = 'check_{}.py'.format(file_name)
        output = template.render(contents=contents)
        # レンダリング結果をファイルに書き込み
        with open(aws_service_name, 'w') as f:
            f.write(output)


# フォルダパス
folder_path = "yaml_list"

# フォルダ内のファイルパスをリストに格納
file_paths = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        file_paths.append(file_path)

contents = []
for file_path in file_paths:
    with open(file_path) as f:
        obj = yaml.safe_load(f)
        elements = []
        elements_list = []
        print_yaml_keys(obj, elements, elements_list)
        contents.append(dict(file_path=file_path, elements_list=elements_list))

file_name = "cloudfront"
create_check_file(contents, file_name)
