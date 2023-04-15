"""
对称加密算法v230415
"""

import os
import time
import string
os.system("cls")

#公钥
try:
    #访问配置文件查找自定义公钥
    i = "[自定义公钥]"
    with open("config.ini","r+",encoding="utf-8") as u:
        p = u.readlines()
    ty = 0
    while ty <= len(p):
        try:
            if p[ty].split('=')[0].strip() == "Public_Key":
                chars = p[ty].split('=')[1].strip()
                break
            else:
                ty += 1
                continue
        except:
            ty += 1
    char = chars
    del char,ty,p
except:
    #当自定义公钥不存在时使用冗余公钥
    i = "[冗余公钥]"
    chars = string.ascii_letters + string.digits +string.punctuation

#选择模式
inp = input(f"·选择模式{i}\n[1]加密模式\n[2]解密模式\n选择:")
os.system("cls")
if inp == "1":
    print(f"·加密模式{i}")
elif inp == "2":
    print(f"·解密模式{i},请保证使用的公钥与密钥对应")
else:
    exit()

#输入文本和密钥
file = input("输入文本:")
password = input("输入密钥:")
pwdnum = 1
filenum = 0
filemax = len(file)-1
pwdmax = len(password)-1
passstr = list(password)[0]

#生成密匙列表
while filenum < filemax:
    passstr = passstr + list(password)[pwdnum]
    filenum += 1
    pwdnum += 1
    if pwdnum > pwdmax:
        pwdnum = 0
filenum = 0
filecheck = ""

if inp == "1":
    #加密
    while filenum <= filemax:
        if list(file)[filenum] in chars:
            #生成
            i = chars.find(list(file)[filenum]) + chars.find(list(passstr)[filenum])
            if i >= len(chars):
                i -= len(chars)
            filecheck = filecheck + list(chars)[i]
        elif list(file)[filenum] == " ":
            #空格
            filecheck = filecheck + " "
        else:
            input("文本格式错误")
            exit()
        filenum += 1
    inp = input(f"·加密结果(输入save保存结果)\n{filecheck}\n")
    if inp == "save":
        t = time.strftime("%Y-%m-%d %H:%M",time.localtime(time.time()))
        with open("encryption.txt","a",encoding="utf-8") as u:
            u.write(f"{t}|模式 加密\n")
            u.write(f"公钥 {chars}\n")
            u.write(f"文本 {file}\n")
            u.write(f"密钥 {password}\n")
            u.write(f"结果 {filecheck}\n\n")


elif inp == "2":
    #解密
    while filenum <= filemax:
        if list(file)[filenum] in chars:
            #生成
            i = chars.find(list(file)[filenum]) - chars.find(list(passstr)[filenum])
            if i < 0:
                i += len(chars)
            filecheck = filecheck + list(chars)[i]
        elif list(file)[filenum] == " ":
            #空格
            filecheck = filecheck + " "
        else:
            input("文本格式错误")
            exit()
        filenum += 1
    inp = input(f"·解密结果(输入save保存结果)\n{filecheck}\n")
    if inp == "save":
        t = time.strftime("%Y-%m-%d %H:%M",time.localtime(time.time()))
        with open("encryption.txt","a",encoding="utf-8") as u:
            u.write(f"{t}|模式 解密\n")
            u.write(f"公钥 {chars}\n")
            u.write(f"文本 {file}\n")
            u.write(f"密钥 {password}\n")
            u.write(f"结果 {filecheck}\n\n")