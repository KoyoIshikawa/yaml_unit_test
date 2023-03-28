import yaml
import ast

file = "list-distributions.yaml"
with open(file) as f:
    file = yaml.safe_load(f)

# target = {
#     "elements": ["DistributionList", "Items", 0, "ARN"], "aaa": "arn:aws:cloudfront::000000000:distribution/E1CCWMEEVPCZP9"
# }

# # value = obj.copy()
# for element in target['elements']:
#     value = value[element]

# print(value)

# print("---------------------")
path = 'output.txt'

with open(path) as f:
    s = f.read()

lines = s.splitlines()

print(lines)
print("========")
for line in lines:
    left = line.split('=')[0]
    right = line.split('=')[1]
    aaa = ast.literal_eval(left)
    print(aaa)
    print("==")
    value = file.copy()
    for element in aaa:
        value = value[element]

    print("yamlの値:{}".format(value))
    print("期待値:{}".format(right))
    if value == right:
        print("OK")
    else:
        print("NG")

    print("===============")
