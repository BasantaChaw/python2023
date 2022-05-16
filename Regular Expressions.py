# -*- coding: utf-8 -*-
"""
Created on Sun May 15 10:17:21 2022

@author: Ibasanta Chaw
"""

import re
line = "Cats are samrter than dogs"
matchOnj = re.match(r'(.*) are (.*?).*', line, re.M | re.I)
if matchOnj:
    print('mathObj.group() : ', matchOnj.group())
    print('mathObj.group(1) : ', matchOnj.group(1))
    print('mathObj.group(2) : ', matchOnj.group(2))
else:
    print('No Match !')
