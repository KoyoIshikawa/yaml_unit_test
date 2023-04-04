import os
import string
import yaml


def print_yaml_keys(obj, key_chain, prefix=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if prefix:
                new_prefix = "{}, '{}'".format(prefix, k)
            else:
                new_prefix = "'{}'".format(k)
            print_yaml_keys(v, key_chain, prefix=new_prefix)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            new_prefix = "{}, {}".format(prefix, i)
            print_yaml_keys(v, key_chain, prefix=new_prefix)
    else:
        if prefix:
            key_chain.append("{}".format(prefix))


def create_tool(obj, file, file_name):
    with open('template_for_string.txt', 'r') as f:

        filename = 'check_{}.py'.format(file_name)
        template_str = ''

        for line in f:
            if "${key_list}" in line:
                key_chain = []
                print_yaml_keys(obj, key_chain)
                for key_list in key_chain:
                    template_str += string.Template(
                        line).substitute(key_list=key_list)
            elif "${path}" in line:
                template_str += string.Template(line).substitute(path=file)
            else
            template_str += line

        with open(filename, 'w') as f:
            f.write(template_str)


# フォルダパス
folder_path = "yaml_list"

# フォルダ内のファイルパスをリストに格納
file_paths = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        file_paths.append(file_path)

for file in file_paths:
    with open(file) as f:
        obj = yaml.safe_load(f)
        file_name = os.path.basename(file)
        create_tool(obj, file, file_name)
