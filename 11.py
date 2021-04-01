#coding:utf-8
from Cryptodome.Cipher import AES
import base64
import os
import time
#AES密文（base64编码后的）存放位置#

input_file = open("C:/Users/dell/Desktop/1.txt", 'r')

key = '2c627233c52031e4'
base64_AES_data = input_file.read()
AES_DATA = base64.b64decode(base64_AES_data.encode(encoding='utf-8'))
cipher = AES.new(key, AES.MODE_ECB)
DATA = str(cipher.decrypt(AES_DATA))
#解密后的.class文件存放位置
output_file = open("C:/Users/dell/Desktop/21.class", 'w')
output_file.write(DATA)
output_file.close()
