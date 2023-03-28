import yaml

def print_yaml_keys(obj, prefix=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            new_prefix = "{}.{}".format(prefix, k) if prefix else k
            print_yaml_keys(v, prefix=new_prefix)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            new_prefix = "{}[{}]".format