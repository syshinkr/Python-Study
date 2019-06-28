import re

import Map as Map

data = '''
    
'''
regex = r"\d{6}[-]\d{7}"
regex2 = "[a-z]+ "


pat = re.compile(regex2)
m4 = pat.findall("jwa's python")
print(m4)

