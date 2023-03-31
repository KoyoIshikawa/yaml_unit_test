import check_file_creation_func
import jinja2
import yaml


def print_yaml_keys(obj, key_chain, prefix=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if prefix:
                new_prefix = "{}, \'{}\'".format(prefix, k)
            else:
                new_prefix = "\'{}\'".format(k)
            print_yaml_keys(v, key_chain, prefix=new_prefix)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            new_prefix = "{}, {}".format(prefix, i)
            print_yaml_keys(v, key_chain, prefix=new_prefix)
    else:
        if prefix:
            key_chain.append("{}".format(prefix))


def create_tool(obj):
    # テンプレートファイルの読み込み
    with open('template.txt', 'r') as f:
        template = jinja2.Template(f.read())

        # 変数の定義 出力ファイル名を定義
        service = "cloudfront"
        filename = 'check_{}.py'.format(service)

        # テンプレートに変数を渡してレンダリング
        key_chain = []
        print_yaml_keys(obj, key_chain)
        output = template.render(key_chain=key_chain)

        # レンダリング結果をファイルに書き込み
        with open(filename, 'w') as f:
            f.write(output)


file = "list-distributions.yaml"
with open(file) as f:
    obj = yaml.safe_load(f)

check_file_creation_func.create_tool(obj)
