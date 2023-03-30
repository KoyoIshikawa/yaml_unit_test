import yaml
import ast

file = "list-distributions.yaml"
with open(file) as f:
    file = yaml.safe_load(f)

path = 'output.txt'

with open(path) as f:
    s = f.read()

# output.txtを一行ずつ分解し,list化
lines = s.splitlines()

# output.txtの値がなくなるまで実行
for line in lines:
    # output.txtから値を取得
    key_chain = line.split('=')[0]
    expected_value = line.split('=')[1]
    # key_cahinをlist型に変換
    listing_key_chain = ast.literal_eval(key_chain)
    # valueの初期化
    value = file.copy()

    # listing_key_chainがなくなるまでvalueに内容をvalueを上書き
    for element in listing_key_chain:
        value = value[element]

    print("yamlの値:{}".format(value))
    print("期待値:{}".format(expected_value))
    if value == expected_value:
        print("OK")
    else:
        print("NG")

    print("===============")
