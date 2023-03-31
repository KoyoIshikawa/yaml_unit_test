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
        template_str = f.read()

        # 変数の定義 出力ファイル名を定義
        service = "cloudfront"
        filename = 'check_{}.py'.format(service)

        # テンプレートに変数を渡してレンダリング
        key_chain = []
        print_yaml_keys(obj, key_chain)
        template = string.Template(template_str)
        output = template.substitute(key_chain=key_chain)

        # レンダリング結果をファイルに書き込み
        with open(filename, 'w') as f:
            f.write(output)
