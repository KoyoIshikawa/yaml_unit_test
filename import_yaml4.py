import yaml


def print_yaml_keys(obj, prefix=None):
    if prefix is None:
        prefix = []

    if isinstance(obj, dict):
        for k, v in obj.items():
            prefix.append(k)
            print_yaml_keys(v, prefix=prefix)
            prefix.pop()
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            prefix.append(i)
            print_yaml_keys(v, prefix=prefix)
            prefix.pop()
    else:
        with open('output.txt', 'a') as f:
            f.write(f"{prefix}\n")


# yamlファイルの読み込み
with open('list-distributions.yaml', 'r') as f:
    obj = yaml.safe_load(f)

# ファイルへの書き込み
with open('output.txt', 'w') as f:
    print_yaml_keys(obj)
