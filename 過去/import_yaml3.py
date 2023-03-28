import yaml

def print_yaml_keys(obj, prefix=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if prefix:
                new_prefix = f"{prefix}.{k}"
            else:
                new_prefix = k
            print_yaml_keys(v, prefix=new_prefix)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            new_prefix = f"{prefix}[{i}]"
            print_yaml_keys(v, prefix=new_prefix)
    else:
        if prefix:
            with open('output.txt', 'a') as f:
                f.write(f"{prefix}\n")

# yamlファイルの読み込み
with open('list-distributions.yaml', 'r') as f:
    obj = yaml.safe_load(f)

# ファイルへの書き込み
with open('output.txt', 'w') as f:
    print_yaml_keys(obj, file=f)