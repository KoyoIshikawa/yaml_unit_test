import check_file_creation_func as check_file_creation_func
import yaml

file = "list-distributions.yaml"
with open(file) as f:
    obj = yaml.safe_load(f)

check_file_creation_func.create_tool(obj)
