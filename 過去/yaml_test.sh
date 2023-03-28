#/bin/zsh

input_file=list-distributions.yaml

if [ "HEAD/ GET" = $(yq e '.DistributionList.Items[0].CacheBehaviors.Items[].AllowedMethods.CachedMethods.Items[]' ${input_file}) ] ; then
  arg=$(yq e '.DistributionList.Items[0].ARN' ${input_file}) # YAMLで設定されている値を保持
  line_num=$(sed -n "/${arg}/=" list-distributions.yaml) # 不一致行数を特定
  echo "NG ${line_num}行目がおかしい。" 
fi