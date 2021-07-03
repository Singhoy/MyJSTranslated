# -*- coding: utf-8 -*-
from base64 import b64encode


def btoa(s):
    st = s.encode()
    res = b64encode(st)
    return res.decode()
