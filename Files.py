# -*- coding: utf-8 -*-
"""
Created on Sun May 15 00:41:27 2022

@author: Ibasanta Chaw
"""
# # file open
# myfile=open('mytxt.txt','wb')
# print('file name Is : ',myfile.name)
# print('file close or not ',myfile.closed)
# print('openning mode : ',myfile.mode)
# myfile.close()

# #writes files
# myf=open('mytxt.txt','w')
# s='''Hi, Basanta chaudhary howw are u...?W3Schools is optimized for learning and training. Examples might be simplified to improve reading and learning. Tutorials, references, and examples are constantly reviewed to avoid errors, but we cannot warrant full correctness of all content. While using W3Schools, you agree to have read and accepted our terms of use, cookie and privacy policy.
# W3Schools is optimized for learning and training. Examples might be simplified to improve reading and learning. Tutorials, references, and examples are constantly reviewed to avoid errors, but we cannot warrant full correctness of all content. While using W3Schools, you agree to have read and accepted our terms of use, cookie and privacy policy.

# Copyright 1999-2022 by Refsnes Data. All Rights Reserved.
# W3Schools is Powered by W3.CSS.


# W3Schools is optimized for learning and training. Examples might be simplified to improve reading and learning. Tutorials, references, and examples are constantly reviewed to avoid errors, but we cannot warrant full correctness of all content. While using W3Schools, you agree to have read and accepted our terms of use, cookie and privacy policy.

# Copyright 1999-2022 by Refsnes Data. All Rights Reserved.
# W3Schools is Powered by W3.CSS.



# Copyright 1999-2022 by Refsnes Data. All Rights Reserved.
# W3Schools is Powered by W3.CSS.


# '''
# myf.write(s)
# myf.close()


#file reads

# my=open('mytxt.txt','r+')
# str=my.read()
# print(str)

#rename file name
import os

# os.rename('mytxt.txt','TextFile.txt')

# os.remove('ok.txt')

# os.mkdir('chaw')
os.listdir()