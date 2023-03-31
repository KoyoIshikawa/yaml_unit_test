import string
import yaml


def print_yaml_keys(obj, key_chain, prefix=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if prefix:
                new_prefix = f"{prefix}, '{k}'"
            else:
                new_prefix = f"'{k}'"
            print_yaml_keys(v, key_chain, prefix=new_prefix)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            new_prefix = f"{prefix}, {i}"
            print_yaml_keys(v, key_chain, prefix=new_prefix)
    else:
        if prefix:
            key_chain.append(f"{prefix}")


def create_tool(obj):
    # テンプレートファイルの読み込み
    with open('template_for_string.txt', 'r') as f:

        service = "cloudfront"
        filename = 'check_{}.py'.format(service)
        template_str = ''

        for line in f:
            if '${key_list}' in line:
                key_chain = []
                print_yaml_keys(obj, key_chain)
                for key_list in key_chain:
                    template_str += string.Template(
                        line).substitute(key_list=key_list)
            else:
                template_str += line

        with open(filename, 'w') as f:
            f.write(template_str)


file = "list-distributions.yaml"
with open(file) as f:
    obj = yaml.safe_load(f)

create_tool(obj)
