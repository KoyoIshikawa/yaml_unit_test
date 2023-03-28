import yaml
import output

file = "list-distributions.yaml"
with open(file) as f:
    obj = yaml.safe_load(f)

print(output.DistributionList_Items_0_ARN)
print(obj["DistributionList"]["Items"][0]["ARN"])

targets = [{"DistributionList_Items_0_ARN",
           "arn:aws:cloudfront::165181188474:distribution/E1CCWMEEVPCZP9"}, {"DistributionList_Items_0_Aliases_Quantity", ""}]

# targets2 = [{"DistributionList", "Items", 0, "ARN"], }] = の右と左で分ける
# 左側は_を起点に文字列を分ける
if output.DistributionList_Items_0_ARN == obj["DistributionList"]["Items"][0]["ARN"]:
    print("OK")
else:
    print("NG")

for element as
