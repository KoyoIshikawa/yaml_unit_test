import string
import glob

text = "${hoge} is fuga."
template_text = string.Template(text)
# result = template_text.safe_substitute({'hoge': 'ほげー'})

# "ほげー is fuga." と出力される
print(template_text)
