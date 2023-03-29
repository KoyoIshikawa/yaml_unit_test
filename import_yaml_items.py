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
                f.write("[{}]=\n".format(prefix))


file = "list-distributions.yaml"
with open(file) as f:
    obj = yaml.safe_load(f)

print_yaml_keys(obj)
