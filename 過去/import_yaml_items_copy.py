import jinja2
import yaml


def print_yaml_keys(obj, prefix=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if prefix:
                new_prefix = "{}, \"{}\"".format(prefix, k)
            else:
                new_prefix = "\"{}\"".format(k)
            print_yaml_keys(v, prefix=new_prefix)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            new_prefix = "{}, {}".format(prefix, i)
            print_yaml_keys(v, prefix=new_prefix)
    else:
        if prefix:
            with open('output.txt', 'a') as f:
                f.write("[{}]\n".format(prefix))

            # テンプレートファイルの読み込み
            with open('template.txt', 'r') as f:
                template = jinja2.Template(f.read())

            # 変数の定義 出力ファイル名を定義
            service = "cloudfront"
            filename = 'check_{}.py'.format(service)

            # テンプレートに変数を渡してレンダリング
            key_chain = prefix
            output = template.render(key_chain=key_chain)

            # レンダリング結果をファイルに書き込み
            with open(filename, 'w') as f:
                f.write(output)

# テンプレートのキーの部分にprefixを入れてやる。


file = "list-distributions.yaml"
with open(file) as f:
    obj = yaml.safe_load(f)

print_yaml_keys(obj)
