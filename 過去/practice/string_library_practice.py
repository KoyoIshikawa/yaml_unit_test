import string

with open('../template_for_string.txt', 'r') as f:
    template_str = ''
    for line in f:
        if '${key}' in line:
            data = ["aaa", "bbb", "ccc"]
            for name in data:
                template_str += string.Template(line).substitute(key=name)
        else:
            template_str += line

print(template_str)
