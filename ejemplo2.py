# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 18:20:36 2019

@author: CEC
"""

aclnum = int(input("WHAT IS THE ipV4 aCL NUMBER "))
if aclnum >=1 and aclnum <= 99:
    print("this is a standard IPv4 ACL.")
elif aclnum >=100 and aclnum <= 199:
     print("this is a extended")
else:
    print("this is not a standard or extend IP ACL.")
     