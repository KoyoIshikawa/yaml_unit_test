
import jinja2
import yaml
import os
import copy


def print_yaml_keys(obj, elements, elements_list):
    new_elements = copy.copy(elements)

    if isinstance(obj, dict):
        for k, v in obj.items():
            new_elements.append("'{}'".format(k))
            print_yaml_keys(v, new_elements, elements_list)
            new_elements.pop()
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            new_elements.append(i)
            print_yaml_keys(v, new_elements, elements_list)
            new_elements.pop()
    else:
        if elements:
            elements_list.append(new_elements)


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

# フォルダの一覧を取得(folder_info = [{path: , name:])
folder_and_file_list = os.listdir(folder_path)
aws_service_dir_list = []
for f in folder_and_file_list:
    if os.path.isdir(os.path.join(folder_path, f)):
        aws_service_dir_list.append(f)

for aws_service_dir in aws_service_dir_list:
    # フォルダ内のファイルパスをリストに格納
    file_paths = []
    aws_service_dir_folder_path = '{}/{}'.format(folder_path, aws_service_dir)
    for root, dirs, files in os.walk(aws_service_dir_folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)

    # テンプレートにいれるすべての変数をcontentsに格納
    contents = []
    for file_path in file_paths:
        with open(file_path) as f:
            obj = yaml.safe_load(f)
            elements = []
            elements_list = []
            print_yaml_keys(obj, elements, elements_list)
            contents.append(
                dict(file_path=file_path, elements_list=elements_list))

    file_name = aws_service_dir
    create_check_file(contents, file_name)
