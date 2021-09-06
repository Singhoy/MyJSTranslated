# -*- coding: utf-8 -*-
"""
原文：
password = CryptoJS.AES.encrypt(CryptoJS.enc.Utf8.parse(pwd), CryptoJS.enc.Utf8.parse(key), {
    iv: CryptoJS.enc.Utf8.parse(key),
    mode: CryptoJS.mode.CBC,
    padding: CryptoJS.pad.Pkcs7
}).toString();
"""
from base64 import encodebytes

from Crypto.Cipher import AES


def 加密(pwd, key):
    """
    :param pwd: 需要加密的字符串
    :param key: 加密密钥，16个字符
    
    :return: 加密后的字符串
    """
    aes = AES.new(str.encode(key), AES.MODE_CBC, IV=key.encode())
    return str(encodebytes(aes.encrypt(序列化(pwd))), encoding='utf8').replace('\n', '')


def 序列化(s):
    while len(s) % 16 != 0:
        s += (16 - len(s) % 16) * chr(16 - len(s) % 16)
    return s.encode()


if __name__ == "__main__":
    pwd = "4548af8a455f9c8e"
    key = "85ddcd789dfa10df"
    a = 加密(pwd, key)
    print(a)
