import yaml

# YAMLデータの読み込み
with open('list-distributions.yaml') as f:
    data = yaml.safe_load(f)

for k, v in data.items():
    for k2,v2 in v.items():
        kv = k + "." + k2
        print(kv)
        print("aaaaaaaa")

    print("-------1")
    
    for k3,v3 in v2[0].items():
        kv2 = kv + "." + k3
        print(kv2)
        print("bbb")

    print("-----2")

    for k3,v3 in v2[0].items():
        if isinstance(v3,dict):
            for k4,v4 in v3.items():
                kv3 = kv2 + "." + k4
                print(kv3)
                if isinstance(v4,list):
                    for k5,v5 in v4[0].items():
                        kv4 = kv3 + "." + k5
                        print(kv4)
    print("-----4")