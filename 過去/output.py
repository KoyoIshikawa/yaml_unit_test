import yaml
import os
import sys
import cheke_func

dir = os.getcwd()
account_env = sys.argv[1]

env, account_env = cheke_func.setup_value(account_env)
system = 'system'
section = 'section'
name_prefix = '{}-{}-{}'.format(system, env, section)

taraget = [
    {'file': '/Users/koyoishikawa/Desktop/python_yaml/list-distributions.yaml',
     'parameters': [
         {'elements': ["${key_chain}"], 'expected_value': ''},
         {'elements': ["${key_chain}"], 'expected_value': ''},
     ]
     }
]