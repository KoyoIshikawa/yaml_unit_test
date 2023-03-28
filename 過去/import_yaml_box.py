import yaml
from box import Box

# YAMLデータの読み込み
with open('list-distributions.yaml') as f:
    data = yaml.safe_load(f)
