# -*- coding: utf-8 -*-
from base64 import b64encode
from json import dumps
from math import floor
from random import random
from time import time

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

"""
原文：
var publicNewKey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCmljIi6pIJL8yfXnvg0MYkXFvCExKvZ/dSAdfOnfZKHsHGyVrct/z0sXdNQr5i+HWE8VFQud9TSGevOMD4zJbz433j3zNqH6gHlT0IUSs8wwu3ucAzJjMrt92789oCrJrbycomwwTj+sAhNdBxUPlw0dY853JEc7FCBDxRPd58twIDAQAB";

function getNewEncodeStr(raw) {
    var encodeJson = JSON.stringify({ "num": generateUUID(), "stamp": new Date().getTime(), "username": raw });
    var encrypt = new JSEncrypt();
    encrypt.setPublicKey(publicNewKey);
    return encrypt.encrypt(encodeJson);
}

function generateUUID() {
    var d = new Date().getTime();
    var uuid = 'xxxxxxxxxxxxyxxxyxxxxxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        var r = (d + Math.random() * 16) % 16 | 0;
        d = Math.floor(d / 16); return (c == 'x' ? r : (r & 0x3 | 0x8)).toString(16);
    });
    return uuid;
};
"""


def 加密(pwd):
    key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCmljIi6pIJL8yfXnvg0MYkXFvCExKvZ/dSAdfOnfZKHsHGyVrct/z0sXdNQr5i+HWE8VFQud9TSGevOMD4zJbz433j3zNqH6gHlT0IUSs8wwu3ucAzJjMrt92789oCrJrbycomwwTj+sAhNdBxUPlw0dY853JEc7FCBDxRPd58twIDAQAB"
    public_key = '-----BEGIN PUBLIC KEY-----\n' + key + '\n-----END PUBLIC KEY-----'
    rsakey = RSA.importKey(public_key)
    cipher = PKCS1_v1_5.new(rsakey)
    uid = generate_uuid()
    t = int(time() * 1000)
    js = {"num": uid, "stamp": t, "username": pwd}
    js = dumps(js).replace(" ", "")
    cipher_text = b64encode(cipher.encrypt(js.encode("utf-8")))
    return cipher_text.decode()


def generate_uuid():
    la = [_ for _ in range(10, 36)]
    lb = [chr(_) for _ in range(ord("a"), ord("z") + 1)]
    dic = dict(zip(la, lb))
    uuid = 'xxxxxxxxxxxxyxxxyxxxxxxxxxxxxxxx'
    s = ""
    d = int(time() * 1000)
    for c in uuid:
        _r = int((d + random() * 16) % 16) or 0
        d = floor(d / 16)
        if c != "x":
            _r = int(_r and 0x3 or 0x8)
        s += str(_r) if _r < 10 else dic[_r]
    return s


if __name__ == "__main__":
    k = "UzqJjJlfzBTDkHs5"
    a = 加密(k)
    print(a)
