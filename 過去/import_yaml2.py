import yaml

# YAMLデータの読み込み
with open('list-distributions.yaml') as f:
    data = yaml.safe_load(f)

def key_chain(parent, child):
  if isinstance(parent, dict) or isinstance(parent, list):
    # もし、valueがdictの場合、ディクトの取り出し方を実行
    if isinstance(parent,dict):
        for key, value in parent.items():
            key = list(parent.keys())
            return value
    elif isinstance(parent, list):
      for key, value in parent[0].items():
            parent = value
  else:
    for key, value in parent():
      return key + value



# a = key_chain(data)
# b = key_chain(a)
# c = key_chain(b)

# print(c)

print (data)
