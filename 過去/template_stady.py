import jinja2

# テンプレートファイルの読み込み
with open('template.txt', 'r') as f:
    template = jinja2.Template(f.read())

# 変数の定義
filename = 'output_1.py'

# テンプレートに変数を渡してレンダリング
key_chain = ['apple', 'banana', 'orange']
output = template.render(key_chain=key_chain)

# レンダリング結果をファイルに書き込み
with open(filename, 'w') as f:
    f.write(output)
