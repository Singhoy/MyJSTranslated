# -*- coding: utf-8 -*-
from base64 import b64encode


def btoa(s):
    if not isinstance(s, str):
        s = str(s)
    st = s.encode()
    res = b64encode(st)
    return res.decode()
